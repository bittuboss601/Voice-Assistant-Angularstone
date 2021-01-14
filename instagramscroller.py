def Instagram_scroller(driver,command):
    print('In scroller function')
    while True:
        while True:
            l0 = ["scroll up","call down","call don","scroll down","up","down","exit","roll down","croll down","roll up","croll up"]
            if len([i for i in l0 if i in command]) != 0:
                break
            else:
                speak("Please , come again .")
                command = takeCommand().lower()
        print("in scroller function, while loop")        
        l = ["scroll down","down","roll down","croll down"]
        if len([i for i in l if i in command]) != 0:
            print("voice gets recognized")
            speak("Scrolling Down the pan")
            while True:
                driver.execute_script("window.scrollBy(0,500)","")
                time.sleep(0)
                q = takeCommand().lower()
                if "stop" in q or "exit" in q or "top" in q:
                    speak("Exiting the scroll down")
                    break
        l2 = ["scroll up","croll up","up","roll up","call app"]
        if len([i for i in l2 if i in command]) != 0:
            speak("Scrolling up the pan")
            while True:
                driver.execute_script("scrollBy(0,-2000);")
                time.sleep(0)
                q = takeCommand().lower()
                if "stop" in q or "exit" in q or "top" in q:
                    speak("Exiting the scroll up")
                    break
        command = takeCommand().lower()
        if "exit" in command:
            speak("exiting from scroller")
            break