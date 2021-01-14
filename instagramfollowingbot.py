def Instagram_following_bot(driver,follow_request_command):
    driver = driver
    follow_request_command = follow_request_command
    
    search = driver.find_element_by_xpath('//input[@class = "XTCLo x3qfX "]')
    search.clear()
    search.send_keys(follow_request_command)
    time.sleep(4)
    searched_results = driver.find_elements_by_xpath('//div[@class = "fuqBx"]/a')
    pages_link = []
    for i in searched_results:
        pages_link.append(i.get_attribute('href'))
    
    COUNT = 0
    for i in pages_link:
        driver.get(i)
        time.sleep(3)
        try:
            driver.find_element_by_partial_link_text('followers').click()
        except NoSuchElementException:
            pass
        time.sleep(3)
        count = 0
        while True:
            for i in driver.find_elements_by_xpath('//div[@class="Pkbci"]/button'):
                i.click()
                time.sleep(1)
                try:
                    driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]').click()
                except NoSuchElementException as exception:
                    count += 1
                    pass
            print("Profile followed count =",count)
            element_inside_popup = driver.find_element_by_xpath('//ul[@class="jSC57  _6xe7A"]//a')
            element_inside_popup.send_keys(Keys.END)
            break_loop = False
            if takeCommand().lower() in ['stop','top','stop follow','stop following','break','exit']:
                break_loop = True
                break
            if count > 20:
                break
        if break_loop:
            speak('Exiting the follow command !')
            break
        COUNT += 1
            
        if COUNT > 3:
            break