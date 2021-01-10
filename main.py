from datetime import datetime
import pyttsx3
import pywhatkit as what
import speech_recognition as sr
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# i = 0
# for voice in voices:
#     print(i)
#     print(voice)
#     i += 1
engine.setProperty('voice', voices[11].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', "")
            return command

    except Exception as e:
        print(e)
        return None


def run_alexa():
    command = take_command()
    print(command)
    if command is None:
        pass

    elif 'play' in command:
        song = command.replace('play ', "")
        talk('playing' + song)
        print(song)
        what.playonyt(song)

    elif 'time' in command:
        time = datetime.now().strftime('%I:%M %p')
        talk(f'It is {time}')

    elif 'info' in command:
        info = command.replace('info about', "")
        # talk(what.info(info, lines=1))
        talk(wikipedia.summary(info, sentences=1))
    else:
        talk("Please say the command again.")

while True:
    run_alexa()
