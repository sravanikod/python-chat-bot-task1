import pyttsx3
import os
import cv2

print("hello, what do you want me to do for you?")

pyttsx3.speak("hello, what do you want me to do for you?")





while True:
    def socialmedia():
        while True:
            print("please type the social media you want to open")
            pyttsx3.speak("please type the social media you want to get into")
            search=input()
            os.system(" chrome {}{}".format(search,".com"))
            print("would you like to open another social media?")
            pyttsx3.speak("would you like to open another social media?")
            print("1.yes             2.no")
            website_name=int(input())
            if website_name==1:
                continue
            else :
                break
            
            
                  
                    
                
                    
    def application():
        while True:
            print("Which application do you want me to launch?")
            pyttsx3.speak("which application do you want me to launch?")
            app=input()
            os.system("{}".format(app))
            print("would you like to open another application?")
            pyttsx3.speak("would you like to open another application?")
            print("1.yes           2.no")
            app_name=int(input())
          
            if app_name==1 :
                continue
            else :
                break
            
            
    def capture():
        while True:
            print("get ready for the shot we are capturing ")

    
            cap=cv2.VideoCapture(0)
            status,photo=cap.read()
            cv2.imshow("here is your pic",photo)
            pyttsx3.speak("your pic has been captured check it out")
            cv2.waitKey()
            cv2.destroyAllWindows()
            cap.release()
            print("would you like to capture another pic?")
            pyttsx3.speak("would you like to capture another pic?")
            print("1.yes           2.no")
            captureagain=int(input())
        
            if captureagain==1 :
                continue
            else :
                break
       
        
    def spotify():
        print("sure opening spotify")
        os.system("chrome https://open.spotify.com/search" )
        
    
    
    
    print("please type \"help\"  to know what i can do ")
    pyttsx3.speak("please type help to know what i can do" )
    p=input()
    if ("help" in p):
        print("1. open social media")
        print("2. run system application")
        print("3. capture your pic")
        print("4. listen music on spotify")
        print("select any of the following to get started")
        pyttsx3.speak("select any of the following to get started")
    i=int(input())
    
    if i==1 :
         socialmedia()
         print("do you want to continue ? please select any number")
         pyttsx3.speak("do you want to continue ? please select any number")
         print("1.Yes,continue               2.No,exit")
         
         ce=int(input())
         if ce==1 :
             continue
         else :
             break
             
    
    elif i==2 :
        
        application()
        print("do you want to continue ? please select any number")
        pyttsx3.speak("do you want to continue ? please select any number")
        print("1.Yes,continue               2.No,exit")
        ce=int(input())
        if ce==1 :
             continue
        else :
             break
    
    
    elif i==3 :
        
        capture()
        print("do you want to continue ? please select any number")
        pyttsx3.speak("do you want to continue ? please select any number")
        print("1.Yes,continue               2.No,exit")
        ce=int(input())
        
        if ce==1 :
            continue
        else :
            break
        
    elif i==4 :
        
        spotify()
        
        print("do you want to continue ? please select any number")
        pyttsx3.speak("do you want to continue ? please select any number")
        print("1.Yes,continue               2.No,exit")
        ce=int(input())
        if ce==1 :
            continue
        else :
            break

pyttsx3.speak("See you later,bye for now!!")





    
    



   


