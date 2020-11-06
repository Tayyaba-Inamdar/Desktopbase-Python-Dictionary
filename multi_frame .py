import Tkinter as tk
from Tkinter import *
from PyDictionary import PyDictionary
from PIL import Image, ImageTk
import tkMessageBox

dic = PyDictionary()

TITLE_FONT = ("Comic Sans MS", 40, "bold")


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, FeedBack, PageSeven, Tips,Trans):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        self.title('Smart English Doc')


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        img = Image.open('1bg.png')
        self.tkimage = ImageTk.PhotoImage(img)
        myvar=tk.Label(self,image = self.tkimage)
        myvar.place(x=0, y=10)
        myvar.pack()


        label = tk.Label(self, text="Self Access langue", font=TITLE_FONT,bg="white")
        label.pack(side="top", fill="x", pady=10)
        label.place(x=540, y=30)
        
        img = Image.open('start.png')
        self.tkstart = ImageTk.PhotoImage(img)
        button1 = tk.Button(self, text=" Lets Start ", height=50, width=300, font=('Palatino Linotype', 25,'bold'),image = self.tkstart,compound="right",
                            command=lambda: controller.show_frame("PageOne"), bg='#8C92AC')
        button1.pack()
        button1.place(x=500, y=300)

      
        img = Image.open('learn.png')
        self.tklearn = ImageTk.PhotoImage(img)
        button2 = tk.Button(self, text=" Learn lesson", height=50, width=300, font=('Palatino Linotype', 25,'bold'),image = self.tklearn,compound="left",
                            command=lambda: controller.show_frame("PageFour"), bg='#8C92AC')
        button2.pack()
        button2.place(x=500, y=400)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        img = Image.open('main_bg.png')
        self.tkimage = ImageTk.PhotoImage(img)
        myvar=tk.Label(self,image = self.tkimage)
        myvar.pack()
        myvar.place(x=0, y=0)
     
        label = tk.Label(self, text="SELF ACCESS LANGUE", font=TITLE_FONT,bg='#40E0D0',relief="solid")
        label.pack(side="top",fill='x')
       
        
        back = tk.Button(self, text="<---BACK---", font=('Gabriola', 12, 'bold'), bg='#FF55A3',
                         command=lambda: controller.show_frame("StartPage")).pack(side="top", fill="x", padx=3)

        docButton1 = tk.Button(self, text='My Doc', font=('Gabriola', 20), height=1, width=12, bg='cyan',
                               command=lambda: controller.show_frame("PageThree"))
        
        docButton2 = tk.Button(self, text='Tips', font=('Gabriola', 20),height=1, width=12, bg='cyan',
                               command=lambda: controller.show_frame("Tips"))

        docButton3 = tk.Button(self, text='About us', font=('Gabriola', 20), height=1, width=12, bg='cyan',
                               command=lambda: controller.show_frame("PageSeven"))
        img = Image.open('Dictionary.png')
        self.tkstart = ImageTk.PhotoImage(img)
        docButton4 = tk.Button(self, text='Dictionary', font=('Gabriola', 20),  bg='cyan',image = self.tkstart,compound="left",
                               command=lambda: controller.show_frame("PageSix"))
        img = Image.open('feedback.png')
        self.tkfb = ImageTk.PhotoImage(img)
        docButton5 = tk.Button(self, text='', font=('Gabriola', 20),bg='cyan',image = self.tkfb,compound="left",
                               command=lambda: controller.show_frame("FeedBack"))

        

        docButton1.pack()
        docButton1.place(x=150, y=150)
        docButton2.pack()
        docButton2.place(x=360, y=150)
        docButton3.pack()
        docButton3.place(x=570, y=150)
        docButton4.pack()
        docButton4.place(x=780, y=150)
        docButton5.pack()
        docButton5.place(x=990, y=150)
       
       
        #img = Image.open('ftre.png')
        #self.tkftre = ImageTk.PhotoImage(img)
        #label = tk.Label(self, text='F\ne\na\nt\nu\nr\ne\ns', font=("Comic Sans MS", 20, "bold"),height=300, width=15,bg='#00868B',image = self.tkftre,compound="center",)
        #label.pack()
        #label.place(x=100, y=280)

        self.image1 = tk.PhotoImage(file="images (1).gif")
        B1 = tk.Button(self, text = "* Click Here",font=('Gabriola', 20,"underline"),height=250, width=175,fg='#3F00FF',bg='#00E5EE',relief="solid",
                       command=lambda: controller.show_frame("PageTwo"),compound="center",image=self.image1)
        B1.pack()
        B1.place(x=150, y=280)
        
        self.image2 = tk.PhotoImage(file="images (2).gif")
        B2 = tk.Button(self, text="* Click Here", font=('Gabriola', 20,"underline"), height=250, width=175, fg='#3F00FF',bg='#00E5EE',relief="solid",
                       command=lambda: controller.show_frame("PageFive"),compound="center",image=self.image2)
        B2.pack()
        B2.place(x=375, y=280)
        
        self.image3 = tk.PhotoImage(file="images (3).gif")
        B3 = tk.Button(self, text="* Click Here", font=('Gabriola', 20,"underline"), height=250, width=175, fg='#3F00FF',bg='#00E5EE',relief="solid",
                        command=lambda: controller.show_frame("Trans"),compound="center",image=self.image3)
        B3.pack()
        B3.place(x=600, y=280)

        
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        img = Image.open('hie.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        myvar=tk.Label(self,image = self.tkimage)
        myvar.pack()
        myvar.place(x=0, y=0)
        
        Label(self, text="ANTONYM: ", font=("Comic Sans MS", 40, "bold"),bg='white').pack()
        
        back = Button(self, text="Home", font=('Gabriola',15,'bold'), height=1, width=72,
                      command=lambda: controller.show_frame("StartPage"), bg='#FF55A3')
        back.pack(anchor="nw")
        back.place(y=81)
        
        back = Button(self, text="<---BACK---", font=('Gabriola', 15, 'bold'),height=1, width=72,
                      command=lambda: controller.show_frame("PageOne"), bg='#FF55A3').pack(anchor="ne")

        img = Image.open('owl.jpg')
        self.tkimg = ImageTk.PhotoImage(img)
        sp = tk.Label(self, image=self.tkimg)
        sp.pack(side="right")

        Label(self, text=''' A word opposite in meaning to another.
Each word in the pair is the antithesis of the other. A word may have more than one antonym.
There are three categories of antonyms identified by the nature of the relationship between the opposed meanings.
1)two words have definitions that lie on a continuous spectrum of meaning are gradable antonyms.
2)the meanings do not lie on a continuous spectrum and the words have no other lexical relationship are complementary antonyms.
3)two meanings are opposite only within the context of their relationship are relational antonyms''', font=("Gabriola", 15),bg='white', justify=LEFT).pack()

        def evaluate(event):
            res.configure(text="Antonyms are: \n " + str(dic.antonym(e.get())))

        Label(self, text="Enter a word:", font=("Gabriola", 20), fg="red",bg="white"    ).pack()
        e = Entry(self, font=("Gabriola", 20),relief="solid")
        e.bind("<Return>", evaluate)
        e.pack()
        res = Label(self, font=("Gabriola", 15), fg="blue",bg="white",relief="solid")
        res.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        img = Image.open('main_bg.png')
        self.tkimage = ImageTk.PhotoImage(img)
        myvar=tk.Label(self,image = self.tkimage)
        myvar.pack()
        myvar.place(x=0, y=0)

        label = tk.Label(self, text="About Self Access Langue", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="<---BACK---", font=('Gabriola', 12, 'bold'), bg='#FF55A3',
                           command=lambda: controller.show_frame("PageOne")).pack(side="top", fill="x", padx=3)

       
        
        logo = tk.Label(self,
                        text='''\t Our project, Self-access langue is an desktop application,developed by using python language with the help
of active python idle which is helpful to learn grammar easily
Smart English Doc is a learning and practice grammar app designed to help improve English langue accuracy.
The app is suitable for learners it not only check the proper usage of specific words,
but will also check the spelling that you use with certain words so that they will be used in the right context.
There are certain words in the English language that change their meaning when positioned differently in a sentence.
Smart English Doc makes sure that the word you used is in its proper place so your sentence means what you want it to mean.
Smart English Doc is very useful for people who are learning the English language and can also be used as a personal tutor
to help you in your study of English grammar.\n
                              ''', font=("Gabriola", 15), justify=LEFT)
        logo.pack()

class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        img = Image.open('Chp_BG.png')
        self.tkimage = ImageTk.PhotoImage(img)
        myvar=tk.Label(self,image = self.tkimage)
        myvar.pack()
        myvar.place(x=00, y=0)

        label = tk.Label(self, text="Chapters", font=TITLE_FONT).pack(side="top", fill="x", pady=6)
        
        back = Button(self, text="<---BACK---",font=('Gabriola', 12,'bold'),
                      command=lambda: controller.show_frame("StartPage"),bg='#FF55A3').pack(side="top", fill="x", padx=3)
       
        def hello():
            tkMessageBox.showinfo("Noun", '''
        NOUN....
        A noun is a part of speech that names a person, place, thing, action.
        Nouns can be classified into two either common or proper.
        Different types of nouns such as Abstract Nouns, Collective Nouns, Compound Nouns and Concrete Nouns.
        Proper nouns refer to the individual name of a person, place or thing.\n
        EXAMPLE: Animals,birds,names,place,etc''')

        B1 = tk.Button(self, text="Chapter 1:\nNoun", command=hello, font=('Gabriola', 20), height=1, width=12, bg='cyan',
                            relief="sunken")
        B1.pack()
        B1.place(x=100, y=150)

        def hello1():
            tkMessageBox.showinfo("Pronoun", '''
        A pronoun is a word or phrase that may be substituted for a noun or noun phrase, which once replaced,is known as the pronouns antecedent.
        How is this possible?
        Its because pronouns can do everything that nouns can do. A pronoun can act as a subject,direct object, indirect object, object of the preposition, and more.''')

        B1 = tk.Button(self, text="Chapter 2:\nPronoun", command=hello1, font=('Gabriola', 20), height=1, width=12,
                       bg='cyan', relief="sunken")
        B1.pack()
        B1.place(x=350, y=150)
        def hello2():
            tkMessageBox.showinfo("Adjectives", '''Adjectives are words that describe or modify other words,
        making your writing and speaking much more specific, and a whole lot more interesting.
        Words like small, blue, and sharp are descriptive, and they are all examples of adjectives.
        Because adjectives are used to identify or quantify individual people and unique things,
        they are usually positioned before the noun or pronoun that they modify. Some sentences contain multiple adjectives''')

        B2 = tk.Button(self, text="Chapter 3:\nAdjective", command=hello2, font=('Gabriola', 20), height=1, width=12,
                            bg='cyan', relief="sunken")
        B2.pack()
        B2.place(x=580, y=150)

        def hello3():
            tkMessageBox.showinfo("Tenses", '''
        A verb-based method used to indicate the time, and sometimes the continuation or completeness,of an action or state in relation to the time of speaking.
        ORIGIN Latin tempus "time"
        Time expresses:
           past - before now
           present - now, or any time that includes now
           future - after now''')

        B3 = tk.Button(self, text="Chapter 4:\nTenses", command=hello3, font=('Gabriola', 20), height=1, width=12,
                            bg='cyan', relief="sunken")
        B3.pack()
        B3.place(x=820, y=150)

        def hello4():
            tkMessageBox.showinfo("Verbs", '''
        A verb is a "doing" word. A verb can express:
        A physical action (e.g., to swim, to write, to climb).
        A mental action (e.g., to think, to guess, to consider).
        A state of being (e.g., to be, to exist, to appear).
        The verbs that express a state of being take a little practice to spot, but, actually,
        they are the most common. The most common verb is the verb to be. Below is the verb to be in the different tenses:''')

        B4 = tk.Button(self, text="Chapter 5:\nVerbs", command=hello4, font=('Gabriola', 20), height=1, width=12,
                            bg='cyan', relief="sunken")
        B4.pack()
        B4.place(x=1060, y=150)

        def hello5():
            tkMessageBox.showinfo("Adverb", '''
        Adverbs are words like now, then, today, tomorrow and carefully.
        An adverb modifies the meaning of a verb, an adjective or another adverb. Read the following sentences:''')

        B5 = tk.Button(self, text="Chapter 6:\nAdverb", command=hello5, font=('Gabriola', 20), height=1, width=12,
                            bg='cyan', relief="sunken")
        B5.pack()
        B5.place(x=100, y=250)

        def hello6():
            tkMessageBox.showinfo("Phrases", ''' A phrase may be any group of words, often carrying a special idiomatic meaning;
        in this sense it is roughly synonymous with expression. In linguistic analysis, a phrase is a group of words (or possibly a single word)
        that functions as a constituent in the syntax of a sentence, a single unit within a grammatical hierarchy.
        A phrase typically appears within a clause, but it is possible also for a phrase to be a clause or to contain a clause within it.''')

        B6 = tk.Button(self, text="Chapter 7:\nPhrases", command=hello5, font=('Gabriola', 20), height=1, width=12,
                            bg='cyan', relief="sunken")
        B6.pack()
        B6.place(x=100, y=350)

        def hello7():
            tkMessageBox.showinfo("Antonyms", ''' An antonym is a word that means the opposite of another word. For instance, the antonym of 'hot' may be 'cold.'
        The root words for the word 'antonym' are the words 'anti,' meaning 'against' or 'opposite,' and 'onym,' meaning 'name.' . ''')

        B7 = tk.Button(self, text="Chapter 8:\nAntonyms", command=hello7, font=('Gabriola', 20), height=1, width=12,
                            bg='cyan', relief="sunken")
        B7.pack()
        B7.place(x=1060, y=250)

        def hello8():
            tkMessageBox.showinfo("Synonyms", ''' A synonym is a word that has a similar meaning to or exactly the same meaning as another word.
        Synonyms and antonyms are exactly the opposite.  ''')

        B8 = tk.Button(self, text="Chapter 9:\nSynonyms", command=hello8, font=('Gabriola', 20), height=1, width=12,
                            bg='cyan', relief="sunken")
        B8.pack()
        B8.place(x=1060, y=350)

       
        def hello9():
            tkMessageBox.showinfo("Meaning",
                                  ''' . Something that is conveyed or intended, especially by language; sense or significance:  ''')

        B9 = tk.Button(self, text="Chapter 11:\nMeaning", command=hello9, font=('Gabriola', 20), height=1, width=12,
                             bg='cyan', relief="sunken")
        B9.pack()
        B9.place(x=1060, y=450)


class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        img = Image.open('hie.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        myvar=tk.Label(self,image = self.tkimage)
        myvar.pack()
        myvar.place(x=0, y=0)
        
        Label(self, text="SYNONYMS: ", font=("Comic Sans MS", 40, "bold"),bg='white').pack()
        back = Button(self, text="Home", font=('Gabriola',15,'bold'), height=1, width=72,
                      command=lambda: controller.show_frame("StartPage"), bg='#FF55A3')
        back.pack(anchor="nw")
        back.place(y=81)
        
        back = Button(self, text="<---BACK---", font=('Gabriola', 15, 'bold'),height=1, width=72,
                      command=lambda: controller.show_frame("PageOne"), bg='#FF55A3').pack(anchor="ne")

        img = Image.open('synonyms.jpg')
        self.tkimgsp = ImageTk.PhotoImage(img)
        sp = tk.Label(self, image=self.tkimgsp)
        sp.pack(side="right")


        def evaluate(event):
            res.configure(text="Synonym are: \n  " + str(dic.synonym(e.get())))

        Label(self, text=''' A word or phrase that means exactly or nearly
the same as another word or phrase in the same language.
An example of synonyms are the words begin, start, commence, and initiate.
Words can be synonymous when meant in certain senses, even if they are not synonymous in all of their senses.
For example, if one talks about a long time or an extended time,
long and extended are synonymous within that context.''', font=("Gabriola", 15),bg='white',justify=LEFT).pack()

        Label(self, text="Enter a word:", font=("Gabriola", 20), fg="red",bg='white').pack()
        e = Entry(self, font=("Gabriola", 20),relief="solid")
        e.bind("<Return>", evaluate)
        e.pack()
        res = Label(self, font=("Gabriola", 15), fg="blue",relief="solid")
        res.pack()


class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        img = Image.open('hie.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        myvar=tk.Label(self,image = self.tkimage)
        myvar.pack()
        myvar.place(x=0, y=0)

        Label(self, text="MEANINGS: ", font=("Comic Sans MS", 40, "bold"),bg='white').pack()

        back = Button(self, text="Home", font=('Gabriola',15,'bold'), height=1, width=72,
                      command=lambda: controller.show_frame("StartPage"), bg='#FF55A3')
        back.pack(anchor="nw")
        back.place(y=81)
        
        back = Button(self, text="<---BACK---", font=('Gabriola', 15, 'bold'),height=1, width=72,
                      command=lambda: controller.show_frame("PageOne"), bg='#FF55A3').pack(anchor="ne")
        
        def evaluate(event):
            res.configure(text="Meanings are: \n  " + str(dic.meaning(e.get())))

        Label(self, text='''A word or phrase that means exactly or nearly
the same as another word or phrase in the same language.''', font=("Gabriola", 15),bg='white', justify=LEFT).pack()

        Label(self, text="Enter a word:", font=("Gabriola", 20), fg="red",bg='white').pack()
        e = Entry(self, font=("Gabriola", 20),relief="solid")
        e.bind("<Return>", evaluate)
        e.pack()
        res = Label(self, font=("Gabriola", 15), fg="blue", wraplength=900)
        res.pack()
        
class Trans(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        img = Image.open('hie.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        myvar=tk.Label(self,image = self.tkimage)
        myvar.pack()
        myvar.place(x=0, y=0)
        
        Label(self, text="TRANSLATE: ", font=("Comic Sans MS", 40, "bold"),bg='white').pack()
        back = Button(self, text="Home", font=('Gabriola',15,'bold'), height=1, width=75,
                      command=lambda: controller.show_frame("StartPage"), bg='#FF55A3')
        back.pack(anchor="nw")
        back.place(y=81)
        
        back = Button(self, text="<---BACK---", font=('Gabriola', 15, 'bold'),height=1, width=72,
                      command=lambda: controller.show_frame("PageOne"), bg='#FF55A3').pack(anchor="ne")
        
        def evaluate(event):
            res.configure(text = "Translation is:\n " + str(dic.translate(word , lan)))
        Label(self, text="Enter a word and press enter:",font=("Gabriola", 20), fg="red",bg="white").pack()
        e = Entry(self,font=("Gabriola", 20),relief="solid")
        e1 = Entry(self,font=("Gabriola", 20),relief="solid")
        word=e.get()
        lan=e1.get()
        e.bind("<Return>",evaluate)
        e1.bind("<Return>",evaluate)
        e.pack()
        e1.pack()
        res = Label(self, font=("Gabriola", 15), fg="blue", wraplength=900)
        res.pack()


class FeedBack(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        img = Image.open('feedback.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        myvar=tk.Label(self,image = self.tkimage)
        myvar.pack()
        myvar.place(x=00, y=0)  

        def changeLabel():
            name = ("Thank you " + T.get()+ " for completing feedback form.\n Your Feedback helps us understand what \n we do well and where we can improve")
            labelText.set(name)
            T.delete(0, END)
            T.insert(0, " ")
            T1.delete(0, END)
            T1.insert(0, " ")
            T2.delete(0, END)
            T2.insert(0, " ")
            return
        
        logo = Label(self, text='Send us your Feedback', font=("Comic Sans MS", 40, "bold")).pack()

        back = Button(self, text="<---BACK---", font=('Gabriola', 12, 'bold'), bg='#FF55A3',
                      command=lambda: controller.show_frame("PageOne")).pack(side="top", fill="x", padx=3)

        img0 = Image.open('home.png')
        self.tkimg0 = ImageTk.PhotoImage(img0)
        back = Button(self, text="", font=('Gabriola', 12, 'bold'), image=self.tkimg0, compound="center",
                      command=lambda: controller.show_frame("StartPage"), bg='#FF55A3')
        back.place(x=5, y=0)
        
        img1 = Image.open('name_icon.gif')
        self.tkimg = ImageTk.PhotoImage(img1)
        logo = Label(self, text=' Name:', font=("Gabriola", 18, 'bold'),height=30,width=200,image = self.tkimg,compound="left",bg='white').place(x=250, y=150)
        T = Entry(self, font=("Gabriola",20),width=30)
        T.pack()
        T.place(x=200, y=185)

        img2 = Image.open('Email.png')
        self.tkimgem = ImageTk.PhotoImage(img2)
        logo = Label(self, text=' Em@il:', font=("Gabriola", 18, 'bold'),height=30,width=200,image = self.tkimgem,compound="left",bg='white').place(x=650, y=150)
        T1 = Entry(self, font=("Gabriola",20),width=30)
        T1.pack()
        T1.place(x=600, y=185)

        img3 = Image.open('comments.png')
        self.tkcmnt = ImageTk.PhotoImage(img3)
        logo = Label(self, text='Your Comments:', font=("Gabriola",18,'bold'),height=30,width=200,image = self.tkcmnt,compound="left",bg='white').place(x=250, y=270)
        T2 = Entry(self, font=("Gabriola",20),width=30)
        T2.pack()
        T2.place(x=450, y=260)

        # radio buttons
        w = Label(self, text="Rate Our Application ", font=("Gabriola", 18, 'bold'))
        w.pack()
        w.place(x=500, y=350)
        v = IntVar()

        imgr = Image.open('r.png')
        self.r = ImageTk.PhotoImage(imgr)
        r = Radiobutton(self,image = self.r,compound="bottom",font=("Gabriola"), variable=v, value=1)
        r.pack()
        r.place(x=435, y=390)

        imgr1 = Image.open('r1.png')
        self.r1 = ImageTk.PhotoImage(imgr1)
        r1 = Radiobutton(self,image = self.r1,font=("Gabriola"),  variable=v, value=2)
        r1.pack()
        r1.place(x=500, y=390)

        imgr2 = Image.open('r2.png')
        self.r2 = ImageTk.PhotoImage(imgr2)
        r2 = Radiobutton(self,image = self.r2,font=("Gabriola"),  variable=v, value=3)
        r2.pack()
        r2.place(x=565, y=390)

        imgr3 = Image.open('r3.png')
        self.r3 = ImageTk.PhotoImage(imgr3)
        r3 = Radiobutton(self,image = self.r3,font=("Gabriola"),  variable=v, value=4)
        r3.pack()
        r3.place(x=630, y=390)
        
        labelText = tk.StringVar()
        labelText.set("Thank You")
        label1 = tk.Label(self, textvariable=labelText, height=3,width=60,font=("Gabriola", 18),relief="groove")
        label1.pack()
        label1.place(x=350, y=450)
        
        
        docButton = Button(self, text='Submit', font=('Gabriola',15,'bold'), height=1, width=30, relief=RAISED,command=changeLabel)
        docButton.place(x=550, y=600)


class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        img = Image.open('main_bg.png')
        self.tkimage = ImageTk.PhotoImage(img)
        myvar=tk.Label(self,image = self.tkimage)
        myvar.pack()
        myvar.place(x=0, y=0)

        img = Image.open('MTT.png')
        self.tkteam = ImageTk.PhotoImage(img) 
        logo = Label(self, text='Our Team...!!!', font=("Comic Sans MS", 35, "bold"),image = self.tkteam)
        logo.pack()
        logo.place(x=175,y=0)
        
        img = Image.open('home.png')
        self.tkimgo = ImageTk.PhotoImage(img)
        back = Button(self, text="", font=('Gabriola', 12, 'bold'), image=self.tkimgo, compound="center",
                      command=lambda: controller.show_frame("StartPage"), bg='#FF55A3')
        back.place(x=5, y=0)

        back = Button(self, text="<---BACK---", font=('Gabriola', 12, 'bold'),
                      command=lambda: controller.show_frame("PageOne"), bg='#FF55A3').pack(anchor='e')

        def changeLabel():
           
            name = ('''ANSARI AIMAN SABA QAIYYUM\nbelongs to Computer department of A.R.Kalsekar Polytechnic.
Aiman Saba is the leader of our group. She has done the coding of our Application.
Email ID:ellisworn123@gmail.com
Contact:8767088772''')
            labelText.set(name)

        def changeLabel1():
           
            name = ('''INAMDAR TAYYABA HAMID
belongs to Computer department of A.R.Kalsekar Polytechnic.
Tayyaba is the team member of this group
She has done the coding and also supported the GUI coding of our Application.
Email ID:inamdartayyaba@gmail.com
Contact:8291702227''')
            labelText.set(name)

        def changeLabel2():
           
            name = ('''FANGARI IRAM RIYAZ
belongs to Computer department of A.R.Kalsekar Polytechnic.
Iram is the team member of this group
She has done the GUI design and also supported in the GUI coding of our Application.
Email ID:iramfangari2@gmail.com
Contact:8691902129''')
            labelText.set(name)

        def changeLabel3():
           
            name = ('''HAKIM RIMSHA ALLABAKSH
belongs to Computer department of A.R.Kalsekar Polytechnic.
Iram is the team member of this group
She has done the Documentation and also supported in the GUI designing of our Application.
Email ID:rimsha.hakim@gmail.com
Contact:8652593993''')
            labelText.set(name)

        labelText = tk.StringVar()
        labelText.set("Details..")
        label1 = tk.Label(self, textvariable=labelText,font=('Gabriola', 18),relief="solid",wraplength=500,justify="left")
        label1.pack()
        label1.place(x=800, y=125)

        img1 = Image.open('p_amn.png')
        self.tkimag = ImageTk.PhotoImage(img1)
        docButton = Button(self, text='ANSARI AIMAN SABA ',height=250, width=200, font=('Gabriola', 15),  relief=RAISED,
                           command=changeLabel,image = self.tkimag,compound="top")
        docButton.pack()
        docButton.place(x=100, y=125)
        
        img2 = Image.open('p_tabz.png')
        self.tkimg = ImageTk.PhotoImage(img2)
        docButton = Button(self, text='INAMDAR TAYYABA', height=250, width=200, font=('Gabriola', 15),  relief=RAISED,
                           command=changeLabel1,image = self.tkimg,compound="top")
        docButton.pack()
        docButton.place(x=340, y=125)

        img3 = Image.open('p_amn.png')
        self.tkimg3 = ImageTk.PhotoImage(img3)
        docButton = Button(self, text='FANGARI IRAM', font=('Gabriola', 15),  relief=RAISED,
                           command=changeLabel2,image = self.tkimg3,compound="top")
        docButton.pack()
        docButton.place(x=100, y=405)
        
        img4 = Image.open('p_amn.png')
        self.tkimg4 = ImageTk.PhotoImage(img4)
        docButton = Button(self, text='HAKIM RIMSHA', font=('Gabriola', 15),  relief=RAISED,
                           command=changeLabel3,image = self.tkimg4,compound="top")
        docButton.pack()
        docButton.place(x=340, y=405)

class Tips(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        logo = Label(self, text='Tips and Tricks to memorise', font=("Comic Sans MS", 40, "bold")).pack()
        back = Button(self, text="<---BACK---", font=('Gabriola', 12, 'bold'),
                      command=lambda: controller.show_frame("PageOne"), bg='#FF55A3').pack(side="top", fill="x", padx=3)
       
        img = Image.open('home.png')
        self.tkimg = ImageTk.PhotoImage(img)
        back = Button(self, text="", font=('Gabriola', 12, 'bold'), image=self.tkimg, compound="center",
                      command=lambda: controller.show_frame("StartPage"), bg='#FF55A3')
        back.place(x=5, y=0)

        Tips = Label(self, text='''Note:There is no shortcut for learning grammatically correct English.
It takes time to understand and put to use the rules of English grammar.
But, there are ways to remember the grammar to help you speak correctly.''', font=("Gabriola", 15),fg='#CF1020',justify='left').pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
