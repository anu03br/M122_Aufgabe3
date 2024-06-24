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
import argparse
import os
from PIL import Image, ImageStat
from image_comparison import compare_images


def main(dry_run: bool):

    # abfrage des filepaths für die Bilder
    folder_path = input("bitte geben Sie den Pfad zum Bildordner an\n")

    # funktionsaufruf image_comparison.compare_images
    duplicate_files = compare_images(folder_path)

    if dry_run:
        print(f"duplicate files:\n{duplicate_files}")
        print("Das war nur ein testlauf. Die Bilder wurden nicht gelöscht")
        
    else:
        print(f"duplicate files:\n{duplicate_files}")
        print("dry_run ist false.\nDie Bildduplikate werden gelöscht")
        

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


# original function with dry_run insteal of opposite full_run
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#         "--dry-run",
#         "-d",
#         default=True,
#         action="store_true",
#         help="A dry run shows the duplicates but does not delete anything",
#     )

#     args = parser.parse_args()

#     main(dry_run=args.dry_run)