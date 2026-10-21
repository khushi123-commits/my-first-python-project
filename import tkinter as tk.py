import tkinter as tk
import random

questions = [
    ("Which language are we using?", ["Java", "Python", "C++", "HTML"], 1),
    ("What does CPU stand for?", ["Central Processing Unit",
     "Computer Power Unit", "Central Program Utility", "None"], 0),
    ("Which symbol starts a Python comment?", ["//", "/*", "#", "$"], 2),
    ("Which data type stores True or False?", ["String", "Integer",
     "Boolean", "List"], 2),
    ("Which structure stores multiple items?", ["List", "Float",
     "Boolean", "Character"], 0),
]

random.shuffle(questions)

BG = "#101326"
CYAN = "#54F6FF"
PINK = "#FF55B8"
WHITE = "#F5F5FF"

root = tk.Tk()
root.title("CYBER QUIZ ARENA")
root.geometry("600x500")
root.configure(bg=BG)
root.resizable(False, False)

index = 0
score = 0
answered = False

title = tk.Label(
    root, text="⚡ CYBER QUIZ ARENA ⚡",
    font=("Consolas", 22, "bold"),
    bg=BG, fg=CYAN
)
title.pack(pady=20)

progress = tk.Label(
    root, text="", font=("Arial", 11),
    bg=BG, fg=WHITE
)
progress.pack()

question_label = tk.Label(
    root, text="", wraplength=520,
    font=("Arial", 16, "bold"),
    bg=BG, fg=WHITE, pady=20
)
question_label.pack()

feedback = tk.Label(
    root, text="", font=("Arial", 12, "bold"),
    bg=BG, fg=CYAN
)
feedback.pack(pady=5)

buttons = []

def show_question():
    global answered
    answered = False
    feedback.config(text="")
    progress.config(
        text=f"QUESTION {index + 1} / {len(questions)}     SCORE: {score}"
    )
    question, options, correct = questions[index]
    question_label.config(text=question)

    for i, button in enumerate(buttons):
        button.config(
            text=options[i],
            state="normal",
            bg="#242944",
            fg=WHITE
        )

    next_button.config(text="NEXT ➜", state="disabled")

def check_answer(choice):
    global score, answered
    if answered:
        return

    answered = True
    correct = questions[index][2]

    if choice == correct:
        score += 1
        feedback.config(text="✓ CORRECT! NICE WORK", fg=CYAN)
        buttons[choice].config(bg="#176B58")
    else:
        feedback.config(
            text=f"✗ WRONG! Answer: {questions[index][1][correct]}",
            fg=PINK
        )
        buttons[choice].config(bg="#78334D")
        buttons[correct].config(bg="#176B58")

    for button in buttons:
        button.config(state="disabled")

    progress.config(
        text=f"QUESTION {index + 1} / {len(questions)}     SCORE: {score}"
    )
    next_button.config(state="normal")

def next_question():
    global index
    if not answered:
        return

    index += 1
    if index < len(questions):
        show_question()
    else:
        show_result()

def show_result():
    for widget in root.winfo_children():
        widget.pack_forget()

    tk.Label(
        root, text="🏆 QUIZ COMPLETED!",
        font=("Consolas", 23, "bold"),
        bg=BG, fg=CYAN
    ).pack(pady=55)

    tk.Label(
        root, text=f"YOUR SCORE: {score} / {len(questions)}",
        font=("Arial", 21, "bold"),
        bg=BG, fg=WHITE
    ).pack(pady=15)

    message = "Excellent!" if score >= 4 else "Keep practising!"
    tk.Label(
        root, text=message,
        font=("Arial", 16),
        bg=BG, fg=PINK
    ).pack(pady=10)

    tk.Button(
        root, text="PLAY AGAIN",
        command=restart,
        font=("Arial", 13, "bold"),
        bg=CYAN, fg=BG, padx=20, pady=10
    ).pack(pady=20)

def restart():
    global index, score
    random.shuffle(questions)
    index = 0
    score = 0

    for widget in root.winfo_children():
        widget.pack_forget()

    title.pack(pady=20)
    progress.pack()
    question_label.pack()
    feedback.pack(pady=5)
    for button in buttons:
        button.pack(fill="x", padx=70, pady=5)
    next_button.pack(pady=15)

    show_question()

for i in range(4):
    button = tk.Button(
        root, text="",
        font=("Arial", 12, "bold"),
        bg="#242944", fg=WHITE,
        activebackground=CYAN,
        activeforeground=BG,
        relief="flat", pady=8,
        command=lambda n=i: check_answer(n)
    )
    button.pack(fill="x", padx=70, pady=5)
    buttons.append(button)

next_button = tk.Button(
    root, text="NEXT ➜",
    font=("Arial", 12, "bold"),
    bg=CYAN, fg=BG,
    state="disabled",
    command=next_question
)
next_button.pack(pady=15)

show_question()
root.mainloop()