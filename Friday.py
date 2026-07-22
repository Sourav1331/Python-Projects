import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib

r = sr.Recognizer()
intro = pyttsx3.init()

def speak(text):
    intro.say(text)
    intro.runAndWait()

def useCommand(c):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif"open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif"open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif"open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
    elif"open wikipedia" in command.lower():
        webbrowser.open("https://wikipedia.com")
    elif "play" in command.lower():
        song = command.lower().split(" ")[1]
        link = musicLib.music[song]
        webbrowser.open(link)
    elif"shutdown" in command.lower():
        speak("Goodbye Sir")
        print("Goodbye Sir")
        exit()
    else:
        speak("I didn't get that!")

if __name__ == "__main__":
    speak("   Activating Friday...")
    while True:
        print("recongnizing...")
        try:
            with sr.Microphone() as mic:
                print("listening...")
                audio = r.listen(mic, timeout = 2, phrase_time_limit = 1)
            name = r.recognize_google(audio)
            if "friday" in name.lower():
                speak("    Yes, How can i assist you?")
                print("Friday Activated...")

                with sr.Microphone() as mic:
                    audio = r.listen(mic)
                    command = r.recognize_google(audio)
                    print(command)

                    useCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))