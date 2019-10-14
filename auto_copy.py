#pip install watchdog
from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler


import os
import json
import time

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = forder_to_track + "/" + filename
            os.rename(src,new_destination)

folder_to_track = "Users/zalcee/Desktop/newfolder"
folder_destination = "/Users/zalcee/Desktop/transfer"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
