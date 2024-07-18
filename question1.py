# Task 1
import os

def list_directory_contents(path):
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for subdir in dirnames:
                print("Subdirectory:" + subdir)
            for name in filenames:
                print("File: " + os.path.join(path, name))
    except PermissionError:
        print("You don't have permission to access this file/path!")
    except FileNotFoundError:
        print("This file doesn't exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

#change my_local_path to path to directory you want to use
my_local_path = "/users/sudea/OneDrive/Pictures"
list_directory_contents(my_local_path)
