#Si no funcionan las dos notificaciones es porque posiblemente el Asistente de concentración no tenga seleccionado el radio button de "Desactivado"

import random
import os
import time
from plyer import notification

def get_script_directory():
    return os.path.dirname(os.path.abspath(__file__))

def desktop_notifier(title, message, timeout):
    script_directory = get_script_directory()
    icon_path = os.path.join(script_directory, "coding.ico")
    # from https://icon-icons.com/es/icono/chat-comunicaci%C3%B3n-mensaje-amor/256510
    
    notification.notify(
        title=title,
        message=message,
        timeout=timeout,
        app_icon=icon_path
    )

questions = {
    "q1": {
        "question": "What's your favorite color?\n(a) Red\n(b) Blue\n(c) Green",
        "answers": {
            "a": "Lion",
            "b": "Dolphin",
            "c": "Koala"
        }
    },
    "q2": {
        "question": "What's your ideal vacation?\n(a) Safari\n(b) Beach\n(c) Mountains",
        "answers": {
            "a": "Tiger",
            "b": "Shark",
            "c": "Eagle"
        }
    },
    "q3": {
        "question": "What's your favorite activity?\n(a) Sleeping\n(b) Swimming\n(c) Flying",
        "answers": {
            "a": "Sloth",
            "b": "Fish",
            "c": "Bird"
        }
    },
    "q4": {
        "question": "What's your favorite food?\n(a) Steak\n(b) Pizza\n(c) Salad",
        "answers": {
            "a": "Lion",
            "b": "Dolphin",
            "c": "Koala"
        }
    },
    "q5": {
        "question": "What's your favorite season?\n(a) Summer\n(b) Winter\n(c) Spring",
        "answers": {
            "a": "Tiger",
            "b": "Shark",
            "c": "Eagle"
        }
    },
    "q6": {
        "question": "What's your favorite movie genre?\n(a) Action\n(b) Romance\n(c) Comedy",
        "answers": {
            "a": "Sloth",
            "b": "Fish",
            "c": "Bird"
        }
    },
    "q7": {
        "question": "What's your preferred mode of transportation?\n(a) Car\n(b) Bicycle\n(c) Plane",
        "answers": {
            "a": "Lion",
            "b": "Dolphin",
            "c": "Koala"
        }
    },
    "q8": {
        "question": "What's your favorite book genre?\n(a) Mystery\n(b) Fantasy\n(c) Biography",
        "answers": {
            "a": "Tiger",
            "b": "Shark",
            "c": "Eagle"
        }
    },
    "q9": {
        "question": "What's your favorite music genre?\n(a) Rock\n(b) Pop\n(c) Classical",
        "answers": {
            "a": "Sloth",
            "b": "Fish",
            "c": "Bird"
        }
    },
    "q10": {
        "question": "What's your favorite hobby?\n(a) Painting\n(b) Cooking\n(c) Hiking",
        "answers": {
            "a": "Lion",
            "b": "Dolphin",
            "c": "Koala"
        }
    },
    "q11": {
        "question": "What's your favorite sport?\n(a) Soccer\n(b) Tennis\n(c) Swimming",
        "answers": {
            "a": "Tiger",
            "b": "Shark",
            "c": "Eagle"
        }
    },
    "q12": {
        "question": "What's your favorite outdoor activity?\n(a) Camping\n(b) Picnic\n(c) Biking",
        "answers": {
            "a": "Sloth",
            "b": "Fish",
            "c": "Bird"
        }
    },
    "q13": {
        "question": "What's your favorite drink?\n(a) Coffee\n(b) Tea\n(c) Juice",
        "answers": {
            "a": "Lion",
            "b": "Dolphin",
            "c": "Koala"
        }
    },
    "q14": {
        "question": "What's your favorite holiday?\n(a) Christmas\n(b) Halloween\n(c) Thanksgiving",
        "answers": {
            "a": "Tiger",
            "b": "Shark",
            "c": "Eagle"
        }
    },
    "q15": {
        "question": "What's your favorite superhero?\n(a) Superman\n(b) Spider-Man\n(c) Wonder Woman",
        "answers": {
            "a": "Sloth",
            "b": "Fish",
            "c": "Bird"
        }
    },
    "q16": {
        "question": "What's your favorite animal?\n(a) Elephant\n(b) Giraffe\n(c) Panda",
        "answers": {
            "a": "Lion",
            "b": "Dolphin",
            "c": "Koala"
        }
    },
    "q17": {
        "question": "What's your favorite type of weather?\n(a) Sunny\n(b) Rainy\n(c) Snowy",
        "answers": {
            "a": "Tiger",
            "b": "Shark",
            "c": "Eagle"
        }
    },
    "q18": {
        "question": "What's your favorite dessert?\n(a) Ice Cream\n(b) Cake\n(c) Pie",
        "answers": {
            "a": "Sloth",
            "b": "Fish",
            "c": "Bird"
        }
    },
    "q19": {
        "question": "What's your favorite board game?\n(a) Monopoly\n(b) Chess\n(c) Scrabble",
        "answers": {
            "a": "Lion",
            "b": "Dolphin",
            "c": "Koala"
        }
    },
    "q20": {
        "question": "What's your favorite flower?\n(a) Rose\n(b) Sunflower\n(c) Tulip",
        "answers": {
            "a": "Tiger",
            "b": "Shark",
            "c": "Eagle"
        }
    },
}

user_answers = []

def calculate_result(answers):
    animal_counts = {
        "Lion": 0,
        "Tiger": 0,
        "Sloth": 0,
        "Dolphin": 0,
        "Shark": 0,
        "Bird": 0,
        "Koala": 0,
        "Eagle": 0,
        "Fish": 0,
    }
    
    for i, answer in enumerate(answers):
        for question, choices in questions.items():
            if answer in choices["answers"]:
                animal = choices["answers"][answer]
                animal_counts[animal] += 1
    
    max_count = max(animal_counts.values())
    result = [animal for animal, count in animal_counts.items() if count == max_count]
    
    if len(result) == 1:
        return result[0]
    else:
        return random.choice(result)

def take_quiz():
    print("Welcome to the 'Which Animal Are You?' quiz!\n")
    for question_id, question_data in questions.items():
        print(question_data["question"])
        user_answer = input("Your choice: ").lower()
        while user_answer not in question_data["answers"]:
            print("Invalid choice. Please choose from (a), (b), or (c).")
            user_answer = input("Your choice: ").lower()
        user_answers.append(user_answer)
        print("\n")

    animal_result = calculate_result(user_answers)
    print(f"\nYou are a {animal_result}!")

    # Notify the user of the result
    notification_title = "Quiz"
    notification_message = f"Test finished. You're a {animal_result}!"
    notification_timeout = 10 

    script_directory = get_script_directory()
    icon_path = os.path.join(script_directory, "coding.ico")    
    
    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=notification_timeout,
        app_icon=icon_path

    ) 

# Main program
if __name__ == "__main__":

    title = "Quiz"
    message = "Welcome to the animal quiz!"
    timeout = 10
    desktop_notifier(title, message, timeout)

    take_quiz()