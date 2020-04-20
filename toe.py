from tkinter import *
from tkinter import messagebox
import random as r
def button(frame):          #Function to define a button
    b=Button(frame,padx=1,bg="papaya whip",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b
def change_a():             #Function to change the operand for the next player
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break
def reset():                #Resets the game
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])
def check():                #Checks for victory or Draw
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Congrats!!","'"+a+"' has won")
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats!!","'"+a+"' has won")
        reset()   
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()
	
def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')
        
def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_a()
        labelp.config(text=a+"'s Chance")
	
	
def f1():
	root.withdraw()
	w.deiconify()
def f2():
	w.withdraw()
	root.deiconify()

###############   Main Program #################
root=Tk()                   #Window defined
root.title("Tic-Tac-Toe")   #Title given
root.geometry("400x400+200+100")
root.configure(background='MediumOrchid1')
lblwt=Label(root,text="WELCOME",width=10,font=("arial",16,'bold'),bg='#FFF0F5')
btnplay=Button(root,text="PLAY",width=10,font=("arial",16,'bold'),command=f1)
lblwt.pack(pady=10)
btnplay.pack(pady=10)
	
w=Toplevel(root)
w.title("TIC TOE")
w.configure(background='MediumOrchid1')
a=r.choice(['O','X'])       #Two operators defined
colour={'O':"deep sky blue",'X':"lawn green"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(w))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)


labelp=Label(w,text=a+"'s Chance",font=('arial',20,'bold'))
labelp.grid(row=3,column=0,columnspan=3)



def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        w.destroy()

w.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()