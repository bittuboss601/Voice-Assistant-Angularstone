def sendEmail(to, content): 
    import credentials
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 

    # Enable low security in gmail 
    server.login(credentials.email(), credentials.password()) 
    server.sendmail(credentials.email(), to, content) 
    server.close()