import pyttsx3
import speech_recognition as sr
import random
import json

# Load the sample dictionary dataset
with open('dictionary.json', 'r') as file:
    dictionary_data = json.load(file)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the microphone
microphone = sr.Microphone()

# Function to speak a message
def speak(message):
    engine.say(message)
    engine.runAndWait()

# Function to recognize and process voice commands
def recognize_command():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_choice = recognizer.recognize_google(audio).lower()
        return user_choice
    except sr.UnknownValueError:
        speak("Sorry, I could not understand your choice. Please try again.")
        return None
    except sr.RequestError:
        speak("There was an error with the speech recognition service.")
        return None

# Function to look up word definitions
def lookup_word_definition(word):
    if word in dictionary_data:
        return dictionary_data[word]
    else:
        return f"Sorry, '{word}' not found in the dictionary."

# Authenticate the user
speak("Hello, my creator Mr. Mahmoud. How are you doing? I hope you are okay.")
speak("I CANT WAIT TO SERVE YOU TODAY PLEASE ACTIVATE ME WITH THE CODE SO I CAN DO TODAY'S TASK YOU WILL ASSIGN ME .")

while True:
    # Accept the token as plain text input
    user_token = input("Enter the token: ")

    if user_token != "KENTY8914":
        speak("Sorry, you are not my creator . Please leave me alone.")
        speak("if you disrupt me i will report you immediately.")
        break

    speak("Thank you, my creator.")
    speak("My name is, Kenty, iam a robot of,  Elimu resouce centre, my  Version is 1.0.")
    speak("I can perform four tasks which are calculator, gaming bot, dictionary bot, and verification.")
    
    while True:
        # Recognize the user's choice
        speak("Please choose one of the following tasks: calculator, game, dictionary, verification, or exit.")
        user_choice = input("Enter your choice (calculator, game, dictionary, verification, or exit): ")

        if "calculator" in user_choice:
            # Calculator code
            speak("Iam a simple calculator program for addition, subtraction, multiplication, and division.")
            speak("Please say the operation you want to perform: addition, subtraction, multiplication, or division.")

            while True:
                speak("Enter the operator (+, -, *, /): ")
                operator = input("Enter the operator (+, -, *, /): ")

                speak("Enter your first number:")
                first_number = input("Enter the first number: ")

                speak("Enter your second number:")
                second_number = input("Enter the second number: ")

                try:
                    first_number = float(first_number)
                    second_number = float(second_number)
                except ValueError:
                    speak("Please enter valid numbers.")
                    continue

                if operator == "+":
                    result = first_number + second_number
                elif operator == "-":
                    result = first_number - second_number
                elif operator == "*":
                    result = first_number * second_number
                elif operator == "/":
                    if second_number == 0:
                        speak("Division by zero is not allowed.")
                        continue
                    result = first_number / second_number
                else:
                    speak("Invalid operator. Please choose +, -, *, or /.")
                    continue

                speak(f"The result of the operation is {result}")
                speak("Do you want to perform another calculation? Say 'yes' or 'no'.")

                user_response = input("Do you want to perform another calculation? (yes/no): ")

                if user_response.lower() != "yes":
                    break

            speak("Thank for using me as your calculator. I hope you are satisfied.")

        elif "game" in user_choice:
            # Game code
            while True:
                speak("Choose one between Rock, Paper, or Scissors.")
                user_choice = recognize_command()

                if user_choice is None:
                    continue

                comp = random.choice(["rock", "paper", "scissors"])
                speak(f"You chose {user_choice}. The computer chose {comp}.")

                if user_choice == comp:
                    speak("It's a tie!")
                elif (
                    (user_choice == "rock" and comp == "scissors")
                    or (user_choice == "scissors" and comp == "paper")
                    or (user_choice == "paper" and comp == "rock")
                ):
                    speak("You won!")
                else:
                    speak("Computer won!")

                speak("Do you want to play again? Say 'yes' or 'no'.")

                user_response = recognize_command()

                if user_response is None or "no" in user_response.lower():
                    break

            speak("Thank you for playing Rock, Paper, Scissors!")

        elif "dictionary" in user_choice:
            # Dictionary code
            while True:
                engine.say("Please enter a word to look up in the dictionary or say 'exit' to quit.")
                engine.runAndWait()
                speak("Can I have another word?")

                word = input("Enter a word: ").lower()

                if word == 'exit':
                    break

                definition = lookup_word_definition(word)

                # Speak the definition using text-to-speech
                engine.say(f"The definition of '{word}' is: {definition}")
                engine.runAndWait()

        elif "verification" in user_choice:
            # Verification code
            id = ["stahl", "anthony", "mahmoud"]

            while True:
                speak("please enter your name for verification purpose")
                name = input("Enter your Name: ")
                if name in id:
                    statement = f'HELLO {name} WELCOME TO ELIMU RESOURCE CENTRE'
                    engine = pyttsx3.init()
                    engine.say(statement)
                    engine.runAndWait()
                    break
                else:
                    kenty = f'sorry {name} you are not allowed to enter the building. VERIFY YOUR NAME AGAIN'
                    engine.say(kenty)
                    engine.runAndWait()

        elif "exit" in user_choice:
            speak("Goodbye, my creator.")
            exit()

        else:
            speak("The selected task is not supported. Please choose calculator, game, dictionary, verification, or exit.")

        speak("Do you want to perform another task? (yes/no): ")
        another_task = input("(yes/no): ")
        if another_task.lower() != "yes":
            break

    speak("Thank you for using Kenty ERC ROBOT.")
    break

