def wake(): 
    r = sr.Recognizer() 

    with sr.Microphone() as source: 
        #print("Listening...") 
        #playsound(r'C:\Users\LENOVO\Desktop\coding ninja\Notifications\Pixel Sounds\Trill (online-audio-converter.com).mp3')
        r.pause_threshold = 1
        print("Listening...") 
        audio = r.listen(source,timeout=10) 

    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 

    except Exception as e: 
        print(e) 
        print("Unable to Recognizing your voice.") 
        return False
    if query != "None":
        playsound(r'C:\Users\LENOVO\Desktop\coding ninja\Notifications\Pixel Sounds\Trill (online-audio-converter.com).mp3')
        return True