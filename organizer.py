import os
import shutil
import logging
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'organizer.log')

logging.basicConfig(
    filename=LOG_FILE, 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s'
    )


parser = argparse.ArgumentParser(description="Organize files by category.")
parser.add_argument("folder", help="The folder to organize")
parser.add_argument(
    "--dry-run", 
    action="store_true", 
    help="Preview what would be moved without actually moving the files"
    )
args = parser.parse_args()

folder = args.folder
dry_run = args.dry_run

if not os.path.exists(folder):
    print("The specified folder does not exist.")
    exit()
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Code": [".py", ".js", ".html", ".css"],
}

def get_unique_filename(destination_folder, filename):
    name, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(destination_folder, new_filename)):
        new_filename = f"{name} ({counter}){extension}"
        counter += 1

    return new_filename

files = os.listdir(folder)

for file in files:
    name, extension = os.path.splitext(file)

    for category, extensions in file_categories.items():
        if extension.lower() in extensions:

            destination_folder = os.path.join(folder, category)

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            unique_filename = get_unique_filename(destination_folder, file)
               
            source = os.path.join(folder, file)
            destination = os.path.join(destination_folder, unique_filename)
                
            if dry_run:
                print(f"Dry run: {file} would be moved to {destination}")
            else:
                shutil.move(source, destination)
                print(f"Moved: {file} -> {category}/{unique_filename}")
                logging.info(f"Moved: {file} -> {category}/{unique_filename}")
