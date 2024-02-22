from lib.store.files import files
from lib.store.filesInFolder import filesInFolder

class search:
    def __init__(self):
        self.filesIntented = files(None)
        self.filesFound = files(None)
        self.filesPretended = files(None)

    """
    Get the files found
    """
    def checkInsideFiles(self):
        for pretended in self.filesPretended:
            with open(pretended, 'r') as file:
                content = file.read()
                for fIntented in self.filesIntented:
                    filename = os.path.basename(fIntented)
                    dot_position = filename.rfind('.')
                    if filename in content or fIntented[:dot_position] in content:
                        self.filesFound.add(pretended)

    """
    Add intented files to the list
    """
    def addIntentedFile(self, file):
        self.filesIntented.add(file)

    """
    Get the files found
    """
    def getFilesFound(self):
        return self.filesFound

    """
    Get the files intented
    """
    def getFilesIntented(self):
        return self.filesIntented
    
    """
    Get the files pretended
    """
    def getFilesPretended(self):
        return self.filesPretended

    """
    Get files not founded
    """
    def getFilesNotFound(self):
        return self.filesIntented - self.filesFound

    """
    Set and search all files in folder
    """
    def setFilesInFolder(self, path):
        ffolder = filesInFolder(path)
        ffolder.find()
        self.filesPretended = ffolder.getFiles()