# File Organizer

This is a simple Python script that automatically organizes files into different folders based on their file type. I built it as a small automation project to make it easier to keep a folder organized.

## Features

* Sorts files into folders for Images, Documents, Audio, Videos and Code
* Automatically creates the folders if they don't already exist
* Renames files if a file with the same name already exists
* Has a dry-run option to see what would be moved before actually moving anything
* Keeps a log of files that have been moved
* Can be set up to run automatically using Windows Task Scheduler

## Built With

* Python
* os
* shutil
* argparse
* logging

## How to Use

Run the script and provide the folder you want to organize. You can also use the dry-run option if you want to see what the script will do first.

## Project Structure

* `organizer.py` - main Python script
* `organizer.log` - log of moved files
* `test-folder/` - folder used for testing

## Future Improvements

I would like to add support for more file types and possibly create a simple graphical interface for the program.
