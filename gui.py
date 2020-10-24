import tkinter as tk
import bgmodules.answer_handlers
import bgmodules.label_updates
import bgmodules.count_time

# Frame widget class of imported tkinter module.
class Boost_Game(tk.Frame):
    # Constructor of Frame widget class. init method inherits that class
    # and taking parameter master. Master represents the parent window.
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Initializing variables with initial values for
        # the RIGHT ANSWER, GENERAL SCORE, TIME COUNT FOR ONE ANSWER.
        self.current_answer = ''
        self.game_scores = 0
        self.counter = 0

        # Initializing variables for realtime random numbers changing every 3 seconds.
        self.rand_num_1 = 0
        self.rand_num_2 = 0
        self.rand_num_3 = 0
        self.rand_num_4 = 0

        # Initializing variables with initial values and then expecting random number values.
        # Basic Tk class and its subclasses called Label and Button
        # with own properties to render them on the window.
        self.lab1=tk.Label(self, text="Соответствует ли значение цвету текста?", font=("Arial", 10))
        self.lab1.grid(row=0, column=0, columnspan=2)
    
        # Master is the parent window of all the widgets: Labels and Buttons.
        self.lab2=tk.Label(self, text="Oчки: ", width=10, font=("Arial", 10), anchor='w', justify='left')
        self.lab2.place(x = 20, y = 45)
        
        self.lab3=tk.Label(self, text="Значение\n\u2193", font=("Arial", 20), width=7)
        self.lab3.grid(row=1, column=0, columnspan=2)

        self.lab4=tk.Label(self, text="Время: ", width=10, font=("Arial", 10), anchor='w', justify='left')
        self.lab4.place(x = 280, y = 45)
        
        self.lab5=tk.Label(self, text='', bg='white', width=10, height=2, borderwidth=2, relief='groove', font=("Arial", 30))
        self.lab5.grid(row=2, column=0, columnspan=2)

        self.lab6=tk.Label(self, text='', bg='white', width=10, height=2, borderwidth=2, relief='groove', font=("Arial", 30))
        self.lab6.grid(row=3, column=0, columnspan=2)
        
        self.lab7=tk.Label(self, text="\u2191\nЦвет текста", font=("Arial", 20))
        self.lab7.grid(row=4, column=0, columnspan=2)

        self.lab8=tk.Label(self, text='', bg='white', width=10, height=2)
        self.lab8.grid(row=5, column=0, columnspan=2)

        # Creating buttons and binding to the functions from answer_handlers module.
        but1=tk.Button(self, command=lambda:bgmodules.answer_handlers.answer_handler_yes(self), text='ДА', width=20, height=5, font=("Arial", 10), relief='raised', bd=5)
        but1.grid(row=6, column=0, sticky='nsew')

        but2=tk.Button(self, command=lambda:bgmodules.answer_handlers.answer_handler_no(self), text='НЕТ', width=20, height=5, font=("Arial", 10), relief='raised', bd=5)
        but2.grid(row=6, column=1, sticky='nsew')

        # Updating labels from label_updates module.
        def run_updatelab1():
            self.lab5.after(0, bgmodules.label_updates.update_label_1(self))
            """Updating Label every 3 seconds."""
            self.lab5.after(3000, run_updatelab1)

        def run_updatelab2():
            self.lab5.after(0, bgmodules.label_updates.update_label_2(self))
            self.lab5.after(3000, run_updatelab2)

        def run_updatelab3():
            self.lab6.after(0, bgmodules.label_updates.update_label_3(self))
            self.lab6.after(3000, run_updatelab3)

        def run_updatelab4():
            self.lab6.after(0, bgmodules.label_updates.update_label_4(self))
            self.lab6.after(3000, run_updatelab4)

        def run_updatelab11():
            self.lab8.after(0, bgmodules.label_updates.update_label_1(self))
            self.lab8.after(3000, run_updatelab11)

        def run_updatelab22():
            self.lab8.after(0, bgmodules.label_updates.update_label_2(self))
            self.lab8.after(3000, run_updatelab22)

        def run_updatelab33():
            self.lab8.after(0, bgmodules.label_updates.update_label_3(self))
            self.lab8.after(3000, run_updatelab33)

        def run_updatelab44():
            self.lab8.after(0, bgmodules.label_updates.update_label_4(self))
            self.lab8.after(3000, run_updatelab44)

        # Updating labels by calling its methods.
        run_updatelab1()
        run_updatelab2()
        run_updatelab3()
        run_updatelab4()

        run_updatelab11()
        run_updatelab22()
        run_updatelab33()
        run_updatelab44()

        # Updating labels from count_time module.
        def run_updatelab555():
            self.lab4.after(0, bgmodules.count_time.count(self))
            self.lab4.after(1000, run_updatelab555)

        # Updating labels by calling its methods.
        run_updatelab555()
