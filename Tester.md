

# Universal Markdown Linker

A Python script that recursively searches for Markdown files (files with the ".md" file extension) in a given directory and its subdirectories, and modifies the links to image attachments in those files.

## How it works

-   The script starts by setting the "workspace_root" variable to the current working directory, and then sets the "base_dir" variable to "." and the "attachment_dir" variable to "z".
-   It then uses the `os.walk` function to recursively search for .md files in all subdirectories
-   For each file it opens it in read mode and reads the contents into a string.
-   Then the script uses a regular expression to find all instances of the pattern `![](file_name)` in the contents of the file.
-   After that it iterates through the matches and replaces them with the desired pattern `![](z/file_name)` by adding the relative path to the attachment directory to the front of the file name.
-   Finally, it opens the file in write mode and writes the modified contents back to the input file.

## Requirements

-   Python 3

## Usage

Copy code

`python linker.py`

## Future plans

-   Progressively working on:
    -   Adding error handling to the script to handle cases where the input files are not found or are not in the expected format.
    -   Adding a command line argument parser to make it easy for the user to specify the input and output directories.
    -   Adding an option to backup the original files before modifying them. (Actively 👨‍💻)
    -   Adding a progress bar to show the user the progress of the script.
    -   Adding an option to recursively search for files only in specific subdirectories.
    -   Adding an option to only search for specific file types other than .md
    -   Adding an option to search for a different pattern other than `![](../z/file_name.png)` (in thoughts only ☁️)
    -   Adding an option to specify the new_path in the replacement, instead of calculating it in the script.
    -   Adding an option to dry run the script without making any changes to the files.
    -   Adding an option to check the number of changes made to the files.
    -   Adding CLI support (Actively 👨‍💻)

## Note

-   This is a prototype version and I am still working on it.

## Author

-   Solo dev, [Angel Haro](https://github.com/aharo24)



