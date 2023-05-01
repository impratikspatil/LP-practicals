import datetime
import wikipedia
import webbrowser
import os


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")   

    else:
        print("Good Evening!")  
     



if _name_ == "_main_":
    wishMe()
    while True:
        print("Please tell me how may I help you")
        query = input()
    # if 1:
        query = query.lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"The time is {strTime}")

        elif 'what is your name' in query:
            print("My name is Ybhav")

        elif 'how are you?' in query:
            print("I am fine, Thank you")

        elif 'who made you?' in query:
            print("I was built by Ybhav")

        elif 'open code' in query:
            codePath = "C:\\Users\\Ybhav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        else:
            print("I am sorry, I am not able to understand you")