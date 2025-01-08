import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio
import webbrowser
import winshell
from pygame import mixer

language = "pt" #Idioma padrão PT-BR
tld = "com.br" #Sotaque

def get_audio(idioma):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            if idioma == "pt":
                lang = "pt-br"
            else:
                lang = "en-US"
            said = r.recognize_google(audio, language=lang)
            print(said)
        except sr.UnknownValueError:
            print("Repita")
        except sr.RequestError:
            print("Repita, serviço não disponivel")
    return said.lower()
#speak converted audio to text
def speak(text):
    tts = gTTS(text=text, lang=language, tld=tld)
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)
#function to respond to commands
def respond(text):
    print("Texto do audio captado: " + text)
    if 'youtube' in text:
        speak("What do you want to search for") if language == "en"  else  speak("O que você quer procurar?")
        keyword = get_audio()
        if keyword!= '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"This is what I found about {keyword} on youtube") if language == "en" else speak(f"Aqui está o que eu encontrei para {keyword} no youtube")
    elif ('search' if language == "en" else 'pesquise') in text:
        speak("What do you want to search for?") if language == "en" else speak("O que você quer pesquisar?")
        query = get_audio()
        if query !='':
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia") if language == "en" else speak("De acordo com a wikipedia")
            print(result)
            speak(result)
    elif 'joke' in text:
        speak(pyjokes.get_joke())
    elif ('empty recycle bin' if language == "en" else 'esvaziar lixeira') in text:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle bin emptied") if language == "en" else speak("Lixeira esvaziada")
    elif ('what time' if language == "en" else 'que horas') in text:
        strTime = datetime.today().strftime("%H:%M %p")
        print(strTime)
        speak(strTime)
    elif ('play music' if language == "en" else 'tocar música') in text or 'play song' in text:
        speak("Now playing...") if language == "en" else speak("Agora tocando música...")
        music_dir = "C:\\Users\\unico\\Music\\baladag4.com.br_64719" #add your music directory here..
        songs = os.listdir(music_dir)
        print(songs)
        playmusic(music_dir + "\\" + songs[0])
    elif ('stop music' if language == "en" else 'parar música') in text:
        speak("Stopping playback.") if language == "en" else speak("Parando música")
        stopmusic()
    elif ('quit' if language == "en" else 'desconectar') in text:
        speak("Goodbye, till next time") if language == "en" else speak("Tchau, até a proxima")
        exit()
#Tocar musica
def playmusic(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()
#Parar musica
def stopmusic():
    mixer.music.stop()
