# prints all projects appearing in the .md files in /docs to terminal  
# run with: python list-projects.py  
import os  

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# Get list of markdown files  
md_files = []  
md_files_absolute = []
for root, dirs, files in os.walk(os.path.join(PROJECT_ROOT, 'docs', 'our_work')):  
    for file in files:  
        if file.endswith('.md') and file not in ['Publications.md', 'tags.md', 'template-project.md', 'index.md']:  
            relative_path = os.path.relpath(os.path.join(root, file), os.path.join(PROJECT_ROOT, 'docs', 'our_work'))
            md_files.append(relative_path)  
            md_files_absolute.append(f'our_work/{relative_path}')

print(md_files)
print(md_files_absolute)