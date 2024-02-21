import files from lib.store.files
import filesInFolder from lib.store.filesInFolder

class search:
    def __init__(self, path):
        self.filesIntented = files(None)
        self.filesFound = files(None)
        filesInFolder = filesInFolder(path)
        self.filesPretended = filesInFolder.getFiles()

    """
    Get the files found
    """
    def checkInsideFiles(self):
        for pretended in self.filesPretended:
            with open(pretended, 'r') as file:
                content = file.read()
                for filesIntented in self.filesIntented:
                    if filesIntented in content:
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