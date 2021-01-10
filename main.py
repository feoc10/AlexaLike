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
engine.setProperty('voice', voices[0].id)
wikipedia.set_lang('pt')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            # listener.adjust_for_ambient_noise(source)
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='pt-BR')
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

    elif 'toca' in command:
        song = command.replace('toca ', "")
        talk('tocando' + song)
        print(song)
        what.playonyt(song)

    elif 'horas' in command:
        time = datetime.now().strftime('%I:%M %p')
        talk(f'São {time}')

    elif 'quem é' in command:
        info = command.replace('quem é', "")
        talk(wikipedia.summary(info, sentences=1))
    else:
        talk("Oche fala de novo.")


while True:
    run_alexa()
