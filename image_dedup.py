#--------------------------------------------------------------------------------
# Autor: Andreas Nüssli
# Funktion des Skripts: Hauptfunktion wurde bereitgestellt, nimmt user input (folder_path, dry_run) und ruft funktion compare_images auf welche liste mit duplicates zurückgibt
# Datum: 24.06.2024
# Version: 1.0
# Changelog
# 24.06.24 V0.5 Skript Erstellt
# 24.06.24 V0.6 Skript läuf fehlerlos, dry-run invertiert: "-f is full_run wich sets dry-run parameter to false (true by default)"
# 25.06.24 V1.0 Unterfunktionen ausgelagert, listener integriert und bugfixes
#Quelle: LMS M122 Aufgabe 3
# Issues: 
# wrong filepath input is not caught -- fixed
# on file delete watcher triggers but gives error because image no longer exists -- fixedd
#duplicate files is output twice -- fixed
#--------------------------------------------------------------------------------
#  can use pathlib, os
# import modules
import argparse
import os
from PIL import Image, ImageStat
# import my image-comparison function 
from image_comparison import compare_images
# import listener
from file_listener import start_listener
# import delete function
from delete_dupes import delete_duplicates

# if listener detects a filechange it produces a callback to this wich calls compare_images 
def files_changed(compare_again, folder_path):
    if compare_again == 1:
        compare_images(folder_path)


def main(full_run: bool):

    while True:
        # abfrage des filepaths für die Bilder
        folder_path = input("bitte geben Sie den Pfad zum Bildordner an\n")
        # check if provided path
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            break
        else:
            print("Ungültiger Pfad\n")

    # funktionsaufruf image_comparison.compare_images
    duplicate_files = compare_images(folder_path)

    # Define the callback function with parameters
    def callback(compare_again):
        files_changed(compare_again, folder_path)


    if full_run:
        delete_duplicates(folder_path, duplicate_files)

    # at the end Start the file listener
    start_listener(folder_path, callback)
    
        
# reversed parameterm -f is full_run wich sets dry-run parameter to false (true by default)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--full-run",
        "-f",
        default=False,          # Default to full_run
        action="store_true",  # Set to False if flag is present
        dest="full_run",        # Use 'dry_run' as the destination variable
        help="Execute with full functionality, disabling the dry run mode.",
    )

    args = parser.parse_args()

    main(full_run=args.full_run)
