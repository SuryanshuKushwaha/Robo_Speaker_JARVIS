import pyttsx3

if __name__ == '__main__':
    print("Welcome! This is jarvis speaking...")

    engine = pyttsx3.init()

    while True:
        x = input("Type something (or type 'exit' to quit): ")

        if x.lower() == 'exit':
            break
 
        engine.say(x)
        engine.runAndWait()
