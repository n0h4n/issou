#coding=UTF-8

import tkinter
from threading import Thread
import winsound

class Application(tkinter.Tk):
	def __init__(self):
		tkinter.Tk.__init__(self)
		#self.title('Risitas.exe')
		self.iconify()
		self.toplevel = tkinter.Toplevel(self)
		self.toplevel.overrideredirect(1)
		self.toplevel.resizable(width=False, height=False)
		self.issou = tkinter.PhotoImage(file ='issou.png')
		self.canvas = tkinter.Canvas(self.toplevel,width=self.winfo_screenwidth(),height=self.winfo_screenheight(),bg='white')
		self.canvas.grid(column=1,row=0)
		self.canvas.create_image(self.winfo_screenwidth()/2,self.winfo_screenheight()/2,image=self.issou)
		self.toplevel.geometry('{}x{}'.format(self.winfo_screenwidth(),self.winfo_screenheight()))
		self.init_menu()
		self.toplevel.mainloop()
		
	def init_menu(self):
		self.bouton_issou = tkinter.Button(self.toplevel,text="Quitter",command=self.quitter)
		self.bouton_issou.grid(column=0,row=0)
		
	def quitter(self):
		winsound.PlaySound("issou.wav", winsound.SND_FILENAME)
		self.destroy()
		return
		


Application()
