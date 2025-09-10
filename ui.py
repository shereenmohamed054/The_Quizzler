from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:   # tha name of the class should be written in a PascalCase

    def __init__(self, quiz_brain: QuizBrain):  # we must define the object datatype from class QuizBrain
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("The Quizzler")
        self.window.config(padx=30, pady=50, bg=THEME_COLOR)
        self.canvas = Canvas(height=350, width=400, bg="White")
        self.q_text = self.canvas.create_text(185,
                                              150,
                                              width=350,     # to wrap the text into the canvas
                                              text="",
                                              font=("Arial", 20, "bold"),
                                              fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text=f"The Score:0", fg="White", bg=THEME_COLOR, font=("Arial", 10, "italic"))
        self.score_label.grid(column=1, row=0)

        true_button_photo = PhotoImage(file="true.png")
        self.true_button = Button(image=true_button_photo, highlightthickness=0, command=self.is_ans_true)
        self.true_button.grid(column=0, row=2)

        false_button_photo = PhotoImage(file="false.png")
        self.false_button = Button(image=false_button_photo, highlightthickness=0, command=self.is_ans_false)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"The Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=question_text)
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")     # to disable the button
            self.false_button.config(state="disabled")

    def is_ans_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_ans_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green2")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red2")
            self.window.after(1000, self.get_next_question)


