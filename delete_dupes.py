import os

def delete_duplicates(folder_path, duplicate_files):
    # lösche alle files in duplicate files
    for file in duplicate_files:
        file_path = os.path.join(folder_path, file)
        try:
            os.remove(file_path)
            print(f"gelöschtes File: {file_path}")
        except Exception as e:
            print(f"beim löschen des files {file_path} ist ein Fehler aufgetreten: {e}")