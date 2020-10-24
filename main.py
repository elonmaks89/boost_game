import tkinter as tk
import gui

# Importing main gui module with imported submodules.
def main():
    root = tk.Tk()
    root.geometry('350x488+400+100')
    root.title("Boost Game")
    root.resizable(width=False, height=False)
    gui.Boost_Game(root).pack()
    root.mainloop()

if __name__ == "__main__" :
    main()
    





    
