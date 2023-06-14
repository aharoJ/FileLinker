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
#             pattern = r'!\[\]\(([\w\d_./]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 replacement = f'![](/Users/aharo/programming/python/linkFixer_workspace/z/{match})'
#                 contents = contents.replace(f'








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
#             pattern = r'!\[\]\(([\w\d_./]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 replacement = f'![](/Users/aharo/programming/python/linkFixer_workspace/z/{match})'
#                 contents = contents.replace(f'![]({match})', replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)








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
#             pattern = r'!\[\]\(([\w\d_./]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 # Compute the relative path from the root of the workspace to the z directory
#                 z_path = os.path.relpath(os.path.join(workspace_root, 'z'), start=root)
#                 replacement = f'![]({z_path}/{match})'
#                 contents = contents.replace(f'![]({match})', replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)











# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Recursively search for .md files in the workspace root
# for root, dirs, files in os.walk(workspace_root):
#     # Skip subdirectories of the workspace root
#     if not os.path.samefile(os.path.abspath(root), os.path.abspath(workspace_root)):
#         continue

#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_name)"
#             pattern = r'!\[\]\(([\w\d_./]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in














# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Recursively search for .md files in the workspace root
# for root, dirs, files in os.walk(workspace_root):
#     # Skip subdirectories of the workspace root
#     if not os.path.samefile(os.path.abspath(root), os.path.abspath(workspace_root)):
#         continue

#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_name)"
#             pattern = r'!\[\]\(([\w\d_./]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 # Compute the relative path from the root of the workspace to the z directory
#                 z_path = os.path.relpath(os.path.join(workspace_root, 'z







# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Recursively search for .md files in the workspace root
# for root, dirs, files in os.walk(workspace_root):
#     # Skip subdirectories of the workspace root
#     if not os.path.samefile(os.path.abspath(root), os.path.abspath(workspace_root)):
#         continue

#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_name)"
#             pattern = r'!\[\]\(([\w\d_./]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 # Compute the relative path from the root of the workspace to the z directory
#                 z_path = os.path.relpath(os.path.join(workspace_root, 'z'), root)
#                 replacement = f'![]({os.path.join(z_path, match)})'
#                 contents = contents.replace(f'![]({match})', replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)








# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Recursively search for .md files in the workspace root
# for root, dirs, files in os.walk(workspace_root):
#     # Skip subdirectories of the workspace root
#     if not os.path.samefile(os.path.abspath(root), os.path.abspath(workspace_root)):
#         continue

#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_name)"
#             pattern = r'!\[\]\(([\w\d_./]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 # Compute the relative path from the root of the workspace to the z directory
#                 z_path = os.path.relpath(os.path.join(workspace_root, 'z'), root)
#                 replacement = f'![]({z_path}









# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Recursively search for .md files in the workspace root
# for root, dirs, files in os.walk(workspace_root):
#     # Skip subdirectories of the workspace root
#     if not os.path.samefile(os.path.abspath(root), os.path.abspath(workspace_root)):
#         continue

#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_name)"
#             pattern = r'!\[\]\(([\w\d_./]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 # Compute the relative path from the root of the workspace to the z directory
#                 z_path = os.path.relpath(os.path.join(workspace_root, 'z'), root)
#                 replacement = '![](' + z_path + '/' + match + ')'
#                 contents = contents.replace(f'![]({match})', replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)













# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Recursively search for .md files in the workspace root
# for root, dirs, files in os.walk(workspace_root):
#     # Skip subdirectories of the workspace root
#     if not os.path.samefile(os.path.abspath(root), os.path.abspath(workspace_root)):
#         continue

#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_name)"
#             pattern = r'!\[\]\(([\w\d_./]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them








# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Recursively search for .md files in the workspace root
# for root, dirs, files in os.walk(workspace_root):
#     # Skip subdirectories of the workspace root
#     if not os.path.samefile(os.path.abspath(root), os.path.abspath(workspace_root)):
#         continue

#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_name)"
#             pattern = r'!\[\]\(([\w\d_./]+)\)'
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








# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Recursively search for .md files in the workspace root
# for root, dirs, files in os.walk(workspace_root):
#     # Skip subdirectories of the workspace root
#     if not os.path.samefile(os.path.abspath(root), os.path.abspath(workspace_root)):
#         continue

#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_name)"
#             pattern = r'!\[\]\((.+?)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 replacement = f'![](z/{match})'
#                 contents = contents.replace(f'![]( {match} )', replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)







# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Recursively search for .md files in the workspace root
# for root, dirs, files in os.walk(workspace_root):
#     # Skip subdirectories of the workspace root
#     if not os.path.samefile(os.path.abspath(root), os.path.abspath(workspace_root)):
#         continue

#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_name)"
#             pattern = r'!\[\]\((.+?)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 replacement = f'![](z/{match})'
#                 contents = contents.replace(f'![]( {match} )', replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)








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
#             pattern = r'!\[\]\((.+?)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 replacement = f'![](z/{match})'
#                 contents = contents.replace(f'![]( {match} )', replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)






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
#             pattern = r'!\[\]\(([^)]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 # Construct the replacement string
#                 z_path = os.path.relpath(os.path.join(workspace_root, 'z'), root)
#                 replacement = f'![](z/{match})'
#                 # Replace the matched string with the replacement string
#                 contents = contents.replace(match, replacement)

#             # Open the input file in write mode
#             with open(file_path, '



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
#             pattern = r'!\[\]\(([^)]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 # Construct the replacement string
#                 z_path = os.path.relpath(os.path.join(workspace_root, 'z'), root)
#                 replacement = f'![](z/{match})'
#                 # Replace the matched string with the replacement string
#                 contents = contents.replace(match, replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)


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
#             pattern = r'!\[\]\(([^)]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
#             for match in matches:
#                 # Construct the replacement string
#                 z_path = os.path.relpath(os.path.join(workspace_root, 'z'), root)
#                 replacement = f'![]({z_path}/{match})'
#                 # Replace the matched string with the replacement string
#                 contents = contents.replace(match, replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)




# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Set the path to the z directory
# z_dir = os.path.join(workspace_root, 'z')

# # Recursively search for .md files in the root directory
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
#             pattern = r'!\[\]\(([^)]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](../z/file_name)"
#             for match in matches:
#                 # Check if the file name is located in the z directory
#                 if os.path.exists(os.path.join(z_dir, match)):
#                     # Construct the replacement string
#                     replacement = f'![](../z/{match})'
#                     # Replace the matched string with the replacement string
#                     contents = contents.replace(match, replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)



# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Set the path to the z directory
# z_dir = os.path.join(workspace_root, 'z')

# # Recursively search for .md files in the root directory
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
#             pattern = r'!\[\]\(([^/]+)\)'
#             matches = re.findall(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](../z/file_name)"
#             for match in matches:
#                 # Check if the file name is located in the z directory
#                 if os.path.exists(os.path.join(z_dir, match)):
#                     # Construct the replacement string
#                     replacement = f'![](../z/{match})'
#                     # Replace the matched string with the replacement string
#                     contents = contents.replace(match, replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)




# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Set the path to the z directory
# z_dir = os.path.join(workspace_root, 'z')

# # Recursively search for .md files in the root directory
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
#             pattern = r'!\[\]\(([^/]+)\)'
#             matches = re.finditer(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](../z/file_name)"
#             for match in matches:
#                 # Get the full matched string and the file name
#                 full_match = match.group()
#                 file_name = match.group(1)
#                 # Check if the file name is located in the z directory
#                 if os.path.exists(os.path.join(z_dir, file_name)):
#                     # Construct the replacement string
#                     replacement = f'![](../z/{file_name})'
#                     # Replace the matched string with the replacement string
#                     contents = contents.replace(full_match, replacement)

#             # Open the input file in write mode
#             with open(file





# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Set the path to the z directory
# z_dir = os.path.join(workspace_root, 'z')

# # Recursively search for .md files in the root directory
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
#             pattern = r'!\[\]\(([^/]+)\)'
#             matches = re.finditer(pattern, contents)
#             print(f"Found {len(matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](../z/file_name)"
#             for match in matches:
#                 # Get the full matched string and the file name
#                 full_match = match.group()
#                 file_name = match.group(1)
#                 # Check if the file name is located in the z directory
#                 if os.path.exists(os.path.join(z_dir, file_name)):
#                     # Construct the replacement string
#                     replacement = f'![](../z/{file_name})'
#                     # Replace the matched string with the replacement string
#                     contents = contents.replace(full_match, replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)



# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Set the path to the z directory
# z_dir = os.path.join(workspace_root, 'z')

# # Recursively search for .md files in the root directory
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
#             pattern = r'!\[\]\(([^/]+)\)'
#             matches = re.finditer(pattern, contents)
#             print(f"Found {sum(1 for _ in matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](../z/file_name)"
#             for match in matches:
#                 # Get the full matched string and the file name
#                 full_match = match.group()
#                 file_name = match.group(1)
#                 # Check if the file name is located in the z directory
#                 if os.path.exists(os.path.join(z_dir, file_name)):
#                     # Construct the replacement string
#                     replacement = f'![](../z/{file_name})'
#                     # Replace the matched string with the replacement string
#                     contents = contents.replace(full_match, replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)



# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Set the path to the z directory
# z_dir = os.path.join(workspace_root, 'z')

# # Recursively search for .md files in the root directory
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
#             pattern = r'!\[\]\(([^/]+)\)'
#             matches = re.finditer(pattern, contents)
#             print(f"Found {sum(1 for _ in matches)} matches in {file_name}: {matches}")

#             # Iterate through the matches and replace them with the desired pattern "![](../z/file_name)"
#             for match in matches:
#                 # Get the full matched string and the file name
#                 full_match = match.group()
#                 file_name = match.group(1)
#                 # Check if the file name is located in the z directory
#                 if os.path.exists(os.path.join(z_dir, file_name)):
#                     # Construct the replacement string
#                     replacement = f'![](../z/{file_name})'
#                     # Replace the matched string with the replacement string
#                     contents = contents.replace(full_match, replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)



# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Set the path to the z directory
# z_dir = os.path.join(workspace_root, 'z')

# # Recursively search for .md files in the root directory
# for root, dirs, files in os.walk(workspace_root):
#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_path)"
#             pattern = r'!\[\]\((.+)\)'
#             matches = re.finditer(pattern, contents)
#             print(f"Found {sum(1 for _ in matches)} matches in {file_name}")

#             # Iterate through the matches and replace them with the desired pattern "![](../z/file_name)"
#             for match in matches:
#                 # Get the full matched string and the file path
#                 full_match = match.group()
#                 file_path = match.group(1)
#                 # Extract the file name from the file path
#                 file_name = os.path.basename(file_path)
#                 # Check if the file name is located in the z directory
#                 if os.path.exists(os.path.join(z_dir, file_name)):
#                     # Construct the replacement string
#                     replacement = f'![](../z/{file_name})'
#                     # Replace the matched string with the replacement string
#                     contents = contents.replace(full_match, replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)



# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Set the path to the z directory
# z_dir = os.path.join(workspace_root, 'z')

# # Recursively search for .md files in the root directory
# for root, dirs, files in os.walk(workspace_root):
#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_path)"
#             pattern = r'!\[\]\((.+)\)'
#             matches = re.finditer(pattern, contents)
#             print(f"Found {sum(1 for _ in matches)} matches in {file_name}")

#             # Iterate through the matches and replace the file path in the matched string with the file name in the replacement string
#             for match in matches:
#                 # Get the file path
#                 file_path = match.group(1)
#                 # Extract the file name from the file path
#                 file_name = os.path.basename(file_path)
#                 # Check if the file name is located in the z directory
#                 if os.path.exists(os.path.join(z_dir, file_name)):
#                     # Replace the file path in the matched string with the file name in the replacement string
#                     contents = contents.replace(file_path, file_name)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)




# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Set the path to the z directory
# z_dir = os.path.join(workspace_root, 'z')

# # Recursively search for .md files in the root directory
# for root, dirs, files in os.walk(workspace_root):
#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_path)"
#             pattern = r'!\[\]\((.+)\)'
#             matches = re.finditer(pattern, contents)
#             print(f"Found {sum(1 for _ in matches)} matches in {file_name}")

#             # Iterate through the matches and replace them with the desired pattern "![](../z/file_name)"
#             for match in matches:
#                 # Get the full matched string and the file path
#                 full_match = match.group()
#                 file_path = match.group(1)
#                 # Extract the file name from the file path
#                 file_name = os.path.basename(file_path)
#                 # Check if the file name is located in the z directory
#                 if os.path.exists(os.path.join(z_dir, file_name)):
#                     # Construct the replacement string using the file name from the z directory
#                     replacement = f'![](../z/{os.path.basename(os.path.join(z_dir, file_name))})'
#                     # Replace the matched string with the replacement string
#                     contents = contents.replace(full_match, replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)


# import re
# import os

# # Set the root of the workspace
# workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# # Set the path to the z directory
# z_dir = os.path.join(workspace_root, 'z')

# # Recursively search for .md files in the root directory
# for root, dirs, files in os.walk(workspace_root):
#     for file_name in files:
#         if file_name.endswith('.md'):
#             # Construct the full path to the file
#             file_path = os.path.join(root, file_name)

#             # Open the input file in read mode
#             with open(file_path, 'r') as file:
#                 # Read the contents of the file into a string
#                 contents = file.read()

#             # Use a regular expression to find all instances of the pattern "![](file_path)"
#             pattern = r'!\[\]\((.+)\)'
#             matches = re.finditer(pattern, contents)
#             print(f"Found {sum(1 for _ in matches)} matches in {file_name}")

#             # Iterate through the matches and replace them with the desired pattern "![](../z/file_name)"
#             for match in matches:
#                 # Get the full matched string and the file path
#                 full_match = match.group()
#                 file_path = match.group(1)
#                 # Extract the file name from the file path
#                 file_name = os.path.basename(file_path)
#                 # Check if the file name is located in the z directory
#                 if os.path.exists(os.path.join(z_dir, file_name)):
#                     # Construct the replacement string using the file name from the matched string
#                     replacement = f'![](../z/{file_name})'
#                     # Replace the matched string with the replacement string
#                     contents = contents.replace(full_match, replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)





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
#                 replacement = f'![](../z/{match})'
#                 contents = contents.replace(f'![]({match})', replacement)

#             # Open the input file in write mode
#             with open(file_path, 'w') as file:
#                 # Write the modified contents back to the input file
#                 file.write(contents)








import re
import os

# Set the root of the workspace
workspace_root = '/Users/aharo/programming/python/linkFixer_workspace'

# Set the base directory and the attachment directory
base_dir = '.'
attachment_dir = 'z'


# Recursively search for .md files in all subdirectories
for root, dirs, files in os.walk(workspace_root):
    # Calculate the relative depth of the current directory
    depth = root[len(workspace_root):].count(os.sep)
    # Construct the relative path to the attachment directory
    attachment_path = os.sep.join(['..'] * depth + [attachment_dir])
    for file_name in files:
        if file_name.endswith('.md'):
            # Construct the full path to the file
            file_path = os.path.join(root, file_name)

            # Open the input file in read mode
            with open(file_path, 'r') as file:
                # Read the contents of the file into a string
                contents = file.read()

            # Use a regular expression to find all instances of the pattern "![](file_name)"
            pattern = r'!\[\]\(([\w\d_.]+)\)'
            matches = re.findall(pattern, contents)
            print(f"Found {len(matches)} matches in {file_name}: {matches}")

            # Iterate through the matches and replace them with the desired pattern "![](z/file_name)"
            for match in matches:
                # Calculate the new path by adding the relative path to the attachment directory
                # to the front of the file name
                new_path = os.path.join(attachment_path, match)
                replacement = f'![]({new_path})'
                contents = contents.replace(f'![]({match})', replacement)

            # Open the input file in write mode
            with open(file_path, 'w') as file:
                # Write the modified contents back to the input file
                file.write(contents)
