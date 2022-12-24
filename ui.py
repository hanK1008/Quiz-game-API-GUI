from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface: 
    def __init__(self, quiz_class : QuizBrain):
        # defining data type of the quiz_class so we can see and IDE will suggest all the methods
        self.quiz = quiz_class
        self.window = Tk()
        self.window.title("QuizTion")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.qsn = self.canvas.create_text(150, 125,
                                           width=280,
                                           text="Placeholder",
                                           font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # You can use variable without ""self"" if you don't want to access the variable in future
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bd=0, command=self.true_user_choice)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_image, highlightthickness=0, bd=0, command= self.false_user_choice)
        self.false_button.grid(column=1, row=2)
        self.score_label = Label(text="Score: 0",
                                 bg=THEME_COLOR, fg="white", font=("Arial", 10))
        self.score_label.grid(column=1, row=0)

        # Updating  the ui with the current question and question number
        self.update_question()
        self.window.mainloop()

    def update_question(self):
        if self.quiz.still_has_questions():
            ui_question = self.quiz.next_question()
            self.canvas.itemconfig(self.qsn, text=ui_question)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            # self.true_button.config(state=DISABLED)
            self.canvas.itemconfig(self.qsn, text="Game Over")

    def true_user_choice(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_user_choice(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        self.window.after(1000, func=self.next_qsn)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

    def next_qsn(self):
        self.canvas.config(bg="white")
        self.update_question()








