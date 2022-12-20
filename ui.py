from tkinter import *


THEME_COLOR = "#375362"
# true_image = PhotoImage(file="images/true.png")
# false_image = PhotoImage(file="images/false.png")


class QuizInterface():
    def __init__(self):
        self.updates_score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.qsn = self.canvas.create_text(150, 125, width=250,
                                           text="This is your question looooong question "
                                                "very long question to update the fill", font=("Arial", 20, "italic"))
        # How to use text wrap in canvas create text write in documentation
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=40)
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, bd=0, pady=20, padx=20)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.false_image, highlightthickness=0, bd=0, pady=20, padx=20)
        self.false_button.grid(column=1, row=2)
        self.score_label = Label(text=f"Score: {self.updates_score}", padx=20, pady=20,
                                 bg=THEME_COLOR, fg="white", font=("Arial", 10))
        self.score_label.grid(column=1, row=0)
        # self.canvas.c

        self.window.mainloop()

    def update_score(self, score):
        self.updates_score = score

    # def update_question(self):



