
from cmath import e
from re import search
from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3
from requests import delete

engine=pyttsx3.init()   
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)


def search():
    data=json.load(open('data.json'))
    word=areatoenterword.get()
    word=word.lower()
    
    if word in data:
        meaning=data[word]
        print(meaning)
        textarea.delete(1.0,END)
        
        for i in meaning:
            textarea.insert(END,u'\u2022'+i+'\n\n')
            
    elif len(get_close_matches(word,data.keys()))>0:
        close_word=get_close_matches(word,data.keys())[0]
        cword=messagebox.askyesno('Confirm','Search for '+close_word+' instead')
        
        if cword==True:
            areatoenterword.delete(0,END)
            areatoenterword.insert(END,close_word)
            meaning=data[close_word]
            textarea.delete(1.0,END)
            
            for i in meaning:
                textarea.insert(END,u'\u2022'+i+'\n\n')
                
        else:
            messagebox.showerror('Error','No such word exist, Check once again.')
            areatoenterword.delete(0,END)
            textarea.delete(1.0,END)
            
    else:
        messagebox.showinfo('Information','No such word exist.')   
        areatoenterword.delete(0,END)  
        textarea.delete(1.0,END)
        
def clear():
    areatoenterword.delete(0,END)
    textarea.delete(1.0,END)
    
def exitall():
    res=messagebox.askyesno('Confirm',"Are you sure you want to exit?")
    if res==True:
        window.destroy()
    
    else:
        pass    
    
def wordtoaudio():
    engine.say(areatoenterword.get())
    engine.runAndWait()

def listenAudio():   

    import speech_recognition
    recognizer = speech_recognition.Recognizer()

    try:

        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            areatoenterword.delete(0,END)
            areatoenterword.insert(END,text)
            
            print(f"Recognized: {text}")


    except Exception as e:
        print("Something went wrong")
        pass

def meaningaudio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()
        
        
window=Tk()
window.geometry('800x550+100+50')
window.title('Interactive Dictionary by Anuj Singh')

dcimage=PhotoImage(file='dcbg1.png')
dclabel=Label(window,image=dcimage)
dclabel.place(x=0,y=0)

enterword=Label(window,text='Enter the word:',font=('Book Antiqua',28,'bold'),fg='red',bg='#DCD5CF')
enterword.place(x=470,y=50)

areatoenterword=Entry(window,font=('arial',20,'bold'),justify=CENTER,bd=5,relief=GROOVE)
areatoenterword.place(x=450,y=100)

searchimage=PhotoImage(file="search.png")
searchbutton=Button(window,image=searchimage,bd=0,cursor='hand2',command= search,bg="#E3DAD3" )
searchbutton.place(x=490,y=145)

micimage=PhotoImage(file="microphone.png")
micbutton=Button(window,image=micimage,bd=0,cursor='hand2',command=listenAudio, bg="#E3DAD3")
micbutton.place(x=650,y=145)

result=Label(window,text='Meaning:',font=('Book Antiqua',28,'bold'),fg='red',bg='#DCD5CF')
result.place(x=520,y=230)

textarea=Text(window,width=25,height=7,font=('arial',16),bd=5,relief=GROOVE)
textarea.place(x=450,y=280)

audioimage=PhotoImage(file="C:\\Users\\rajaw\\OneDrive\\Pictures\\speaker2.png")
audiobutton=Button(window,image=audioimage,bd=0,cursor='hand2',command=meaningaudio,bg="#E3DCD6")
audiobutton.place(x=480,y=460)

clearimg=PhotoImage(file='C:\\Users\\rajaw\\OneDrive\\Pictures\\close-button.png')
clearbutton=Button(window,image=clearimg,bd=0,cursor='hand2',command=clear, bg="#E3DAD3")
clearbutton.place(x=570,y=460)

exitimage=PhotoImage(file='C:\\Users\\rajaw\\OneDrive\\Pictures\\exitbutton2.png')
exitbutton=Button(window,image=exitimage,bd=0,cursor='hand2',command=exitall, bg="#E3DAD3")
exitbutton.place(x=660,y=460)

def Enter_func(event):
    searchbutton.invoke()
window.bind('<Return>',Enter_func)


window.mainloop()