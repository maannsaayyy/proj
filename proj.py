from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import*
import bs4
import requests
import socket
import requests

class NegativeRnoException(Exception):
	def __init__(self,rno):
		pass

def f1():
	root.withdraw()
	adst.deiconify()
def f2():
	adst.withdraw()
	root.deiconify()
def f4():
	vist.withdraw()
	root.deiconify()
def f3():
	stdata.delete(1.0,END)
	root.withdraw()
	vist.deiconify()
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select rno,name,mks from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg=msg+"rno="+str(d[0])+ "  name="+str(d[1])+  " mks="+str(d[2]) +"\n"
		stdata.insert(INSERT,msg)
	except DatabaseError as e:
		messagebox.showerror("invalid",e)
	finally:
		if con is not None:
			con.close()
def f5():
	con=None
	try:
		con=connect("system/abc123")
		rno=int(entAddRno.get())
		name=entAddName.get()
		mks=int(entAddMks.get())
		cursor=con.cursor()
		sql="insert into students values ('%d','%s','%d')"
		args=(rno,name,mks)
		if name.isalpha():
			cursor.execute(sql %args)
			con.commit()
			msg=str(cursor.rowcount)+ "record inserted"
			messagebox.showinfo("correct",msg)
			entAddRno.delete(0,END)
			entAddName.delete(0,END)
			entAddMks.delete(0,END)
			entAddRno.focus()
		else:
			messagebox.showerror("invalid name")
			entAddRno.delete(0,END)
			entAddName.delete(0,END)
			entAddMks.delete(0,END)
			entAddRno.focus()
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("invalid",e)
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddMks.delete(0,END)
		entAddRno.focus()
		
	finally:
		if con is not None:
			con.close()
def f6():
	root.withdraw()
	upst.deiconify()
def f7():
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="update students set name='%s',mks='%d' where rno='%d'"
		name=entUpdateName.get()
		mks=int(entUpdateMks.get())
		rno=int(entUpdateRno.get())
		args=(name,mks,rno)
			
		if name.isalpha():
			cursor.execute(sql % args)
			con.commit()
			msg=str(cursor.rowcount)+ "record updated"
			messagebox.showinfo("correct",msg)
			entUpdateRno.delete(0,END)
			entUpdateName.delete(0,END)
			entUpdateMks.delete(0,END)
			entUpdateRno.focus()
		else:
			messagebox.showerror("invalid name")
			entUpdateRno.delete(0,END)
			entUpdateName.delete(0,END)
			entUpdateMks.delete(0,END)
			entUpdateRno.focus()
		
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("invalid",e)
		entUpdateRno.delete(0,END)
		entUpdateName.delete(0,END)
		entUpdateMks.delete(0,END)
		entUpdateRno.focus()
	finally:
		if con is not None:
			con.close()
def f8():
	upst.withdraw()
	root.deiconify()
def f9():
	root.withdraw()
	delst.deiconify()
def f10():
	delst.withdraw()
	root.deiconify()
def f11():
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="delete from students where rno='%d'"
		rno=int(entDeleteRno.get())
		args=(rno)
		if rno<0:
			raise NegativeRnoException("Rno cannot be negative")
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+ "record deleted"
		messagebox.showinfo("correct",msg)
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
		
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("invalid",e)
	except NegativeRnoException as e:
		messagebox.showerror("Wrong",e)
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
	except ValueError as e:
		con.rollback()
		msg="Integer only"
		messagebox.showerror("invalid",msg)
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
	finally:
		if con is not None:
			con.close()
			

			
	

root=Tk()
root.title("S.M.S")
root.geometry("800x500+300+100")
root.configure(background='indianred1')

res=requests.get("https://www.brainyquote.com/quote_of_the_day.html")

soup=bs4.BeautifulSoup(res.text,'lxml')

quote=soup.find('img',{"class":"p-qotd"})

text=quote['alt']
lblText=Label(root,text=text,font=("arial",10,'bold'))
lblText.pack(pady=10)

try:
	city='mumbai'
	socket.create_connection(("www.google.com",80))
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+city
	a3="&appid=c6e315d09197cec231495138183954bd"
	api_address= a1 + a2 + a3
	res1=requests.get(api_address)
	data=res1.json()
	temp=data['main']['temp']
	lblTemp=Label(root,text='temperature',font=("arial",16,'bold'))
	lblText=Label(root,text=temp,font=("arial",16,'bold'))
	lblTemp.pack(pady=10)
	lblText.pack(pady=10)
	

except OSError:
	messagebox.showerror("check network")



btnAdd=Button(root,text="Add",width=10,font=("arial",16,'bold'),bg='#ADD8E6',command=f1)
btnView=Button(root,text="View",width=10,font=("arial",16,'bold'),bg='#ADD8E6',command=f3)
btnUpdate=Button(root,text="Update",width=10,font=("arial",16,'bold'),bg='#ADD8E6',command=f6)
btnDelete=Button(root,text="Delete",width=10,font=("arial",16,'bold'),bg='#ADD8E6',command=f9)

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)

#Add

adst=Toplevel(root)
adst.title("Add Stu.")
adst.geometry("500x500+300+100")
adst.configure(background='coral1')
adst.withdraw()

lblAddRno=Label(adst,text="Enter Rno",font=("arial",16,'bold'))
lblAddName=Label(adst,text="Enter Name",font=("arial",16,'bold'))
lblAddMks=Label(adst,text="Enter Marks",font=("arial",16,'bold'))
entAddRno=Entry(adst,bd=5,font=("arial",16,'bold'))
entAddName=Entry(adst,bd=5,font=("arial",16,'bold'))
entAddMks=Entry(adst,bd=5,font=("arial",16,'bold'))
btnAddSave=Button(adst,text="Save",font=("arial",16,'bold'),command=f5)
btnAddBack=Button(adst,text="Back",font=("arial",16,'bold'),command=f2)

lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
lblAddMks.pack(pady=10)
entAddMks.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)

#view
vist=Toplevel(root)
vist.title("View Stu.")
vist.geometry("500x500+300+100")
vist.configure(background='mediumpurple1')
vist.withdraw()

stdata=scrolledtext.ScrolledText(vist,width=40,height=20)
btnViewBack=Button(vist,text='Back',font=("arial",16,'bold'),command=f4)

stdata.pack(pady=10)
btnViewBack.pack(pady=10)

#update
upst=Toplevel(root)
upst.title("Update Stu.")
upst.geometry("500x500+300+100")
upst.configure(background='MediumOrchid1')
upst.withdraw()

lblUpdateRno=Label(upst,text="Enter Rno",width=10,font=("arial",16,'bold'),bg='#FFF0F5')
entUpdateRno=Entry(upst,bd=5,width=10,font=("arial",16,'bold'))
lblUpdateName=Label(upst,text="Enter Name",width=10,font=("arial",16,'bold'),bg='#FFF0F5')
entUpdateName=Entry(upst,bd=5,width=10,font=("arial",16,'bold'))
lblUpdateMks=Label(upst,text="Enter Marks",width=10,font=("arial",16,'bold'),bg='#FFF0F5')
entUpdateMks=Entry(upst,bd=5,width=10,font=("arial",16,'bold'))
btnUpSave=Button(upst,text="Save",width=10,font=("arial",16,'bold'),command=f7)
btnUpBack=Button(upst,text="Back",width=10,font=("arial",16,'bold'),command=f8)

lblUpdateRno.pack(pady=10)
entUpdateRno.pack(pady=10)
lblUpdateName.pack(pady=10)
entUpdateName.pack(pady=10)
lblUpdateMks.pack(pady=10)
entUpdateMks.pack(pady=10)
btnUpSave.pack(pady=10)
btnUpBack.pack(pady=10)

#delete
delst=Toplevel(root)
delst.title("Delete S")
delst.geometry("500x400+300+200")
delst.configure(background='salmon1')
delst.withdraw()

lblDeleteRno=Label(delst,text="enter Rno",width=10,font=("arial",16,'bold'),bg='#FFF0F5')
entDeleteRno=Entry(delst,bd=5,width=10,font=("arial",16,'bold'))
btnDelete=Button(delst,text="Delete",width=10,font=("arial",16,'bold'),command=f11)
btnDelBack=Button(delst,text="Back",width=10,font=("arial",16,'bold'),command=f10)
lblDeleteRno.pack(pady=10)
entDeleteRno.pack(pady=10)
btnDelete.pack(pady=10)
btnDelBack.pack(pady=10)
root.mainloop()



		