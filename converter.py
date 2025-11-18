import re
import os
import urllib.parse
from pathlib import Path
from collections import defaultdict

# --- Configuration ---
ROOT_DIRECTORY = '.' 
ASSET_FOLDER_NAME = 'assets'
INDEX_FILENAME = 'index.md'

ASSET_EXTENSIONS = (
    'png', 'jpg', 'jpeg', 'gif', 'svg', 'webp', 'pdf', 'mp4', 'mp3',
    'zip', 'txt', 'csv', 'xls', 'xlsx', 'doc', 'docx'
)

# --- Regex Patterns ---

# 1. Asset Links: ![[image.png]]
ASSET_PATTERN = re.compile(
    r'(!?)\[\[(.*?\.(?:' + '|'.join(ASSET_EXTENSIONS) + r'))\]\]',
    re.IGNORECASE
)

# 2. Standard Note Links: [[Note Title]]
NOTE_PATTERN = re.compile(r'\[\[(.*?)\]\]')

# 3. Quotes: #+BEGIN_QUOTE ... #+END_QUOTE
QUOTE_PATTERN = re.compile(r'#\+BEGIN_QUOTE\s*(.*?)\s*#\+END_QUOTE', re.DOTALL | re.IGNORECASE)

# 4. Tags (UPDATED): Matches "tags:: value", "- tags:: value", or "   tags:: value"
# We allow optional whitespace and optional dashes/bullets at the start of the line.
TAGS_PATTERN = re.compile(r'^\s*-?\s*tags::\s*(.*)', re.MULTILINE | re.IGNORECASE)

# ---------------------

def convert_quotes_to_markdown(content):
    """Converts Logseq #+BEGIN_QUOTE to > markdown quotes."""
    def replacer(match):
        block_content = match.group(1)
        return '\n'.join(f'> {line}' for line in block_content.splitlines())
    return QUOTE_PATTERN.sub(replacer, content)

def extract_semester_tags(content):
    """
    Scans content for 'tags::' and returns a list of tags containing 'Semester'.
    Handles [[Semester 1]] and plain Semester 1.
    """
    found_tags = []
    
    # Find all matches of the tags property in the file
    matches = TAGS_PATTERN.findall(content)
    
    for tag_string in matches:
        # Split multiple tags by comma
        raw_tags = [t.strip() for t in tag_string.split(',')]
        
        for t in raw_tags:
            # Remove [[ and ]] if they exist
            clean_t = t.replace('[[', '').replace(']]', '')
            
            if 'semester' in clean_t.lower():
                found_tags.append(clean_t)
                
    return found_tags

def process_file(filepath: Path):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"ERROR reading {filepath}: {e}")
        return None

    original_content = content
    
    # --- Link Conversion Logic ---
    current_dir = os.path.dirname(filepath)
    relative_path_to_root = os.path.relpath(ROOT_DIRECTORY, current_dir)
    relative_path_to_assets = Path(relative_path_to_root) / ASSET_FOLDER_NAME

    def asset_link_replacer(match):
        is_embedded = match.group(1)
        asset_filename = match.group(2)
        encoded_filename = urllib.parse.quote(asset_filename)
        full_asset_path = Path(relative_path_to_assets) / encoded_filename
        return f'![{asset_filename}]({full_asset_path})' if is_embedded == '!' else f'[{asset_filename}]({full_asset_path})'
            
    def note_link_replacer(match):
        note_title = match.group(1)
        filename = urllib.parse.quote(note_title)
        return f'[{note_title}]({filename}.md)'

    content = ASSET_PATTERN.sub(asset_link_replacer, content)
    content = NOTE_PATTERN.sub(note_link_replacer, content)
    content = convert_quotes_to_markdown(content)

    # Write changes if needed
    if content != original_content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            # print(f"Modified: {filepath.name}") 
        except Exception as e:
            print(f"ERROR writing {filepath}: {e}")

    # --- Index Extraction ---
    semester_tags = extract_semester_tags(content)
    if semester_tags:
        # Debug print to confirm tags are being found
        print(f"Found tags in {filepath.name}: {semester_tags}")
        
        rel_path = os.path.relpath(filepath, ROOT_DIRECTORY)
        return {
            'title': filepath.stem,
            'path': rel_path,
            'tags': semester_tags
        }
    return None

def generate_index_file(semester_data):
    grouped_files = defaultdict(list)
    
    for entry in semester_data:
        for tag in entry['tags']:
            # Normalize tag (Title Case) so "semester 1" and "Semester 1" merge
            clean_tag = tag.title() 
            grouped_files[clean_tag].append(entry)

    # Custom sort to ensure "Semester 1, Semester 2, Semester 10" sort numerically if possible
    def semantic_sort_key(key):
        # Extracts numbers to sort "Semester 2" before "Semester 10"
        numbers = re.findall(r'\d+', key)
        if numbers:
            return int(numbers[0])
        return key

    sorted_tags = sorted(grouped_files.keys(), key=semantic_sort_key)

    lines = ["# Course Index by Semester", "", "Auto-generated index.", ""]

    for tag in sorted_tags:
        lines.append(f"## {tag}")
        files = sorted(grouped_files[tag], key=lambda x: x['title'])
        for file_info in files:
            encoded_path = urllib.parse.quote(file_info['path'])
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
        if '.git' in dirnames: dirnames.remove('.git')
        if 'assets' in dirnames: dirnames.remove('assets') # Skip scanning inside assets
            
        for filename in filenames:
            if filename == 'convert_folder_links.py' or filename == INDEX_FILENAME: 
                continue
            if filename.endswith('.md'):
                filepath = Path(dirpath) / filename
                file_info = process_file(filepath)
                if file_info:
                    semester_files_found.append(file_info)
    
    generate_index_file(semester_files_found)

if __name__ == "__main__":
    main()