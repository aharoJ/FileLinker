# import os
# import urllib.parse

# # Get a list of all the files in the 'z' directory
# image_paths = [f for f in os.listdir('z') if os.path.isfile(os.path.join('z', f))]

# # Open the Markdown file in append mode
# with open('Main.md', 'a') as f:
#   # Iterate over the list of file paths and write an image tag for each path to the file
#   for path in image_paths:
#     # Encode the file path using the quote() function
#     encoded_path = urllib.parse.quote(path)
#     f.write('![](z/%s)' % encoded_path)
#     f.write('\n')  # Add a newline character
#   # The file is automatically closed when the block ends



#---------------------------------------------------------------

# import os
# import re
# import urllib.parse

# # Read the contents of the Markdown file into a string
# with open('Main.md', 'r') as f:
#   contents = f.read()

# # Find all the image tags in the string using a regular expression
# image_tags = re.findall(r'!\[\]\((.+?)\)', contents)

# # Iterate over the list of image tags and modify the file paths to include the 'z' directory
# for i, tag in enumerate(image_tags):
#   file_path = tag.split('/')[-1]  # Get the file path from the tag
#   encoded_path = urllib.parse.quote(file_path)  # Encode the file path
#   new_tag = '![](z/%s)' % encoded_path  # Create the new image tag
#   contents = contents.replace(tag, new_tag)  # Replace the old image tag with the new one

# # Write the modified string back to the Markdown file
# with open('Main.md', 'w') as f:
#   f.write(contents)


#---------------------------------------------------------------

# import os
# import re
# import urllib.parse

# # Read the contents of the Markdown file into a string
# with open('Main.md', 'r') as f:
#   contents = f.read()

# # Find all the image tags in the string that do not include the 'z' directory using a regular expression
# image_tags = re.findall(r'!\[\]\(([^z/].+?)\)', contents)

# # Iterate over the list of image tags and modify the file paths to include the 'z' directory
# for i, tag in enumerate(image_tags):
#   file_path = tag.split('/')[-1]  # Get the file path from the tag
#   encoded_path = urllib.parse.quote(file_path)  # Encode the file path
#   new_tag = '![](z/%s)' % encoded_path  # Create the new image tag
#   contents = contents.replace(tag, new_tag)  # Replace the old image tag with the new one

# # Write the modified string back to the Markdown file
# with open('Main.md', 'w') as f:
#   f.write(contents)



#---------------------------------------------------------------


# import re

# # Open the input file in read mode
# with open('obsidian.md', 'r') as file:
#     # Read the contents of the file into a string
#     contents = file.read()

# # Use a regular expression to find all instances of the pattern "![](file_name)"
# pattern = r'!\[\]\(([\w\d_.]+)\)'
# matches = re.findall(pattern, contents)

# # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
# for match in matches:
#     replacement = f'![](z/{match})'
#     contents = contents.replace(f'![]({match})', replacement)

# # Open the output file in write mode
# with open('output.md', 'w') as file:
#     # Write the modified contents to the output file
#     file.write(contents)



#---------------------------------------------------------------




# import re

# # Open the input file in read mode
# with open('obsidian.md', 'r') as file:
#     # Read the contents of the file into a string
#     contents = file.read()

# # Use a regular expression to find all instances of the pattern "![](file_name)"
# pattern = r'!\[\]\(([\w\d_.]+)\)'
# matches = re.findall(pattern, contents)

# # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
# for match in matches:
#     replacement = f'![](z/{match})'
#     contents = contents.replace(f'![]({match})', replacement)

# # Open the input file in write mode
# with open('obsidian.md', 'w') as file:
#     # Write the modified contents back to the input file
#     file.write(contents)


#---------------------------------------------------------------





# import re

# # Ask the user for the file name
# file_name = input("Enter the file name: ")

# # Open the input file in read mode
# with open(file_name, 'r') as file:
#     # Read the contents of the file into a string
#     contents = file.read()

# # Use a regular expression to find all instances of the pattern "![](file_name)"
# pattern = r'!\[\]\(([\w\d_.]+)\)'
# matches = re.findall(pattern, contents)

# # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
# for match in matches:
#     replacement = f'![](z/{match})'
#     contents = contents.replace(f'![]({match})', replacement)

# # Open the input file in write mode
# with open(file_name, 'w') as file:
#     # Write the modified contents back to the input file
#     file.write(contents)




#---------------------------------------------------------------


# import re
# import os

# # Get a list of all the .md files in the current directory
# file_names = [f for f in os.listdir('.') if f.endswith('.md')]

# # Loop through the list of file names
# for file_name in file_names:
#     # Open the input file in read mode
#     with open(file_name, 'r') as file:
#         # Read the contents of the file into a string
#         contents = file.read()

#     # Use a regular expression to find all instances of the pattern "![](file_name)"
#     pattern = r'!\[\]\(([\w\d_.]+)\)'
#     matches = re.findall(pattern, contents)

#     # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#     for match in matches:
#         replacement = f'![](z/{match})'
#         contents = contents.replace(f'![]({match})', replacement)

#     # Open the input file in write mode
#     with open(file_name, 'w') as file:
#         # Write the modified contents back to the input file
#         file.write(contents)


#---------------------------------------------------------------



# import re
# import os

# # Set the root of the workspace
# workspace_root = '/path/to/workspace'

# # Recursively search for .md files in all subdirectories
# for root, dirs, files in os.walk(workspace_root):
#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_name)"
#             pattern = r'!\[\]\(([\w\d_.]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 replacement = f'![](z/{match})'
#                 contents = contents.replace(f'![]({match})', replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)



#---------------------------------------------------------------







# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Recursively search for .md files in all subdirectories
# for root, dirs, files in os.walk(workspace_root):
#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_name)"
#             pattern = r'!\[\]\(([\w\d_.]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 replacement = f'![](z/{match})'
#                 contents = contents.replace(f'![]({match})', replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)





import re
import os

# Set the root of the workspace
workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# Recursively search for .md files in all subdirectories
for root, dirs, files in os.walk(workspace_root):
    for file_name in files:
        if file_name.endswith('.md'):
            # Construct the full path to the file
            file_path = os.path.join(root, file_name)

            # Open the input file in read mode
            with open(file_path, 'r') as file:
                # Read the contents of the file into a string
                contents = file.read()

            # Use a regular expression to find all instances of the pattern "![](file_name)"
            pattern = r'!\[\]\(([\w\d_./]+)\)'
            matches = re.findall(pattern, contents)
            print(f"Found {len(matches)} matches in {file_name}: {matches}")

            # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
            for match in matches:
                replacement = f'![](/Users/aharo/programming/python/linkFixer_workspace/z/{match})'
                contents = contents.replace(f'
