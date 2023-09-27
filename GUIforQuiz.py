import tkinter as tk

# Initialize variables to store user's answers
user_answers = []
animal_points = {
    "Lion": 0,
    "Dolphin": 0,
    "Koala": 0,
    "Tiger": 0,
    "Shark": 0,
    "Eagle": 0,
    "Sloth": 0,
    "Fish": 0,
    "Bird": 0
}

# Questions and options
questions = [
    {
        "question": "What's your favorite color?",
        "options": {
            "Red": "Lion",
            "Blue": "Dolphin",
            "Green": "Koala"
        }
    },
    {
        "question": "What's your ideal vacation?",
        "options": {
            "Safari": "Tiger",
            "Beach": "Shark",
            "Mountains": "Eagle"
        }
    },
    {
        "question": "What's your favorite activity?",
        "options": {
            "Sleeping": "Sloth",
            "Swimming": "Fish",
            "Flying": "Bird"
        }
    },
    {
        "question": "What's your favorite food?",
        "options": {
            "Steak": "Lion",
            "Pizza": "Dolphin",
            "Salad": "Koala"
        }
    },
    {
        "question": "What's your favorite season?",
        "options": {
            "Summer": "Tiger",
            "Winter": "Shark",
            "Spring": "Eagle"
        }
    },
    {
        "question": "What's your favorite movie genre?",
        "options": {
            "Action": "Sloth",
            "Romance": "Fish",
            "Comedy": "Bird"
        }
    },
    {
        "question": "What's your preferred mode of transportation?",
        "options": {
            "Car": "Lion",
            "Bicycle": "Dolphin",
            "Plane": "Koala"
        }
    },
    {
        "question": "What's your favorite book genre?",
        "options": {
            "Mystery": "Tiger",
            "Fantasy": "Shark",
            "Biography": "Eagle"
        }
    },
    {
        "question": "What's your favorite music genre?",
        "options": {
            "Rock": "Sloth",
            "Pop": "Fish",
            "Classical": "Bird"
        }
    },
    {
        "question": "What's your favorite hobby?",
        "options": {
            "Painting": "Lion",
            "Cooking": "Dolphin",
            "Hiking": "Koala"
        }
    }
]


# Function to display the current question
def display_question():
    current_question = questions[current_question_index]
    question_label.config(text=f"Question {current_question_index + 1}: {current_question['question']}")
    
    # Clear previous options
    for widget in option_frame.winfo_children():
        widget.destroy()
    
    # Create new option buttons for the current question
    option_var.set(None)  # Reset option selection
    for option in current_question["options"]:
        option_button = tk.Radiobutton(option_frame, text=option, variable=option_var, value=option)
        option_button.pack()

# Function to move to the next question or display final answers
def next_question():
    global current_question_index
    answer = option_var.get()
    if answer:
        user_answers.append(answer)
        # Update animal points based on user's answer
        animal = questions[current_question_index]["options"][answer]
        animal_points[animal] += 1
        current_question_index += 1
        if current_question_index < len(questions):
            display_question()
        else:
            display_answers()
            next_button.config(state="disabled")  # Disable the "Next" button at the end
            retake_button.config(state="active")  # Enable the "Retake Quiz" button

# Function to display the final answers
def display_answers():
    max_animal = max(animal_points, key=animal_points.get)
    result_label.config(text=f"You're a {max_animal}!")

# Function to retake the quiz
def retake_quiz():
    global current_question_index
    user_answers.clear()
    current_question_index = 0
    for animal in animal_points:
        animal_points[animal] = 0
    display_question()
    result_label.config(text="")  # Clear the result label
    next_button.config(state="active")  # Enable the "Next" button
    retake_button.config(state="disabled")  # Disable the "Retake Quiz" button

# Create a window
window = tk.Tk()
window.title("Animal Quiz")

# Create a label for the question
question_label = tk.Label(window, text="", padx=20, pady=10)
question_label.pack()

# Create a frame for option buttons
option_frame = tk.Frame(window)
option_frame.pack()

# Create a button to move to the next question
next_button = tk.Button(window, text="Next", command=next_question)
next_button.pack(pady=10)

# Create a variable to track the selected option
option_var = tk.StringVar()

# Label to display the result
result_label = tk.Label(window, text="", padx=20, pady=20)
result_label.pack()

# Button to retake the quiz (initially disabled)
retake_button = tk.Button(window, text="Retake Quiz", command=retake_quiz, state="disabled")
retake_button.pack(pady=10)

# Display the first question at the beginning
current_question_index = 0
display_question()

# Start the main window loop
window.mainloop()
