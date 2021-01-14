def locate():
    search_resluts = []
    driver = webdriver.Chrome(executable_path = 'C:/Softwares/selenium webdriver/chromedriver')
    driver.get('https://www.google.com/maps/')
    time.sleep(3)
    speak('. City name where you want to locate :')
    while True:
        city = takeCommand()
        if city != 'None':
            break
        else:
            speak('. Sorry, I did not listen, come again please !')
            
    speak('. Country name :')
    while True:
        country = takeCommand()
        if country != 'None':
            break
        else:
            speak('. Sorry, I did not listen, come again please !')
            
    speak('. what do you want to search for in ' + city +' '+country)
    while True:
        niche = takeCommand()
        if niche != 'None':
            break
        else:
            speak('. Sorry, I did not listen, come again please !')
    
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(niche+','+city+','+country)
    
    driver.find_element_by_xpath('//button[@class="searchbox-searchbutton"]').click()
    time.sleep(3)
    speak('. Okay ! Here is your top 20 search results ')
    for i in driver.find_elements_by_xpath('//h3[@class="section-result-title"]'):
        speak(i.text)
        search_resluts.append(i.text.lower())
    rest = []
    for i in driver.find_elements_by_xpath('//div[@class="section-result"]'):
        rest.append(i)
    time.sleep(1)
    speak('. From these search results which one you want to locate ?')
    time.sleep(1)
    speak('. Let me print it on display, then you just tell me which one you wanna locate')
    print(search_resluts)
    while True:
        restaurant = takeCommand().lower()
        if restaurant in search_resluts:
            break
        else:
            speak('Sorry, I did not listen. Come again please .')
            
    for i in range(len(search_resluts)):
        if restaurant in search_resluts[i]:
            rest[i].click()
            break
    time.sleep(3)
    while True:
        try:
            star_rating = driver.find_element_by_xpath('//div[@class="jqnFjrOWMVU__right"]/div').text
            print(star_rating)
            break
        except NoSuchElementException as exception:
            pass
        
    if float(star_rating) >= 4:
        speak('. This '+niche+' is good '+'It has user rating '+star_rating+' you can go here .')
        time.sleep(1)
        speak('. Do you need more information regarding this '+niche+' .')
        if takeCommand().lower() == 'yes':
            additional_information = []
            for i in driver.find_elements_by_xpath('//div[@class="ugiz4pqJLAG__content"]'):
                additional_information.append(i.text)
            speak('. Okay Tell me what you need .')
            need = takeCommand().lower()
            if 'contact' in need or 'number' in need:
                speak(". Let me check if the "+niche+" has kept it's contact on network or not .")
                flag = False
                for i in additional_information:
                    if '+' in i:
                        flag = True
                        break
                if flag:
                    speak(". Got it's contact, it is " + i )
                else:
                    speak(". Sorry, "+niche+" have kept it's contact private .")
            elif 'website' in need or 'link' in need or 'url' in need:
                speak(". Let me check if the "+niche+" has kept it's website link on network or not .")
                flag = False
                for i in additional_information:
                    if '.com' in i and len(i.split('.')) == 2:
                        flag = True
                        break
                if flag:
                    speak(". Got it's website, it is " + i )
                else:
                    speak(". Sorry, "+niche+" have kept it's website private .")
            elif 'address' in need:
                speak('. Here we go . '+additional_information[0])        
    else:
        speak(". I won't suggest you to go here. Because, this "+niche+" has "+star_rating+" user ratings only .")
