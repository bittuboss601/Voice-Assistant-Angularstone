if __name__ == '__main__': 
    clear = lambda: os.system('cls') 
 
    clear()
    voice_count = 0
    if wake():
        wishMe() 
        #usrname() 

        assname = 'Angularstone'


        while True: 

            query = takeCommand().lower() 

            if 'wikipedia' in query: 
                speak('Searching Wikipedia...') 
                query = query.replace("wikipedia", "") 
                results = wikipedia.summary(query, sentences = 3) 
                speak("According to Wikipedia") 
                print(results) 
                speak(results) 

            elif 'open youtube' in query: 
                speak("Here you go to Youtube\n") 
                webbrowser.open("youtube.com") 

            elif 'open google' in query: 
                speak("Here you go to Google\n") 
                webbrowser.open("google.com") 

            elif 'open stackoverflow' in query: 
                speak("Here you go to Stack Over flow.Happy coding") 
                webbrowser.open("stackoverflow.com") 

            elif 'play music' in query or "play song" in query: 
                speak("Here you go with music") 
                # music_dir = "G:\\Song" 
                music_dir = "D:\Video Songs"
                songs = os.listdir(music_dir) 
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))

            elif 'date' in query:
                speak(getDate())
            
            elif 'change voice' in query:
                if voice_count % 2 == 0:
                    engine.setProperty('voice', voices[1].id)
                else:
                    engine.setProperty('voice', voices[0].id)
                speak("I am at your service sir !")  

            elif 'time' in query:
                speak(time_())

            elif 'open upwork' in query: 
                speak('Happy Freelancing Boss .')
                codePath = r"C:\Softwares\UpworkSetup64.exe"
                os.startfile(codePath)

            elif 'send email' in query: 
                try: 
                    speak("What should I say?") 
                    content = takeCommand() 
                    to = "bittuboss601@gmail.com"
                    sendEmail(to, content) 
                    speak("Email has been sent !") 
                except Exception as e: 
                    print(e) 
                    speak("I am not able to send this email") 

            elif 'how are you' in query: 
                speak("I am fine, Thank you") 
                speak("How are you, Sir") 

            elif 'fine' in query or "good" in query: 
                speak("It's good to know that your fine") 

            elif 'are you human' in query:
                speak('No, I am not Human .')

            elif "change my name to" in query: 
                query = query.replace("change my name to", "") 
                assname = query 

            elif "change name" in query: 
                speak("What would you like to call me, Sir ") 
                assname = takeCommand() 
                speak("Thanks for naming me") 

            elif "what's your name" in query or "What is your name" in query: 
                speak("My friends call me") 
                speak(assname) 
                print("My friends call me", assname) 

            elif 'exit' in query: 
                speak("Thanks for giving me your time") 
                break

            elif "who made you" in query or "who created you" in query: 
                speak("I have been created by Purnendu Tiwari, Nitin Aryan, Mayank Chhabra, Anuj Himachal wala and Ajit Bhalerao.") 

            elif 'joke' in query: 
                speak('I am not so good in cracking jokes, still I will try my best .')
                time.sleep(1)
                speak(pyjokes.get_joke()) 

            elif "calculate" in query: 
                
                import wolframa_alpha
                app_id = wolframa_alpha.wolframa_alpha()
                client = wolframalpha.Client(app_id) 
                indx = query.lower().split().index('calculate') 
                query = query.split()[indx + 1:] 
                res = client.query(' '.join(query)) 
                answer = next(res.results).text 
                print("The answer is " + answer) 
                speak("The answer is " + answer)

            elif 'search' in query: # Example 'search Black Hole'
                searchOnNet(query.replace('search',''))

            elif 'search on net' in query or 'play on net' in query: 

                query = query.replace("search", "") 
                query = query.replace("play", "") 
                webbrowser.open(query) 

            elif "who i am" in query: 
                speak("If you talk then definately you are human.") 

            elif "why you came to world" in query: 
                speak("....future is yet to be decide. That's why I am here .")  

            elif 'is love' in query: 
                speak("Love is a pure emotion. Sometimes, humans relate true love with divine .") 

            elif "who are you" in query: 
                speak("......I am Angularstone version 1 point o . Powered by Raspberry Pi, model 3 B. I am Artificial Intelligence Assistant , created by Angularstone family") 

            elif 'what is angular stone' in query: 
                speak("... It is a startup, owned by Purnendu Tiwari, to develop Intelligent Systems like me. To serve Humans .")  

            elif 'news' in query: 
                news() 

            elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 

            elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 

            elif 'empty recycle bin' in query: 
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
                speak("Recycle Bin Recycled") 

            elif "don't listen" in query or "stop listening" in query: 
                n = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
                speak('Pronounce numbers like 1 0 for ten .')
                time.sleep(1)
                speak("for how much time you want to stop jarvis from listening commands") 
                a = takeCommand().lower()
                a = a.split(' ')
                sleep_time = ''
                for i in a:
                    sleep_time += i
                time.sleep(int(sleep_time)) 
                print(a) 

            elif "locate" in query: 
                locate()

            elif "camera" in query or "take a photo" in query: 
                speak('Opening Camera')
                ec.capture(0, "Jarvis Camera ", "img.jpg") 

            elif "restart" in query: 
                speak('Restarting the system .')
                subprocess.call(["shutdown", "/r"]) 

            elif "hibernate" in query or "sleep" in query: 
                speak("Hibernating") 
                subprocess.call("shutdown / h") 

            elif "log off" in query or "sign out" in query: 
                speak("Make sure all the application are closed before sign-out") 
                time.sleep(5) 
                subprocess.call(["shutdown", "/l"]) 

            elif "write a note" in query: 
                speak("What should i write, sir") 
                note = takeCommand() 
                file = open('jarvis.txt', 'w') 
                speak("Sir, Should i include date and time") 
                snfm = takeCommand() 
                if 'yes' in snfm or 'sure' in snfm: 
                    time__ = ''
                    time_().split(' ')[3:]
                    time__ = time_().split(' ')[-2]+' '+time_().split(' ')[-1]

                    strTime = time__ 
                    file.write(strTime) 
                    file.write(" :- ") 
                    file.write(note) 
                else: 
                    file.write(note) 

            elif "show note" in query: 
                speak("Showing Notes") 
                file = open("jarvis.txt", "r") 
                print(file.read()) 
                speak(file.read(6)) 

            elif "angularstone" in query: 

                wishMe() 
                speak("Angularstone, version one point O") 
                speak(assname) 

            elif "weather" in query: 
                data = Weather_Search()
                speak('Temperature is :'+str(round((data['list'][0]['main']['temp'] -273.15),2))+' degree Celsius '+'.')
                time.sleep(1)
                speak('The temperature feels like'+str(round((data['list'][0]['main']['feels_like']-273.15),2))+' degree Celsius '+'.')
                time.sleep(1)
                speak('Minimum temperature is :'+str(round((data['list'][0]['main']['temp_min']-273.15),2))+' degree Celsius '+'.')
                time.sleep(1)
                speak('Maximum temperature is :'+str(round((data['list'][0]['main']['temp_max']-273.15),2))+' degree Celsius '+'.')
                time.sleep(1)
                speak('Air pressure is around '+str(round(data['list'][0]['main']['pressure'],2))+'.')
                time.sleep(1)
                speak('Humidity value is'+str(round(data['list'][0]['main']['humidity'],2))+'.')
                time.sleep(1)
                speak('Wind Speed is '+str(data['list'][0]['wind']['speed'])+' and wind direction is '+str(data['list'][0]['wind']['deg'])+' degrees .')
                time.sleep(1)
                speak('Rain Information'+str(data['list'][0]['rain'])+'.')
                time.sleep(1)
                speak('Snow information :'+str(data['list'][0]['snow'])+'.')
                time.sleep(1)
                speak('Weather description :'+str(data['list'][0]['weather'][0]['description'])+'.')

            elif "send message" in query: 
                # You need to create an account on Twilio to use this service 
                send_message()
                speak('Message sent successfully.')

            elif "wikipedia" in query: # ->
                webbrowser.open("wikipedia.com") 

            elif "good morning" in query: 
                speak("A warm" +query) 
                speak("How are you Mister") 
                speak(assname) 

            elif "will you be my girlfriend" in query or "will you be my boyfriend" in query: 
                speak("I'm not sure about, may be you should give me some time") 

            elif "how are you" in query: 
                speak("I'm fine, glad you me that") 

            elif "i love you" in query: 
                speak("It's hard to understand") 

            elif "what is" in query or "who is" in query: 

                import wolframa_alpha
                client = wolframalpha.Client(wolframa_alpha.wolframa_alpha()) 
                res = client.query(query) 
                try: 
                    print (next(res.results).text) 
                    speak (next(res.results).text) 
                except StopIteration: 
                    print ("No results") 

            elif 'youtube' in query or 'play' in query:
                youtube(query.replace('youtube',''))
        
            elif 'instagram' in query:
                speak('Opening Instagram')
                Instagram()

            elif query in ['navigate','navigation','nevigate']:
                speak('Opening Google Navigation !')
                navigation()
                
            elif query in ['amazon','order from amazon','open amazon','amazon.com','buy from amazon','add to cart on amazon']:
                speak('What you like to order ?')
                order_text = takeCommand().lower()
                while True:
                    if order_text != "None":
                        break
                    else:
                        speak('Come again please !')
                        order_text = takeCommand().lower()
                amazon_order(order_text)