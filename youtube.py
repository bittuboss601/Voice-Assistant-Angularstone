def youtube(text):
    count = 0
    search_results = []
    driver = webdriver.Chrome(executable_path = 'C:/Softwares/selenium webdriver/chromedriver')
    driver.get('https://www.youtube.com/')
    time.sleep(3)
    search_box = driver.find_element_by_name('search_query')
    search_box.send_keys(text)
    search_box.submit()
    time.sleep(2)
    speak(' Following are the first ten search results :-')
    video_names = []
    for i in driver.find_elements_by_id('video-title'):
        speak(i.text)
        time.sleep(1)
        video_names.append(i.text.lower())
        count += 1
        if count == 10:
            break
    for i in driver.find_elements_by_xpath('//a[@class="yt-simple-endpoint style-scope ytd-video-renderer"]'):
        search_results.append(i.get_attribute('href'))
    print(video_names)
    speak('Which video do you want me to play ?')
    video_query = takeCommand().lower()
    video_query = listening_algorithm(video_query,video_names)
    while True:
        if video_query in video_names:
                break
        else:
            speak('Sorry, I did not hear. Come again please !')
            video_query = takeCommand().lower()
            video_query = listening_algorithm(video_query,video_names)

    for i in range(len(video_names)):
        if video_query in video_names[i]:
            #add = '1'
            #time_ = []
            #for j in driver.find_elements_by_xpath('//span[@class="style-scope ytd-thumbnail-overlay-time-status-renderer"]'):
                #if j.text == '':
                    #pass
                #else:
                    #time_.append(j.text)
            #actual_time = time_[i]
            
            #for k in range(len(actual_time)):
                #if actual_time[k]==':':
                    #for l in range(k+1,len(actual_time)):
                        #add += '0'
            #print(int(actual_time.replace(':',''))/int(add))
            driver.get(search_results[i])
            time.sleep(1)
            #time.sleep(int(actual_time.replace(':',''))/int(add)*60)
        
    
    while True:
        try:
            skip_ad =  driver.find_element_by_xpath('//div[@class="ytp-ad-text ytp-ad-skip-button-text"]')
            try:
                skip_ad.click()
            except ElementNotInteractableException as exception:
                pass
        except NoSuchElementException as exception:
            pass
        command = takeCommand().lower()
        if command in ["stop","top","pause"] :
            try:
                pause_play = driver.find_element_by_xpath('//button[@class="ytp-play-button ytp-button"]')
                pause_play.click()
            except NoSuchElementException as exception:
                pass
            speak(' What happens sir ? Do you want me to play the next song ?')
            reply2 = takeCommand().lower()
            while True:
                if reply2 != 'None':
                    break
                else:
                    speak(" Sorry I didn't listened. Come again please ! ")
                    reply2 = takeCommand().lower()
                    next_loop = driver.find_element_by_xpath('//a[@class="ytp-next-button ytp-button"]')
                    next_loop.click()
            if reply2 == 'yes':
                try:
                    next_loop = driver.find_element_by_xpath('//a[@class="ytp-next-button ytp-button"]')
                    next_loop.click()
                except NoSuchElementException as exception:
                    pass
                time.sleep(3)
            else:
                speak('Do you want me to play some other videos ?')
                reply = takeCommand().lower()
                while True:
                    if reply != 'None':
                        break
                    else:
                        speak(" Sorry I didn't listened. Come again please ! ")
                        reply = takeCommand().lower()
            
                if reply == 'yes':
                    speak('Say it Brother ?')
                    sq = takeCommand()
                    search_box = driver.find_element_by_name('search_query')
                    search_box.clear()
                    search_box.send_keys(sq)
                    search_box.submit()
                    time.sleep(2)
                    driver.find_element_by_id('video-title').click()
            
                    #add = '1'
                    #time_ = ''
                    #for i in driver.find_elements_by_xpath('//span[@class="style-scope ytd-thumbnail-overlay-time-status-renderer"]'):
                        #if i.text == '':
                            #pass
                        #else:
                            #time_ = i.text
                            #break
                    #print(time_)

                    #for i in range(len(time_)):
                        #if time_[i]==':':
                            #for j in range(i+1,len(time_)):
                                #add += '0'
                    #print(int(time_.replace(':',''))/int(add))
                    #time.sleep(int(time_.replace(':',''))/int(add)*60+3)
                else:
                    pause_play.click()
                    
        elif 'exit' in command:
            break
                        
                    
    driver.close()
