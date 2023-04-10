#Niall Whyte 101377899

import os
import shutil


def create_directory():
    directory_name = input("Enter the name of the directory you want to create: ")
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except Exception as e:
        print(f"Error: {e}")


def create_subdirectory():
    directory_name = input("Enter the name of the directory you want to create a subdirectory in: ")
    if not os.path.exists(directory_name):
        print(f"Error: Directory '{directory_name}' does not exist.")
        return
    subdirectory_name = input("Enter the name of the subdirectory you want to create: ")
    directory_path = os.path.join(os.getcwd(), directory_name)
    subdirectory_path = os.path.join(directory_path, subdirectory_name)
    try:
        os.mkdir(subdirectory_path)
        print(f"Subdirectory '{subdirectory_name}' created successfully in '{directory_name}'.")
    except FileExistsError:
        print(f"Subdirectory '{subdirectory_name}' already exists in '{directory_name}'.")
    except Exception as e:
        print(f"Error: {e}")


def copy_file():
    filename = input("Enter the name of the file you want to copy: ")
    source = os.path.abspath(filename)
    if not os.path.exists(source):
        print(f"Error: file '{filename}' does not exist.")
        return
    destination = input("Enter the destination directory path: ")
    if not os.path.exists(destination):
        print(f"Error: Directory '{destination}' does not exist.")
        return
    try:
        shutil.copy(source, destination)
        print(f"File '{filename}' copied to '{destination}' successfully.")
    except Exception as e:
        print(f"Error copying file: {e}")


def move_file():
    filename = input("Enter the name of the file you want to move: ")
    source = os.path.abspath(filename)
    if not os.path.exists(source):
        print(f"Error: file '{filename}' does not exist.")
        return
    destination = input("Enter the destination directory path: ")
    if not os.path.exists(destination):
        print(f"Error: directory '{destination}' does not exist.")
        return
    try:
        shutil.move(source, destination)
        print(f"File '{filename}' moved to '{destination}' successfully.")
    except Exception as e:
        print(f"Error moving file: {e}")


def sort_by_name_asc():
    path = "."
    # path = input("Enter the path to the directory: ")
    while not os.path.isdir(path):
        print("Directory not found.")
        path = input("Enter the path to the directory: ")
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    sorted_dirs = sorted(dirs)
    print("Sorted directories:")
    for d in sorted_dirs:
        print(d)


def sort_by_name_desc():
    path = "."
    # path = input("Enter the path to the directory: ")
    while not os.path.isdir(path):
        print("Directory not found.")
        path = input("Enter the path to the directory: ")
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    sorted_dirs = sorted(dirs, reverse=True)
    print("Sorted directories:")
    for d in sorted_dirs:
        print(d)


def sort_by_date_asc():
    path = "."
    while not os.path.isdir(path):
        print("Directory not found.")
        path = input("Enter the path to the directory: ")
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    sorted_dirs = sorted(dirs, key=lambda d: os.path.getmtime(os.path.join(path, d)))
    print("Sorted directories:")
    for d in sorted_dirs:
        print(d)


def sort_by_date_desc():
    path = "."
    while not os.path.isdir(path):
        print("Directory not found.")
        path = input("Enter the path to the directory: ")
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    sorted_dirs = sorted(dirs, key=lambda d: os.path.getmtime(os.path.join(path, d)), reverse=True)
    print("Sorted directories:")
    for d in sorted_dirs:
        print(d)


def menu():
    while True:
        print("Welcome to Niall's Super File Manager Application! Please choose an option from the following:")
        print("1. Create Directory or Subdirectory")
        print("2. Copy and Move Files")
        print("3. Sort Directories")
        print("4. View Directory Contents")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            make_dir_or_subdir()
        elif choice == "2":
            copy_and_move_files()
        elif choice == "3":
            sort_directories()
        elif choice == "4":
            view_directory_contents()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. You must enter a number between 1-5.")


def make_dir_or_subdir():
    while True:
        print("Creating Directory or Subdirectory...")
        print("Would you like to create a Directory or Subdirectory?")
        print("1. Create Directory")
        print("2. Create Subdirectory")
        print("3. Go Back")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            print("Creating Directory...")
            create_directory()
        elif choice == "2":
            print("Creating Subdirectory...")
            create_subdirectory()
        elif choice == "3":
            print("Going back...")
            break
        else:
            print("Invalid choice. You must enter a number between 1-3.")


def copy_and_move_files():
    while True:
        print("Copying and Moving Files...")
        print("Would you like to copy or move a file?")
        print("1. Copy File")
        print("2. Move File")
        print("3. Go Back")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            print("Copying File...")
            copy_file()
        elif choice == "2":
            print("Moving File...")
            move_file()
        elif choice == "3":
            print("Going back...")
            break
        else:
            print("Invalid choice. You must enter a number between 1-3.")


def sort_directories():
    while True:
        print("Sorting Directories...")
        print("Which sorting method would you like to use?")
        print("1. Sort by Name Ascending")
        print("2. Sort by Name Descending")
        print("3. Sort by Last Modified Date Ascending")
        print("4. Sort by Last Modified Date Descending")
        print("5. Go Back")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            print("Sorting by Name Ascending...")
            sort_by_name_asc()
        elif choice == "2":
            print("Sorting by Name Descending...")
            sort_by_name_desc()
        elif choice == "3":
            print("Sorting by Last Modified Date Ascending...")
            sort_by_date_asc()
        elif choice == "4":
            print("Sorting by Last Modified Date Descending...")
            sort_by_date_desc()
        elif choice == "5":
            print("Going back...")
            break
        else:
            print("Invalid choice. You must enter a number between 1-5.")


def view_directory_contents():
    print("Viewing Directory Contents...")
    while True:
        dir_name = input("Enter the name of a directory: ")
        if not os.path.isdir(dir_name):
            print("Invalid directory name. Please try again.")
        else:
            print(f"Files in {dir_name}:")
            for root, dirs, files in os.walk(dir_name):
                for filename in files:
                    print(os.path.join(root, filename))
                for dirname in dirs:
                    print(os.path.join(root, dirname))
            break


menu()