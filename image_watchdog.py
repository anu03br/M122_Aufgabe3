#--------------------------------------------------------------------------------
# Autor: Andreas Nüssli
# Funktion des Skripts: Watchdog funktion welche den Zielordner auf veränderungen abhört und bei bedarf die image_compare funktion ausführt
# Datum: 25.06.2024
# Version: 0.5
# Changelog
# 25.06.24 V0.5 Skript Erstellt
#Quelle: https://www.geeksforgeeks.org/create-a-watchdog-in-python-to-look-for-filesystem-changes/
#--------------------------------------------------------------------------------

#import modules
import threading
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# define path variable for testing
path = "./images"

#define event handler
class FileChangeHandler (FileSystemEventHandler):
    def on_modified(self,event):
        # print something for testing
        print(f'File modified: {event.src_path}')
    def on_created(self,event):
        # print something for testing
        print(f'File modified: {event.src_path}')

# function to start observer
def start_observer(path):
    # initialize event handler
    event_handler = FileChangeHandler()
    # initialize observer
    observer = Observer()
    # schedule observer
    observer.schedule(event_handler, path, recursive=False)
    #start the observer
    observer.start()
    print("Observer started sucessfully")

    # function to stop the observer if /stop is typed
    def stop_observer():
        while True:
            command = input("Type /stop to stop observer\n")
            if command.strip().lower() == '/stop':
                observer.stop()
                observer.join()
                print("observer was stopped")
                break

    # Start a separate thread to listen for stop command
    stop_thread = threading.Thread(target=stop_observer)
    stop_thread.start()

    try:
        # run until canceled
        while observer.is_alive():
            # sleep for 10 seconds per iteration
            time.sleep(1)
    except KeyboardInterrupt:
        print("Observer was stopped")
        observer.stop()
        observer.join()

if __name__ == "__main__":
    start_observer(path)
