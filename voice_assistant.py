import pyttsx3
import datetime

engine = pyttsx3.init()

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("Assistant: Hello!")
        engine.say("Hello!")
        engine.runAndWait()

    elif "time" in user:
        t = datetime.datetime.now().strftime("%H:%M")
        print("Assistant:", t)
        engine.say("Current time is " + t)
        engine.runAndWait()

    elif "bye" in user:
        print("Assistant: Goodbye")
        engine.say("Goodbye")
        engine.runAndWait()
        break

    else:
        print("Assistant: I did not understand")
        engine.say("I did not understand")
        engine.runAndWait()