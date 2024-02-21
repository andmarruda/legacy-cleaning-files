class files:
    def __init__(self, files):
        if files is None:
            self.files = []
            return

        self.files = files

    """
    Get the files in this object and iterate over them
    """
    def __iter__(self):
        for file in self.files:
            yield file

    """
    Get the file in the index
    """
    def __getitem__(self, index):
        return self.files[index]

    """
    Get the length of the files
    """
    def __len__(self):
        return len(self.files)

    """
    Get the files in this object
    """
    def __str__(self):
        return str(self.files)

    """
    Add a file to the list
    """
    def add(self, file):
        self.files.append(file)

    """
    Remove a file from the list
    """
    def remove(self, file):
        self.files.remove(file)

    """
    Clear the list
    """
    def clear(self):
        self.files.clear()