import tkinter as tk
from tkinter import filedialog
import os

class dialog:
    def __init__(self, root, search):
        self.search = search
        self.root = root
        self.root.title("Legacy Cleaning Files")
        self.root.resizable(False, False)
        self.root.geometry("400x200")

        introduction_label = tk.Label(root, text="Legacy Cleaning Files")
        introduction_label.pack()

        directory_button = tk.Button(root, text="Select directory", command=self.selectDirectory)
        directory_button.pack(pady=(30,0))

        self.directory_label = tk.Label(root, text="No directory selected")
        self.directory_label.pack()

        files_button = tk.Button(root, text="Select files intented", command=self.selectFiles)
        files_button.pack()

        self.files_label = tk.Label(root, text="No files selected")
        self.files_label.pack()

        powered_label = tk.Label(root, text="Powered by Anderson Arruda < andmarruda@gmail.com >")
        powered_label.pack(pady=(20,0))

    def selectDirectory(self):
        self.directory = filedialog.askdirectory()
        self.directory_label.config(text=self.directory)
        if self.directory != "":
            self.search.setFilesInFolder(self.directory)
    
    def selectFiles(self):
        self.files = filedialog.askopenfilenames()
        self.files_label.config(text="Selected")
        for file in self.files:
            self.search.addIntentedFile(file)