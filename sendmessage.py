def send_message():
    import twilio_token
    import twilio_sid
    contacts = {'nitin':'+919304186750','bittu':'+919934093299'}
    speak('Whom do you want to send message ?')
    nmbr = takeCommand().lower()
    while 1:
        try:
            contact_nmbr = contacts[nmbr]
            break
        except KeyError as exception:
            speak('Please come again, i did not hear .')
            nmbr = takeCommand().lower()
    print(contact_nmbr)
    account_sid = twilio_sid.twilio_sid()
    auth_token = twilio_token.twilio_token()
    client = Client(account_sid, auth_token) 
    speak('Please, convey your message')
    client.messages.create(to=contact_nmbr, 
                       from_="+12566662076", 
                       body=takeCommand())