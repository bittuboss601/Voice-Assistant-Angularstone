def news():
    import news_api_key
    country_code = {'argentina':'ar','australia':'au','austria':'at','Belgium':'be','brazil':'br','bulgaria':'bg',
                   'canada':'ca','china':'cn','colombia':'co','cuba':'cu','czech republic':'cz','egypt':'eg','france':'fr',
                   'germany':'de','greece':'gr','hongkong':'hk','hungary':'hu','india':'in','indonesia':'id','ireland':'ir',
                   'israel':'il','italy':'it','japan':'jp','latvia':'lv','lithuania':'lt','malaysia':'my','mexico':'mx',
                   'morocco':'ma','netherlands':'nl','newzealand':'nz','nigeria':'ng','norway':'no','philippines':'ph',
                   'poland':'pl','portugal':'pt','romania':'ro','russia':'ru','saudi arabia':'sa','serbia':'rs','singapore':'sg',
                   'solvakia':'sk','solvenia':'si','south africa':'za','south korea':'kr','sweden':'se','switzerland':'ch',
                   'taiwan':'tw','thailand':'th','turkey':'tr','uae':'ae','ukraine':'ua','united kingdom':'gb','united states':'us',
                   'venuzuela':'ve'}
    speak("Which Country's news do you want to listen ?")
    country = takeCommand().lower()
    if country == "None":
        speak('Please come again, i did not hear .')
        country = takeCommand().lower()
    while 1:
        try:
            country = country_code[country] + '&'
            break
        except KeyError as exception:
            speak('Please come again, i did not hear .')
            country = takeCommand().lower()

    url = ('http://newsapi.org/v2/top-headlines?'
           'country='+country+
           'apiKey='+news_api_key.news_api())
    response = requests.get(url)
    data = response.json()
    for i in data['articles']:
        speak(i['title'])
        time.sleep(1)
        speak(i['description'])
        time.sleep(1)
        speak('NEXT')
        
    print(country)