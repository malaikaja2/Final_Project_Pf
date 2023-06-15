from tkinter import *

levels = [
    {
        "questions": [
             "What is Python?",
             "Which built-in function is used to find the length of a string in Python?",
             "How do you access the last element of a list in Python?",
             "Which of the following is not a valid comparison operator in Python?",
             "Which of the following is a valid way to declare a variable in Python?",
             "Which data structure in Python is immutable?",
             "Which keyword is used to define a function in Python?",
             "Which operator is used to perform exponentiation in Python?",
             "What is the result of the expression: 9 % 2?",
             "What is the purpose of a loop in programming?"
        ],
        "options": [
             ["High-Level language", "Low-Level language", "Scripting language", "None of the above"],
             ["length()", "count()", "size()", "len()"],
             ["list[-1]", "list[0]", "list[-2]", "list[1]"],
             ["==", "!=", "<=", "><"],
             ["var1 = 10", "1_var = 10", "var_1 = 10", "var-1 = 10"],
             ["List", "Dictionary", "Set", "Tuple"],
             ["function", "def", "define", "fun"],
             ["*", "^", "**", "//"],
             ["0", "1", "2", "9"],
             ["To repeat a set of instructions a certain number of times.", "To store multiple values in a variable."]
        ],
        "answers": [
            "High-Level language",
            "len()",
            "list[-1]",
            "><",
            "var1 = 10",
            "Tuple",
            "def",
            "**",
            "1",
            "To repeat a set of instructions a certain number of times."
        ]
    },
    {
        "questions": [
            "Which of the following is used to handle errors and exceptions in Python?",
            "What does the pass statement do in Python?",
            "How do you remove an item from a set in Python?",
            "What is the purpose of the enumerate() function in Python?",
            "How do you open a file in Python for reading?",
            "How do you convert a string to uppercase in Python?",
            "Which of the following is used to sort a list in Python?",
            "How do you append an item to the end of a list in Python?",
            "How do you check the length of a list in Python?",
            "Which of the following statements about dictionaries in Python is correct?"
        ],
        "options": [
             ["try-except", "if-else", "for loop", "while loop"],
             ["It terminates the program execution.", "It raises an exception.", "It is used as a placeholder when no action is required.", "It prints a message to the console."],
             ["Using the `delete()` method", "Using the `remove()` method", "Using the `discard()` method", "Using the `pop()` method"],
             ["To iterate over a sequence and retrieve both the index and value", "To convert a string to uppercase", "To sort a list in ascending order", "To check if a value exists in a dictionary"],
             ["`open('file.txt', 'r')`", "`open('file.txt', 'w')`", "`open('file.txt', 'a')`", "`open('file.txt', 'x')`"],
             ["`str.upper()`", "`str.capitalize()`", "`str.lower()`", "`str.swapcase()`"],
             ["`list.sort()`", "`sorted(list)`", "`list.sort(reverse=True)`", "`sorted(list, reverse=True)`"],
             ["`list.append(item)`", "`list.insert(-1, item)`", "`list.extend(item)`", "`list.add(item)`"],
             ["`len(list)`", "`list.size()`", "`list.length()`", "`list.count()`"],
             ["Dictionaries are ordered collections of elements.", "Dictionaries allow duplicate keys.", "Dictionary keys must be of numeric data types.", "Dictionary values can be accessed using indices."]
        ],
        "answers": [
            "try-except",
            "It is used as a placeholder when no action is required.",
            "Using the `remove()` method",
            "To iterate over a sequence and retrieve both the index and value",
            "`open('file.txt', 'r')`",
            "`str.upper()`",
            "`list.sort()`",
            "`list.append(item)`",
            "`len(list)`",
            "Dictionaries are ordered collections of elements."
        ]
    }
]

score = 0
current_question = 0
selected_level = None

def select_level(level):
    global selected_level, current_question
    selected_level = level
    current_question = 0
    display_question()



def check_answer():
    global score, current_question
    selected_option = option_var.get()
    if selected_option == get_current_answers()[current_question]:
        score += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text="Incorrect!", fg="red")
    current_question += 1
    if current_question < len(get_current_questions()):
        display_question()
    else:
        display_result()

def display_question():
    question_text.set(get_current_questions()[current_question])
    question_number.set(f"Question {current_question+1} of {len(get_current_questions())}")
    for i in range(4):
        option_radios[i].config(text=get_current_options()[current_question][i], value=get_current_options()[current_question][i])
        option_radios[i].deselect()
def saveScore(score_message):
    try:
        with open("C:/Users/HT/AppData/Local/Programs/Python/Python311/quiz_result.txt", "a") as file:
            file.write(score_message + "\n")
    except Exception as e:
        mb.showerror("Error", f"An error occurred while saving the score:\n{str(e)}")


def display_result():
    result_window = Toplevel()
    result_window.title("Quiz Result")

    result_label = Label(result_window, text=f"You got {score} answers correct!", font=("Arial", 14))
    result_label.pack(pady=20)

    save_button = Button(result_window, text="Save Score", font=("Arial", 12), command=lambda: saveScore(f"Score: {score}"))
    save_button.pack(pady=10)

    result_button = Button(result_window, text="Close", font=("Arial", 12), command=result_window.destroy)
    result_button.pack(pady=10)
   

gui = Tk()
gui.title("Quiz Mania")
gui.geometry("1920x1860")
gui.configure(bg="light blue")

title_label = Label(gui, text="Quiz Mania: Battle of the PYTHON Brains", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

level_buttons = []
for i, level in enumerate(levels):
    level_button = Button(gui, text=f"Level {i+1}", font=("Arial", 12), command=lambda level=i: select_level(level))
    level_button.pack(pady=5)
    level_buttons.append(level_button)

question_number = StringVar()
question_number_label = Label(gui, textvariable=question_number, font=("Arial", 12))
question_number_label.pack(pady=10)

question_text = StringVar()
question_label = Label(gui, textvariable=question_text, font=("Arial", 14), wraplength=380)
question_label.pack(pady=20)

option_var = StringVar()

option_radios = []
for i in range(4):
    option_radio = Radiobutton(gui, text="", variable=option_var, value="", font=("Arial", 12))
    option_radio.pack(pady=5)
    option_radios.append(option_radio)

feedback_label = Label(gui, text="", font=("Arial", 12), fg="red")
feedback_label.pack(pady=10)

submit_button = Button(gui, text="Submit", font=("Arial", 12), command=check_answer)
submit_button.pack(pady=10)

def get_current_questions():
    return levels[selected_level]["questions"]

def get_current_options():
    return levels[selected_level]["options"]

def get_current_answers():
    return levels[selected_level]["answers"]

gui.mainloop()
