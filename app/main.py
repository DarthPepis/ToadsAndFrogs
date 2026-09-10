import tkinter as tk
from gui import ToadsAndFrogsGUI

def main():
    root = tk.Tk()
    app = ToadsAndFrogsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
