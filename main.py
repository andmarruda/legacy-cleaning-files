from gui.dialog import dialog
import tkinter as tk
from lib.search import search

def main():
    root = tk.Tk()
    searchClass = search()
    dialog(root, searchClass)
    root.mainloop()

main()