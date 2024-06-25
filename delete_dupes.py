#--------------------------------------------------------------------------------
# Autor: Andreas Nüssli
# Funktion des Skripts: when called it deletes the files in duplicate_files 
# Datum: 25.06.2024
# Version: 0.5
# Changelog
# 25.06.24 V0.5 Skript Erstellt
#Quelle: LMS M122 Aufgabe 3
#--------------------------------------------------------------------------------

# import modules
import os

# delete all items in duplicate files when called (rdy_run trigger is in main)
def delete_duplicates(folder_path, duplicate_files):
    # lösche alle files in duplicate files
    for file in duplicate_files:
        file_path = os.path.join(folder_path, file)
        try:
            os.remove(file_path)
            print(f"gelöschtes File: {file_path}")
        except Exception as e:
            print(f"beim löschen des files {file_path} ist ein Fehler aufgetreten: {e}")