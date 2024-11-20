# prints all projects appearing in the .md files in /docs to terminal  
# run with: python list-projects.py  
import os  
import re  

# Function to extract tags from a markdown file  
def extract_tags_from_file(file_path):  
 
    with open(file_path, 'r') as file:  

        for line in file:

            if not line.strip().startswith('tags:'):  
                continue

            start_pos_of_tags = line.find('[') + 1
            end_pos_of_tags = line.find(']')

            tags_as_string = line[start_pos_of_tags:end_pos_of_tags]
            tags_as_string = tags_as_string.replace("'", "")
            tags_as_string = tags_as_string.replace('"', "")

            tags_as_list = tags_as_string.split(',')

            tags_as_list = [tag.strip() for tag in tags_as_list]

            return tags_as_list
    

# Get list of markdown files  
md_files = []  
md_files_absolute = []
for root, dirs, files in os.walk('docs/our_work'):  
    for file in files:  
        if file.endswith('.md') & (file not in ['Publications.md', 'tags.md','template-project.md']):  
            relative_path = os.path.relpath(os.path.join(root, file), 'docs/our_work')
            md_files.append(relative_path)  
            md_files_absolute.append(f'our_work/{relative_path}')

print(md_files)
print(md_files_absolute)