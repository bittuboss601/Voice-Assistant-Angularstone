def Weather_Search():
    import weather_api
    speak('City name')
    q = takeCommand()
    while True:
        if q != "None":
            break
        else:
            speak('Come again please !')
            q = takeCommand()
    speak('State or Country name')
    q2 = takeCommand()
    while True:
        if q2 != "None":
            break
        else:
            speak('Come again please !')
            q2 = takeCommand()
    
    q += ',' + q2
    
    url = "https://community-open-weather-map.p.rapidapi.com/find"

    querystring = {"type":"link%2C accurate","units":"imperial%2C metric","q":q}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': weather_api.weather_key()
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    search_result = json.loads(response.text)
    return search_result