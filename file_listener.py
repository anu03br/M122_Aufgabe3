#--------------------------------------------------------------------------------
# Autor: Andreas Nüssli
# Funktion des Skripts: File listener to detect changes in folder_path. if change detected callback to main
# Datum: 25.06.2024
# Version: 0.5
# Changelog
# 25.06.24 V0.5 Skript Erstellt
#Quelle: LMS M122 Aufgabe 3
#--------------------------------------------------------------------------------

# import modules
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from image_comparison import compare_images


3# I don't really get this part but it's seems necessary
# initialize the handler I guess
class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, folder_path, callback):
        self.folder_path = folder_path
        self.callback = callback
    # if any filechange is detected (might change to added files only later)
    def on_any_event(self, event):
        if event.is_directory:
            return None
        else:
            print(f"File changed: {event.src_path}")
            #return something to main wich can be used as a trigger for compare_images
            compare_again = 1
            # if a filechange is detected callback to main
            self.callback(compare_again)
            #reset trigger variable (this is lazy)
            compare_again = 0 

# start listener. Can be stopped by typing '/stop' in terminal
def start_listener(folder_path, callback):
    event_handler = FileChangeHandler(folder_path,callback)
    observer = Observer()
    observer.schedule(event_handler, path=folder_path, recursive=False)
    observer.start()
    print("Listening for file changes. Type '/stop' to stop the listener.")

    try:
        while True:
            command = input()
            if command.strip().lower() == '/stop':
                print("Stopping listener...")
                observer.stop()
                observer.join()
                break
    # if something goes wrong end the observer threads
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

    observer.join()
