from lib.store.files import files
import os

class filesInFolder:
    def __init__(self, path):
        self.files = files(None)
        self.path = path
        self.find()

    """
    Find recusively all files in the folder and inside of other folders
    """
    def find(self, path=None):
        path = path if path is not None else self.path

        for file in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, file)):
                self.files.add(file)
            if(os.path.isdir(os.path.join(self.path, file))):
                self.find(os.path.join(self.path, file))

    """
    Get the files found
    """
    def getFiles(self):
        return self.files

    """
    Return initial file path
    """
    def __str__(self):
        return self.path