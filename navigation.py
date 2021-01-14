def navigation():
    driver = webdriver.Chrome(executable_path = 'C:/Softwares/selenium webdriver/chromedriver')
    driver.get('https://www.google.com/maps/')
    time.sleep(3)
    speak('Okay ! Tell me the Source Address  :')
    source_address = takeCommand()
    while True:
        if source_address != 'None':
            break
        else:
            speak('. Sorry, I did not listen, come again please !')
            source_address = takeCommand()

    speak(' Your Destination Address')
    Destination_address = takeCommand()
    while True:
        if Destination_address != 'None':
            break
        else:
            speak('. Sorry, I did not listen, come again please !')
            Destination_address = takeCommand()

    search_box = driver.find_element_by_name('q')
    search_box.send_keys(source_address+' to '+Destination_address)

    driver.find_element_by_xpath('//button[@class="searchbox-searchbutton"]').click()
    time.sleep(3)
    try:
        if 'Sorry, we could not calculate directions from' in driver.find_element_by_xpath('//div[@class="section-directions-error-primary-text"]').text:
            speak(" Sorry, we could not calculate directions ")
            return 0
    except NoSuchElementException:
        pass 
    
    
    speak(" How would you like to travel ? Car, Train, Bicycle or Flight")
    
    travel_mode = driver.find_elements_by_xpath('//div[@class="travel-mode"]')
    if len(travel_mode)==3:
        car = travel_mode[0]
        train = travel_mode[1]
        walk = travel_mode[2]
    elif len(travel_mode)>3:
        try:
            flights = travel_mode[3]
        except IndexError as exception:
            pass
    else:
        car = travel_mode[0]

    medium = takeCommand().lower()
    while True:
        if medium in ["ka","car","four wheeler","bike","auto","cab","train","trains","walk","long walk","walking","walks",
                         "flight","plane","aeroplane","flights","air","by air","via air","flying","by flying"]:
            break
        else:
            speak(" Come again please !")
            medium = takeCommand().lower()
    
    if len(travel_mode) < 3:
        car.click()
        time.sleep(3)
        try:
            element_inside_popup = driver.find_element_by_xpath('//div[@class="section-directions-trip clearfix selected"]')
            element_inside_popup.send_keys(Keys.END)
        except NoSuchElementException:
            pass
        data_detail = [] 
        for i in driver.find_elements_by_xpath('//div[@class="section-directions-trip-description"]'):
            data_detail.append(i.text)
        for i in data_detail:
            print(i)
        routes = len(data_detail)
        speak(str(routes)+" found !")
        trip_number = 1
        for i in data_detail:
            print(i.split('\n'))
            speak("Trip Number "+str(trip_number)+".")
            speak(" This trip will take around "+ i.split('\n')[0]+".")
            speak(" Total distance for this trip is "+i.split('\n')[1]+".")
            speak(" We will go through "+i.split('\n')[2])
            if len(i.split('\n')) > 3:
                content = " I have few more informations "
                for j in i.split('\n')[3:]:
                    content += j
                speak(content)
    
                      
    if medium in ["ka","car","four wheeler","bike","auto","cab"]:
        if len(travel_mode) == 3:
            car.click()
            time.sleep(3)
            try:
                element_inside_popup = driver.find_element_by_xpath('//div[@class="section-directions-trip clearfix selected"]')
                element_inside_popup.send_keys(Keys.END)
            except NoSuchElementException:
                pass
            data_detail = [] 
            for i in driver.find_elements_by_xpath('//div[@class="section-directions-trip-description"]'):
                data_detail.append(i.text)
            for i in data_detail:
                print(i)
            routes = len(data_detail)
            speak(str(routes)+" found !")
            trip_number = 1
            for i in data_detail:
                print(i.split('\n'))
                speak("Trip Number "+str(trip_number)+".")
                speak(" This trip will take around "+ i.split('\n')[0]+".")
                speak(" Total distance for this trip is "+i.split('\n')[1]+".")
                speak(" We will go through "+i.split('\n')[2])
                if len(i.split('\n')) > 3:
                    content = " I have few more informations "
                    for j in i.split('\n')[3:]:
                        content += j
                    speak(content)
                trip_number += 1
        else:
            speak(' No route found .')
    if medium in ["train","trains"]:
        if len(travel_mode) == 3:
            train.click()
            time.sleep(3)
            try:
                element_inside_popup = driver.find_element_by_xpath('//div[@class="section-directions-trip clearfix selected"]')
                element_inside_popup.send_keys(Keys.END)
            except NoSuchElementException:
                pass
            data_detail = [] 
            for i in driver.find_elements_by_xpath('//div[@class="section-directions-trip-description"]'):
                data_detail.append(i.text)
            for i in data_detail:
                print(i)
            routes = len(data_detail)
            speak(str(routes)+" found !")
            trip_number = 1
            for i in data_detail:
                print(i.split('\n'))
                speak("Trip Number "+str(trip_number)+".")
                speak(" This trip will take around "+ i.split('\n')[0]+".")
                speak(" Trip schedule is "+i.split('\n')[1]+".")
                speak(" Trains for this trip is "+i.split('\n')[2])
                if len(i.split('\n')) > 3:
                    content = " I have few more informations "
                    for j in i.split('\n')[3:]:
                        content += j
                    speak(content)
                trip_number += 1
        else:
            speak(' No route found .')
    if medium in ["walk","long walk","walking","walks"]:
        if len(travel_mode) == 3:
            walk.click()
            time.sleep(3)
            for i in driver.find_elements_by_xpath('//div[@class="section-directions-trip-description"]'):
                print(i.text.split('\n'))
                speak(" By walking, you will take around "+i.text.split('\n')[0]+".")
                speak(" Distance for this trip will be "+i.text.split('\n')[1]+".")
                speak(" Route for this trip is "+i.text.split('\n')[2]+".")
        else:
            speak(' No route found .')
    if medium in ["flight","plane","aeroplane","flights","air","by air","via air","flying","by flying"]:
        if len(travel_mode) > 3:
            flights.click()
            time.sleep(3)
            try:
                element_inside_popup = driver.find_element_by_xpath('//div[@class="section-directions-trip clearfix selected"]')
                element_inside_popup.send_keys(Keys.END)
            except NoSuchElementException:
                pass
            data_detail = [] 
            for i in driver.find_elements_by_xpath('//div[@class="section-directions-trip-description"]'):
                data_detail.append(i.text)
            for i in data_detail:
                print(i)
            routes = len(data_detail)
            speak(str(routes)+" found !")
            trip_number = 1
            for i in data_detail:
                print(i.split('\n'))
                speak("Trip Number "+str(trip_number)+".")
                trip_number += 1
            for i in data_detail:
                speak(i)
        else:
            speak(" No flight route informations .")