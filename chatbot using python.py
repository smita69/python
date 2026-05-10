# Simple Chatbot in Python

name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("In which country do you live: ")
city = input("Name of your city/village: ")

std = input("Are you a school student or college student? (college/school): ")

if std == "college":
    course = input("Which course are you doing: ")
    cls = input("In which year are you of your college: ")
else:
    cls = input("In which class do you read: ")
    course = "not applicable"

skill = input("Do you have any skill? (yes/no): ")
if skill == "yes":
    skl = input("Which type of skills do you have: ")
else:
    skl = "you don't have any skill"

nskl = input("Are you learning any new skill? (yes/no): ")
if nskl == "yes":
    newskill = input("Which skill are you working on: ")
else:
    newskill = "nothing"

print("\nWELCOME TO CHATBOX ❤️\n")

def get_bot_response(user_input):
    input = user_input.lower()

    if "hello" in input or "hi" in input or "hey" in input:
        return f"Hello {name}! How can I help you?"

    elif "about me" in input or "my name" in input:
        return f"Your name is {name}. You are {age} years old.\nYou are from {country}, you live in {city}.\nYou are a {std} student in {cls}.\nYour skills: {skl}. Currently working on: {newskill}"

    elif "profession" in input or "am i doing" in input:
        return f"You are a {std} student in {cls}"

    elif "skills" in input:
        return f"Your skills are: {skl}. Currently working on: {newskill}"

    elif "course" in input:
        return f"You are doing {course}"

    elif "about you" in input:
        return "I am a simple chatbot built in Python."

    elif "sad" in input:
        return f"Don't be sad {name} ❤️"

    elif "confuse" in input:
        return f"Stay calm {name}, things will be clear ❤️"

    elif "happy" in input:
        return f"Nice to hear that {name} 😄"

    elif "how are you" in input:
        return "I am fine, thanks!"

    elif "joke" in input:
        return "Why do elephants never use computers? Because they are afraid of the mouse! 😂"

    elif "story" in input:
        return "Once a dog saw his reflection and lost his bone due to greed."

    elif "html" in input:
        return "HTML is used to create webpages using tags."

    elif "bye" in input:
        return "Goodbye! Take care ❤️"

    else:
        return "Sorry, I don't understand."


# Chat loop
while True:
    user_input = input("\nYou: ")

    if user_input.strip() == "":
        print("Bot: Please type something")
        continue

    response = get_bot_response(user_input)
    print("Bot:", response)

    if "bye" in user_input.lower():
        break
