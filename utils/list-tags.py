# prints all tags appearing in the .md files in /docs to terminal  
# run with: python list-tags.py  
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
for root, dirs, files in os.walk('docs'):  
    for file in files:  
        if file.endswith('.md'):  
            md_files.append(os.path.join(root, file))  

# Extract tags from each markdown file  
all_tags = []  
for file_path in md_files:  
    tags = extract_tags_from_file(file_path)  
    if tags:
        all_tags = all_tags + tags

# Remove duplicates and sort tags  
sorted_unique_tags = sorted(set(all_tags))  

# Print sorted tags list  
for tag in sorted_unique_tags:  
    print(tag) 