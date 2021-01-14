# Voice-Assistant-Angularstone
Angularstone is a voice assistant which takes user's voice commands as input and perform some NLP operations then respond accordingly. There are many existing technologies which exhibit the similar feature. But, it has something different to flaunt. Angularstone can get access to Instagram(currently) and other social media platforms like Facebook, Twitter and many more. You can add these platforms easily. And the most important thing about this is, it is cheap.  Yeah ! Go and check out these.

**NOTE:-** 
1)     In functions, I have used chrome webdriver. And for that I need to specify my chromedriver address in variable "executable_path". So change your path accordingly in              functions.
2)     Download chrome driver according to your chrome version. https://chromedriver.chromium.org/
3)     Install all the Python Libraries mentioned in libraries file.
4)     Go and check out following function and place your own credentials or file addresses.
       a) wake() - Add address of your mp3 file.
       b) In credentials.py file, please mention your gmail username & password. For security reasons create dummy gmail account with least security.
       c) searchOnNet() - Write own chromedriver executable path
       d) youtube() - Write own chromedriver executable path
       e) In news_api_key.py file write your own key from http://newsapi.org/v2/
       f) In weather_api.py file write your own key from openweather api
       g) In twilio_token.py & twilio_sid.py get your own twilio credentials and place them in both files as instructed.
       h) locate() - Write own chromedriver executable path
       i) navigation() - Write own chromedriver executable path
       j) Instagram() - Write own chromedriver executable path
       l) In insta_credentials.py file write your own Instagram account credentials.
       m) In wolframa_alpha.py file get your own wolframa api key from official website
       n) In DRIVER PROGRAM.py file change music directory address, replace email address with your own & change the commands accordingly else okay.

### Functions Used :-

**wake()** is used to initiate the program.
If mike detects **None** then this function returns False or vice-versa.

**speak()** uses pyttsx3 speech engine to generate audible voices.
Which is actually a string converted into audio.

**wishMe()** analyze current time and then send greetings to **speak()** 

**takeCommand()** uses Recognizer object to detect voice through microphone.

**sendEmail()** takes two parameters *email* and *content* then create **SMTP** connection using port **587**

**getDate()** returns the current date in a string:-

**searchOnNet()** takes one argument and perform google search.

When results load then this function asks user for **brief** or **detailed information**
If user's command is for brief then it simply read brief info.
If user asks for detailed information then it read the whole webpage.
After completing the above process, this function asks user for another search if user says **yes** then it perform recursion and repeat the above process else, exit.

**listening_algorithm()** takes two arguments **to** and **from**. It returns the most probable string from list of strings contained in **from_** which is similar to **to**.

**youtube()** takes text as arguement and open youtube.com, locate textbox and submit button. Then search text and read the first ten search results and print it on display. 
This function asks user to play which song from the given playlist. Then send text and playlist to **listening_algorithm()** and from the returned value play the song.
It can also perform **stop**, **next**, **skip_Ad** function on youtube.

**time_()** returns current time in a string

**news()** asks user **country** name to read news

**Weather_Search()** asks user **address** to read current weather condition

**send_message()** asks user whom to send message. Then ask user to convey the message and then send text message.
**Note:-** To use this functionality receiver's contact number must be registered with twillio.

**locate()** asks user the **address** where to locate and then asks for what to locate in that address.
After that it suggest good rating search results and speak their **contacts** and **address** when being asked .

**navigation()** asks user the **source** and **Destination** address then ask about the transporation system then
speak the time,date,kilometers and some important note regarding the journey if it is available.

**Instagram_scroller()** scrolls instagram

**Instagram_following_bot()** send follow request based on command

**Instagram()** controls and perform different actions on Instagram like send message,read notifications,open explorer,play stories.


