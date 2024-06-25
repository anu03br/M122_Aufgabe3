# file_listener.py

import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from image_comparison import compare_images

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, folder_path, dry_run):
        self.folder_path = folder_path
        self.dry_run = dry_run

    def on_any_event(self, event):
        if event.is_directory:
            return None
        else:
            print(f"File changed: {event.src_path}")
            x = compare_images(self.folder_path)
            #return something to main wich can be used as a trigger for compare_images
            compare_again = 1
            return compare_again
            # compare_images(self.folder_path)


def start_listener(folder_path, dry_run):
    event_handler = FileChangeHandler(folder_path, dry_run)
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
                break
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
