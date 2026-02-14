# Basic Rule-Based Chatbot in Python

import random

def greet():
    return random.choice([
        "Hello there! 👋",
        "Hi! How can I help you today?",
        "Hey! Nice to talk with you."
    ])


def mood_response():
    return random.choice([
        "I'm just a bot, but I'm running perfectly!",
        "All systems are working great!",
        "Feeling helpful as always 😄"
    ])


def study_response():
    return random.choice([
        "Remember to take short breaks while studying!",
        "Consistency is more important than long hours.",
        "Make a small plan before you start studying."
    ])


def creator_response():
    return "I was created using Python as a simple rule-based chatbot!"


def help_response():
    return "You can try typing things like: hello, mood, study, creator, joke, or bye."


def joke_response():
    return random.choice([
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐞",
        "Why did the computer get cold? It forgot to close its Windows!",
        "Why do Java developers wear glasses? Because they don't C#!"
    ])


def unknown_response():
    return "Sorry, I didn't understand that. Type 'help' to see what you can ask."


def chatbot():
    print("🤖 Chatbot: Hello! Type 'help' to see options. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot:", greet())

        elif user_input in ["how are you", "mood", "status"]:
            print("Chatbot:", mood_response())

        elif user_input in ["study", "tips", "study tips"]:
            print("Chatbot:", study_response())

        elif user_input in ["who made you", "creator", "who created you"]:
            print("Chatbot:", creator_response())

        elif user_input in ["help", "options"]:
            print("Chatbot:", help_response())

        elif user_input in ["joke", "make me laugh"]:
            print("Chatbot:", joke_response())

        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        else:
            print("Chatbot:", unknown_response())


# Run the chatbot
chatbot()
