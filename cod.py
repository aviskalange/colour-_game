import tkinter
import random

timeleft=30
score=0
colours=['Green','Red','Blue','Yellow','Orange','Purple','Black','White']

def start(event):
	countdown()
	nextcolour()

def nextcolour():
	global timeleft
	global score
	if timeleft>0:
		if e.get().lower() == colours[0].lower():
			score+=1
		e.delete(0,tkinter.END)
		random.shuffle(colours)
		txt.config(fg=colours[0],text=colours[1])
		scorelabel.config(text="Score : "+str(score))

def countdown():
	global timeleft
	if timeleft>0:
		timeleft-=1
		timelabel.config(text="Time Left : "+str(timeleft))
		
	else:
		timelabel.config(text="Game Over")

root=tkinter.Tk()
root.title("Color Game")
root.geometry("600x400")

instruction=tkinter.Label(root,text="Name the colour in which the text appears and earn some points",font=("Times New Roman",13))
instruction.pack()

scorelabel=tkinter.Label(root,text="Press Enter to Start the Game",font=("Times New Roman",13))
scorelabel.pack()

timelabel=tkinter.Label(root,text="Time Left : "+str(timeleft),font=("Times New Roman",13))
timelabel.pack()

txt=tkinter.Label(root,font=("Times New Roman",20))
txt.pack()

e=tkinter.Entry(root)
e.pack()

root.bind('<Return>',start)

button=tkinter.Button(root,text="Exit",command=root.destroy)
button.pack()
e.focus_set()
root.mainloop()
