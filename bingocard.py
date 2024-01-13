import tkinter
import random

words=('Hello','come','kome','peg')
word=random.choice(words)

root=tkinter.Tk()
cvs = tkinter.Canvas(width=506,height=506)
cvs.pack()
cvs.create_line(5,5,5,505,fill="black",width=5)
cvs.create_line(105,5,105,505,fill="black",width=5)
cvs.create_line(205,5,205,505,fill="black",width=5)
cvs.create_line(305,5,305,505,fill="black",width=5)
cvs.create_line(405,5,405,505,fill="black",width=5)
cvs.create_line(505,5,505,505,fill="black",width=5)

cvs.create_line(5,5,505,5,fill="black",width=5)
cvs.create_line(5,105,505,105,fill="black",width=5)
cvs.create_line(5,205,505,205,fill="black",width=5)
cvs.create_line(5,305,505,305,fill="black",width=5)
cvs.create_line(5,405,505,405,fill="black",width=5)
cvs.create_line(5,505,505,505,fill="black",width=5)



cvs.create_text(55,55,text=word,fill="black",font=("System",10))
cvs.create_text(155,55,text="help",fill="black",font=("System",10))
cvs.create_text(255,55,text="help",fill="black",font=("System",10))
cvs.create_text(355,55,text="help",fill="black",font=("System",10))
cvs.create_text(455,55,text="help",fill="black",font=("System",10))

cvs.create_text(55,155,text=word,fill="black",font=("System",10))
cvs.create_text(155,155,text="help",fill="black",font=("System",10))
cvs.create_text(255,155,text="help",fill="black",font=("System",10))
cvs.create_text(355,155,text="help",fill="black",font=("System",10))
cvs.create_text(455,155,text="help",fill="black",font=("System",10))

cvs.create_text(55,255,text="help",fill="black",font=("System",10))
cvs.create_text(155,255,text="help",fill="black",font=("System",10))
cvs.create_text(255,255,text="help",fill="black",font=("System",10))
cvs.create_text(355,255,text="help",fill="black",font=("System",10))
cvs.create_text(455,255,text="help",fill="black",font=("System",10))

cvs.create_text(55,355,text="help",fill="black",font=("System",10))
cvs.create_text(155,355,text="help",fill="black",font=("System",10))
cvs.create_text(255,355,text="help",fill="black",font=("System",10))
cvs.create_text(355,355,text="help",fill="black",font=("System",10))
cvs.create_text(455,355,text="help",fill="black",font=("System",10))

cvs.create_text(55,455,text="help",fill="black",font=("System",10))
cvs.create_text(155,455,text="help",fill="black",font=("System",10))
cvs.create_text(255,455,text="help",fill="black",font=("System",10))
cvs.create_text(355,455,text="help",fill="black",font=("System",10))
cvs.create_text(455,455,text="help",fill="black",font=("System",10))
root.mainloop()
