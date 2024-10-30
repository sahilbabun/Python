# Write a python program to print the contents of a directory using the os module.

import os

def list_directory_contents(path='E:\Python'):
    try:
        # List all files and directories in the specified path
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory path you want to list (defaults to current directory)
directory_path = 'E:\Python'  # Replace with the path you want, e.g., 'C:/Users/YourUsername/Documents'
list_directory_contents(directory_path)


