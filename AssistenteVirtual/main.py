from gtts import gTTS
import os
import playsound
from functions import respond, get_audio, speak
from shared import language, tld  # Importar variáveis compartilhadas

os.system('cls||clear')

#Criação do Menu de Acesso
speak("Olá, me chamo Lívia, sua Assistente Virtual", language)
while True:
    os.system('cls||clear')
    print("Escolha a ferramenta que deseja")
    print("[1] Converter Texto para áudio")
    print("[2] Assistente por áudio")
    print("[3] Mudar idioma")
    print("[0] Fechar")

    opcao = input()
    match opcao:
        case '0':
            break
        case '1':
            text = input("Digite o texto: ")
            tts = gTTS(text=text, lang=language, tld=tld)
            filename = "voice.mp3"
            try:
                os.remove(filename)
            except OSError:
                pass
            tts.save(filename)
            playsound.playsound(filename)
            os.system('cls||clear')
        case '2':
            #get mic audio

            while True:
                print("I am listening...")  if language == "en" else print("Estou escutando")
                text = get_audio(language)
                respond(text, language)
        case '3':
            while True:
                print("[1] Português (Brasil)")
                print("[2] English (U.S.A)")
                print("[0] Voltar")
                escolha = input()
                match escolha:
                    case '1':
                        language = "pt"
                        tld = "com.br"
                        os.system('cls||clear')
                        break
                    case '2':
                        language = "en"
                        tld = "us"
                        os.system('cls||clear')
                        break
                    case '0':
                        os.system('cls||clear')
                        break
                    case _:
                        print("Escolha uma opção.")

        case _:
            os.system('cls||clear')
            print("Escolha uma opção.")
