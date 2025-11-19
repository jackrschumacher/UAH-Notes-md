import re
import os
import urllib.parse
from pathlib import Path
from collections import defaultdict

# --- Configuration ---
ROOT_DIRECTORY = '.' 
ASSET_FOLDER_NAME = 'assets'
INDEX_FILENAME = 'index.md'

IGNORE_FILES = ['convert_folder_links.py', INDEX_FILENAME, 'converter.py', '_config.yml', 'CNAME']
IGNORE_DIRS = ['.git', 'assets', '_site']

ASSET_EXTENSIONS = (
    'png', 'jpg', 'jpeg', 'gif', 'svg', 'webp', 'pdf', 'mp4', 'mp3',
    'zip', 'txt', 'csv', 'xls', 'xlsx', 'doc', 'docx'
)

# --- CSS TO INJECT ---
# We keep the CSS to handle any other sizing quirks gracefully
STYLE_FIX = """
<style>
  h1 { font-size: 1.5em; }
  h2 { font-size: 1.3em; }
  h3 { font-size: 1.1em; }
  li h1, li h2, li h3, li h4 { font-size: 1em !important; margin: 0 !important; }
</style>
"""

# --- Regex Patterns ---
ASSET_PATTERN = re.compile(r'(!?)\[\[(.*?\.(?:' + '|'.join(ASSET_EXTENSIONS) + r'))\]\]', re.IGNORECASE)
NOTE_PATTERN = re.compile(r'\[\[(.*?)\]\]')
STANDARD_LINK_PATTERN = re.compile(r'(\[[^\]]+\]\([^)]+)\.md(\)|#)') 
QUOTE_PATTERN = re.compile(r'#\+BEGIN_QUOTE\s*(.*?)\s*#\+END_QUOTE', re.DOTALL | re.IGNORECASE)

TAGS_LINE_PATTERN = re.compile(r'^\s*[-*]?\s*tags::\s*(.*)$', re.MULTILINE | re.IGNORECASE)
JUNK_PROPERTY_PATTERN = re.compile(r'^\s*[-*]?\s*(id|logseq\.[a-z0-9-]+|collapsed|icon)::.*$', re.MULTILINE | re.IGNORECASE)

def force_posix_path(path_obj):
    return str(path_obj).replace(os.sep, '/')

def encode_path(path_str):
    clean_path = path_str.replace('\\', '/')
    return urllib.parse.quote(clean_path, safe='/')

def convert_quotes_to_markdown(content):
    def replacer(match):
        block_content = match.group(1)
        return '\n'.join(f'> {line}' for line in block_content.splitlines())
    return QUOTE_PATTERN.sub(replacer, content)

def remove_headings_from_links(content):
    """
    Finds lines that are headings BUT contain a [[Link]].
    Removes the '#' so they become normal list items.
    Example: '- # [[Taxation]]' -> '- [[Taxation]]'
    """
    # Regex: Start of line -> Bullet -> Hash(es) -> Space -> [[
    # We replace it with just: Start of line -> Bullet -> [[
    return re.sub(r'(^\s*[-*]?\s*)#+\s+(\[\[)', r'\1\2', content, flags=re.MULTILINE)

def extract_yaml_tags(content):
    tags = []
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if match:
        yaml_content = match.group(1)
        if 'tags:' in yaml_content:
            tags_section = yaml_content.split('tags:')[1]
            for line in tags_section.split('\n'):
                tag_match = re.match(r'\s*-\s*(.*)', line)
                if tag_match:
                    tags.append(tag_match.group(1).strip())
                elif line.strip() and not line.startswith(' '):
                    break
    return tags

def process_frontmatter_and_clean(content, filename_stem):
    tags = []
    existing_yaml_tags = extract_yaml_tags(content)
    tags.extend(existing_yaml_tags)

    matches = TAGS_LINE_PATTERN.findall(content)
    for tag_string in matches:
        raw_tags = [t.strip() for t in tag_string.split(',')]
        for t in raw_tags:
            clean_t = t.replace('[[', '').replace(']]', '')
            if clean_t not in tags: 
                tags.append(clean_t)
            
    content = TAGS_LINE_PATTERN.sub('', content)
    content = JUNK_PROPERTY_PATTERN.sub('', content)
    content = re.sub(r'\n{3,}', '\n\n', content)

    content = re.sub(r'^---\n.*?\n---\n\n', '', content, flags=re.DOTALL)
    
    yaml_block = "---\n"
    yaml_block += f"title: {filename_stem}\n"
    if tags:
        yaml_block += "tags:\n"
        for t in tags:
            yaml_block += f"  - {t}\n"
    yaml_block += "---\n\n"
        
    return yaml_block + content, tags

def process_file(filepath: Path):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"ERROR reading {filepath}: {e}")
        return None

    original_content = content
    
    # Clean Frontmatter
    content, extracted_tags = process_frontmatter_and_clean(content, filepath.stem)

    current_dir = os.path.dirname(filepath)
    relative_path_to_root = os.path.relpath(ROOT_DIRECTORY, current_dir)
    relative_path_to_assets = Path(relative_path_to_root) / ASSET_FOLDER_NAME

    # --- APPLY THE FIXES ---
    
    # 1. Remove headings from links (The User's Fix)
    content = remove_headings_from_links(content)

    # 2. Convert Asset Links
    def asset_link_replacer(match):
        is_embedded = match.group(1)
        asset_filename = match.group(2)
        full_asset_path_obj = Path(relative_path_to_assets) / asset_filename
        full_asset_path_str = force_posix_path(full_asset_path_obj)
        encoded_path = encode_path(full_asset_path_str)
        return f'![{asset_filename}]({encoded_path})' if is_embedded == '!' else f'[{asset_filename}]({encoded_path})'
            
    def note_link_replacer(match):
        note_title = match.group(1)
        encoded_filename = encode_path(f"{note_title}.html")
        return f'[{note_title}]({encoded_filename})'

    content = ASSET_PATTERN.sub(asset_link_replacer, content)
    content = NOTE_PATTERN.sub(note_link_replacer, content)
    content = STANDARD_LINK_PATTERN.sub(r'\1.html\2', content)
    content = convert_quotes_to_markdown(content)
    
    # 3. Inject Style Fix (Backup safety)
    if "<style>" not in content:
        content += STYLE_FIX

    if content != original_content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"UPDATED: {filepath.name}") 
        except Exception as e:
            print(f"ERROR writing {filepath}: {e}")

    semester_tags = [t for t in extracted_tags if 'semester' in t.lower()]
    
    if semester_tags:
        rel_path = os.path.relpath(filepath, ROOT_DIRECTORY)
        rel_path_str = force_posix_path(rel_path)
        return {
            'title': filepath.stem,
            'path': rel_path_str,
            'tags': semester_tags
        }
    return None

def generate_index_file(semester_data):
    grouped_files = defaultdict(list)
    for entry in semester_data:
        for tag in entry['tags']:
            clean_tag = tag.title() 
            grouped_files[clean_tag].append(entry)

    def natural_sort_key(key):
        return [int(text) if text.isdigit() else text.lower()
                for text in re.split('([0-9]+)', key)]

    sorted_tags = sorted(grouped_files.keys(), key=natural_sort_key)

    lines = ["---", "title: Course Index", "---", "", "# Course Index by Semester", "", "Auto-generated index.", ""]

    for tag in sorted_tags:
        lines.append(f"## {tag}")
        files = sorted(grouped_files[tag], key=lambda x: x['title'])
        for file_info in files:
            web_path = file_info['path'].replace('.md', '.html')
            encoded_path = encode_path(web_path)
            lines.append(f"- [{file_info['title']}]({encoded_path})")
        lines.append("")
    
    lines.append(STYLE_FIX)

    output_path = Path(ROOT_DIRECTORY) / INDEX_FILENAME
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print("=" * 60)
        print(f"SUCCESS: Generated {INDEX_FILENAME}")
        print("=" * 60)
    except Exception as e:
        print(f"ERROR generating index: {e}")

def main():
    print(f"Scanning folder: {os.path.abspath(ROOT_DIRECTORY)}")
    semester_files_found = []

    for dirpath, dirnames, filenames in os.walk(ROOT_DIRECTORY):
        for ignore in IGNORE_DIRS:
            if ignore in dirnames: dirnames.remove(ignore)
            
        for filename in filenames:
            if filename in IGNORE_FILES: 
                continue
            
            if filename.endswith('.md'):
                filepath = Path(dirpath) / filename
                file_info = process_file(filepath)
                if file_info:
                    semester_files_found.append(file_info)
    
    generate_index_file(semester_files_found)

if __name__ == "__main__":
    main()