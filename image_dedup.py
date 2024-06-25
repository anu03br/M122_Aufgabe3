#--------------------------------------------------------------------------------
# Autor: Andreas Nüssli
# Funktion des Skripts: Hauptfunktion wurde bereitgestellt, nimmt user input (folder_path, dry_run) und ruft funktion compare_images auf welche liste mit duplicates zurückgibt
# Datum: 24.06.2024
# Version: 0.5
# Changelog
# 24.06.24 V0.5 Skript Erstellt
# 24.06.24 V0.6 Skript läuf fehlerlos, dry-run invertiert: "-f is full_run wich sets dry-run parameter to false (true by default)"
#Quelle: LMS M122 Aufgabe 3
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


def main(dry_run: bool):

    # abfrage des filepaths für die Bilder
    folder_path = input("bitte geben Sie den Pfad zum Bildordner an\n")

    # funktionsaufruf image_comparison.compare_images
    duplicate_files = compare_images(folder_path, dry_run)

    if dry_run:
        delete_duplicates(folder_path, duplicate_files)

    # at the end Start the file listener
    start_listener(folder_path, dry_run)
    
        
# reversed parameterm -f is full_run wich sets dry-run parameter to false (true by default)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--full-run",
        "-f",
        default=True,          # Default to dry run
        action="store_false",  # Set to False if flag is present
        dest="dry_run",        # Use 'dry_run' as the destination variable
        help="Execute with full functionality, disabling the dry run mode.",
    )

    args = parser.parse_args()

    main(dry_run=args.dry_run)
