THEME_COLOR = "#375362"

from tkinter import *

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        #Canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125,
                                                     text='Some question text',
                                                     font=('Arial', 20, 'italic'),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #label
        self.scoring = Label(font=('Arial',
                                   12, 'bold'),
                             text='Score: 0',
                             bg=THEME_COLOR,
                             fg='white', highlightthickness=0,
                             padx=20, pady=20)
        self.scoring.grid(row=0, column=1)

        #buttons
        img_true = PhotoImage(file='./images/true.png')
        img_false= PhotoImage(file='./images/false.png')
        self.true_button = Button(image=img_true, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=img_false, highlightthickness=0)
        self.false_button.grid(row=2, column=1)



        self.window.mainloop()