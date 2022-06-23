import os
import shutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



# Setting directories we want to give access to
source_dir = "/Users/lorenzodinapoli/Downloads"
dest_dir_pdf = "/Users/lorenzodinapoli/Desktop/pdf"
dest_dir_img = "/Users/lorenzodinapoli/Desktop/images&videos"


def makeUnique(path):
	"""
	Creating a unique name for the moved file
	"""
	pass


def move(dest, file, name):
	"""
	Checks that the file actually exists and moves it in the desired folder
	"""
	file_exists = os.path.exists(dest + "/" + name)
	if file_exists:
		#unique_name = makeUnique(name)
		os.rename(file, name)
	shutil.move(file, dest)


class MoveHandler(FileSystemEventHandler):
	"""
	Class that manages the move of the file from Downloads to 
	the desired folder.
	"""
	def on_modified(self, event):
		# Giving access to the files in Downloads directory
		with os.scandir(source_dir) as files:
			for file in files:
				name = file.name
				dest = source_dir
				# Directing files to destination
				if name.endswith(".pdf"): # Moving PDFs
					dest = dest_dir_pdf
					move(dest, file, name)
				elif name.endswith(".jpeg") or name.endswith(".png") or name.endswith(".jpg") or name.endswith(".mp4") or name.endswith(".mov"): # Moving images and videos
					dest = dest_dir_img
					move(dest, file, name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
    	observer.stop()
    observer.join()




