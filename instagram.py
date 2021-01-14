def Instagram():
    import insta_credentials
    driver = webdriver.Chrome(executable_path = 'C:/Softwares/selenium webdriver/chromedriver')
    driver.get('https://www.instagram.com/')
    time.sleep(3)
    #driver.maximize_window()
    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    usrname = insta_credentials.insta_mail()
    pwd = insta_credentials.insta_password()
    username.send_keys(usrname)
    password.send_keys(pwd)
    password.submit()
    
    # Handles Pop Up
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]').click()
    except NoSuchElementException: 
        pass
    time.sleep(5)
    try:
        driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]').click()    
    except NoSuchElementException: 
        try:
            a = driver.find_elements_by_xpath('//div[@class="mt3GC"]/button')
            alert = a[-1]
            alert.click()
        except NoSuchElementException:
            pass

    time.sleep(2)
    speak("I am in your Instagram Network . What's next instruction ? ")
    
    l0 = ["scroll down","call down","call don","call up","down","roll down","croll down","up","scroll up","roll up","croll up","start stories","play stories","start story","play story",
                          "stop stories","end stories","stop story","exit story","exit stories","top stories","top story",
                          "message", "messages" ,"inbox","home","notification","notifications","activity","explore","explorer",
                           "send follow requests","send follow request","follow request","follow","exit","close"]
    while True:
        command = takeCommand().lower()
        while True:
            if len([i for i in l0 if i in command]) != 0:
                break
            else:
                speak("Please say it again !")
                command = takeCommand().lower()
                
        l1 = ["scroll down","call down","call don","call up","down","roll down","croll down","up","scroll up","roll up","croll up"]
        if len([i for i in l1 if i in command]) != 0:  
            print('calling scroll down function')
            Instagram_scroller(driver,command)
        
        l2 = ["start stories","play stories","start story","play story"]
        if len([i for i in l2 if i in command]) != 0: 
            speak("Starting the stories .")
            start_story = driver.find_element_by_xpath('//li[@class="Ckrof"]').click()
        
        l3 = ["stop stories","end stories","stop story","exit story","exit stories","top stories","top story"]
        if len([i for i in l3 if i in command]) != 0:
            speak("Closing the stories .")
            close_story = driver.find_element_by_xpath('//span[@class="Szr5J"]').click()

        l4 = ["message","messages","inbox"]
        if len([i for i in l4 if i in command]) != 0:
            speak("Opening Message .")
            unread_message_flag = False
            driver.get(driver.find_element_by_xpath('//a[@class="xWeGp"]').get_attribute('href'))
            time.sleep(5)
            try:
                unread_messages = driver.find_elements_by_xpath('//div[@class=" _41V_T  Sapc9                 Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              "]')
                speak(' You have '+str(len(unread_messages))+ ' unread message left .')
                unread_message_flag = True
            except NoSuchElementException as exception:
                pass

            if unread_message_flag:
                speak("Do you want me to read those unread messages ?")
                unread_message_command = takeCommand().lower()
                while True:
                    if unread_message_command in ["yes","no"]:
                        break
                    else:
                        speak("Sorry, I couldn't hear. Come again please !")
                        unread_message_command = takeCommand().lower()
                if unread_message_command == "yes":
                    for i in unread_messages:
                        i.click()
                        time.sleep(2)
                        try:
                            speak("Okay !")
                            time.sleep(1)
                            speak(driver.find_element_by_xpath('//div[@class="_7UhW9   xLCgt      MMzan  KV-D4             p1tLr      hjZTB"]').text)
                        except NoSuchElementException as exception:
                            speak(" Seems like you have a video or some image. Check that on display")
                else:
                    speak("Okay !")
                    time.sleep(1)
                    speak("would you like to text some one instead ?")
                    text_message_command = takeCommand().lower()
                    while True:
                        if text_message_command in ["yes","no"]:
                            break
                        else:
                            speak("Sorry, I couldn't hear. Come again please !")
                            text_message_command = takeCommand().lower()
                    if text_message_command == "yes" or text_message_command == "okay" or text_message_command == "ok":
                        speak("Whom do you want to send message ?")
                        sender_name = takeCommand()
                        while True:
                            if sender_name != "None":
                                break
                            else:
                                speak("Sorry, I couldn't hear. Come again please !")
                                sender_name = takeCommand()
                        driver.get(driver.find_element_by_xpath('//a[@class="xWeGp"]').get_attribute('href'))
                        time.sleep(1)
                        driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]').click()
                        time.sleep(1)
                        while True:
                            try:
                                driver.find_element_by_xpath('//input[@class="j_2Hd     uMkC7 M5V28"]').send_keys(sender_name)
                                break
                            except NoSuchElementException as exception:
                                pass
                        time.sleep(2)
                        try:
                            if driver.find_element_by_xpath('//div[@class="_7UhW9   xLCgt      MMzan   _0PwGv         uL8Hv         "]').text == "No account found.":
                                speak(" Please say the name again !")
                                sender_name = takeCommand()
                                driver.find_element_by_xpath('//div[@class="QBdPU "]').click()
                                driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]').click()
                                driver.find_element_by_xpath('//input[@class="j_2Hd     uMkC7 M5V28"]').send_keys(sender_name)
                        except NoSuchElementException as exception:
                            pass
                                
                                 
                        sender_name_data = []
                        sender_name_link = []
                        time.sleep(3)
                        try:
                            for i in driver.find_elements_by_xpath('//div[@class="_7UhW9   xLCgt       qyrsm KV-D4          uL8Hv         "]'):
                                sender_name_data.append(i.text)
                                sender_name_link.append(i)
                        except NoSuchElementException as exception:
                            pass
                        sender_name = listening_algorithm(sender_name,sender_name_data)
                        sender_name_link[sender_name_data.index(sender_name)].click()
                        driver.find_element_by_xpath('//div[@class="rIacr"]').click()
                        time.sleep(2)
                        speak("Say your message sir .")
                        say_message_command = takeCommand()
                        while True:
                            if say_message_command != "None":
                                break
                            else:
                                speak(" I couldn't hear. Please say it again .")
                                say_message_command = takeCommand()
                        driver.find_element_by_xpath('//div[@class="X3a-9"]').click()
                        driver.find_element_by_tag_name("textarea").send_keys(say_message_command)
                        driver.find_element_by_xpath('//div[@class="                    Igw0E     IwRSH      eGOV_         _4EzTm                                        JI_ht                                                                      "]').click()
                        speak("Message delivered !")


        elif "home" in command:
            driver.find_element_by_xpath('//div[@class="Fifk5"]').click()
            time.sleep(2)
        
        l5 = ["notification", "notifications","activity"]
        if len([i for i in l5 if i in command]) != 0:
            while True:
                try:
                    buttons = driver.find_elements_by_xpath('//div[@class="_47KiJ"]/div')
                    buttons[3].click()
                    break
                except NoSuchElementException as exception:
                    pass 
            time.sleep(3)
            try:
                speak(" You have "+driver.find_element_by_xpath('//div[@class="JRHhD"]').text+" pending follow requests .")
            except NoSuchElementException as exception:
                        pass
            '''try:
                notify_count = 0
                for i in driver.find_elements_by_xpath('//div[@class="HkZvO"]'):
                    speak(i.text + " started following you .")
                    notify_count += 1
                    if notify_count > 10:
                        break
            except NoSuchElementException as exception:
                        pass'''
            notification_count = 0
            try:
                for i in driver.find_elements_by_xpath('//div[@class="PUHRj  H_sJK"]'):
                    speak(i.text)
                    notification_count += 1
                    time.sleep(1)
                    if notification_count >20:
                        break
            except NoSuchElementException as exception:
                pass
            speak("Closing Notifications ")
            buttons = driver.find_elements_by_xpath('//div[@class="_47KiJ"]/div')
            explore = buttons[3]
            explore.click()
        
        l6 = ["explore","explorer"]
        if len([i for i in l6 if i in command]) != 0:
            buttons = driver.find_elements_by_xpath('//div[@class="_47KiJ"]/div')
            explore = buttons[2]
            explore.click()
            time.sleep(3)

        l7 = ["send follow requests","send follow request","follow request","follow"]
        if len([i for i in l7 if i in command]) != 0:
            speak("Tell me the common interest of people whom you want to send requests .")
            follow_request_command = takeCommand().lower()
            while True:
                if follow_request_command != "None":
                    break
                else:
                    speak("Please , come again .")
                    follow_request_command = takeCommand().lower()
            Instagram_following_bot(driver,follow_request_command)
        
        l8 = ["exit","close","closed","exits"]
        if len([i for i in l8 if i in command]) != 0:
            speak("Closing the Instagram .")
            driver.close()
