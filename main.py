from tkinter import Tk

class MainWindow(TK):
    def __init__(self):
        self.title("My App")
        self.geometry("700x700");

if __name____ == "__main__":
    App = MainWindow()
    App.mainloop()