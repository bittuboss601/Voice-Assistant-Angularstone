def searchOnNet(text):
    driver = webdriver.Chrome(executable_path = 'C:/Softwares/selenium webdriver/chromedriver')
    driver.get('https://www.google.com/')
    time.sleep(3)
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(text)
    search_box.submit()
    time.sleep(2)
    speak('Do you want to listen in detail about '+text+'?')
    if takeCommand() == 'no':
        speak(driver.find_element_by_xpath('//div[@class="IsZvec"]').text)
    else:
        driver.get(driver.find_element_by_xpath('//div[@class="yuRUbf"]/a').get_attribute('href'))
        time.sleep(2)
        for i in driver.find_elements_by_tag_name('p'):
            speak(i.text)
            if takeCommand().lower() in ["stop","stop speaking","exit","top"]:
                break
    speak('Do you want to search again on google ?')
        
    Data = takeCommand()
    time.sleep(1)
    if Data.lower() == 'yes':
        time.sleep(1)
        speak('What do you want to search for .')
        data = takeCommand()
        searchOnNet(data)
    else:
        speak('Okay Bittu Boss, thank  You for using me !')
        driver.close()