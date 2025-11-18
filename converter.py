import re
import os
import urllib.parse
from pathlib import Path
from collections import defaultdict

# --- Configuration ---
ROOT_DIRECTORY = '.' 
ASSET_FOLDER_NAME = 'assets'
INDEX_FILENAME = 'index.md'

# Files to ignore during processing
IGNORE_FILES = ['convert_folder_links.py', INDEX_FILENAME, 'converter.py', '_config.yml']
# Directories to ignore
IGNORE_DIRS = ['.git', 'assets']

ASSET_EXTENSIONS = (
    'png', 'jpg', 'jpeg', 'gif', 'svg', 'webp', 'pdf', 'mp4', 'mp3',
    'zip', 'txt', 'csv', 'xls', 'xlsx', 'doc', 'docx'
)

# --- Regex Patterns ---
ASSET_PATTERN = re.compile(r'(!?)\[\[(.*?\.(?:' + '|'.join(ASSET_EXTENSIONS) + r'))\]\]', re.IGNORECASE)
NOTE_PATTERN = re.compile(r'\[\[(.*?)\]\]')
QUOTE_PATTERN = re.compile(r'#\+BEGIN_QUOTE\s*(.*?)\s*#\+END_QUOTE', re.DOTALL | re.IGNORECASE)

# Pattern to find "tags:: value" lines (with optional bullets/indentation)
TAGS_LINE_PATTERN = re.compile(r'^\s*[-*]?\s*tags::\s*(.*)$', re.MULTILINE | re.IGNORECASE)
# Pattern to find junk Logseq properties (id::, logseq.x::, etc) to delete them
JUNK_PROPERTY_PATTERN = re.compile(r'^\s*[-*]?\s*(id|logseq\.[a-z0-9-]+|collapsed|icon)::.*$', re.MULTILINE | re.IGNORECASE)

def force_posix_path(path_obj):
    """Forces a path to use forward slashes (/) even on Windows."""
    return str(path_obj).replace(os.sep, '/')

def encode_path(path_str):
    """URL-encodes the path but KEEPS the forward slashes safe."""
    clean_path = path_str.replace('\\', '/')
    return urllib.parse.quote(clean_path, safe='/')

def convert_quotes_to_markdown(content):
    def replacer(match):
        block_content = match.group(1)
        return '\n'.join(f'> {line}' for line in block_content.splitlines())
    return QUOTE_PATTERN.sub(replacer, content)

def process_frontmatter_and_clean(content, filename_stem):
    """
    1. Extracts tags.
    2. Removes tags:: and id:: lines from the body.
    3. Generates a clean YAML Front Matter block at the top.
    """
    tags = []
    
    # 1. Extract tags
    matches = TAGS_LINE_PATTERN.findall(content)
    for tag_string in matches:
        raw_tags = [t.strip() for t in tag_string.split(',')]
        for t in raw_tags:
            clean_t = t.replace('[[', '').replace(']]', '')
            tags.append(clean_t)
            
    # 2. Remove the property lines from the content
    # Remove tags:: lines
    content = TAGS_LINE_PATTERN.sub('', content)
    # Remove id:: and logseq:: lines
    content = JUNK_PROPERTY_PATTERN.sub('', content)

    # 3. Clean up double blank lines created by removal
    content = re.sub(r'\n{3,}', '\n\n', content)

    # 4. Construct YAML Front Matter
    # We ensure 'title' is set, and 'tags' are listed if found
    yaml_block = "---\n"
    yaml_block += f"title: {filename_stem}\n"
    if tags:
        # Join tags with proper YAML list syntax if needed, or just comma separated
        # Simple comma separated string works for Jekyll usually, or list format
        # Let's use valid YAML list syntax
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
    
    # --- 1. Clean Properties & Generate Front Matter ---
    # We do this FIRST so we process the clean text for links later
    content, extracted_tags = process_frontmatter_and_clean(content, filepath.stem)

    # --- 2. Link Conversion ---
    current_dir = os.path.dirname(filepath)
    relative_path_to_root = os.path.relpath(ROOT_DIRECTORY, current_dir)
    relative_path_to_assets = Path(relative_path_to_root) / ASSET_FOLDER_NAME

    def asset_link_replacer(match):
        is_embedded = match.group(1)
        asset_filename = match.group(2)
        full_asset_path_obj = Path(relative_path_to_assets) / asset_filename
        full_asset_path_str = force_posix_path(full_asset_path_obj)
        encoded_path = encode_path(full_asset_path_str)
        return f'![{asset_filename}]({encoded_path})' if is_embedded == '!' else f'[{asset_filename}]({encoded_path})'
            
    def note_link_replacer(match):
        note_title = match.group(1)
        encoded_filename = encode_path(f"{note_title}.md")
        return f'[{note_title}]({encoded_filename})'

    content = ASSET_PATTERN.sub(asset_link_replacer, content)
    content = NOTE_PATTERN.sub(note_link_replacer, content)
    content = convert_quotes_to_markdown(content)

    # --- 3. Write Changes ---
    # We always write if we added frontmatter, even if links didn't change
    # But we check if content actually changed effectively (ignoring just simple re-runs)
    if content != original_content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"CLEANED & UPDATED: {filepath.name}") 
        except Exception as e:
            print(f"ERROR writing {filepath}: {e}")

    # --- 4. Return Info for Index ---
    # We return the tags we found during the cleanup phase
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
            encoded_path = encode_path(file_info['path'])
            lines.append(f"- [{file_info['title']}]({encoded_path})")
        lines.append("")

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