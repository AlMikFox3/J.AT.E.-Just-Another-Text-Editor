from tkinter import *
import tkinter.filedialog as tk
import tkinter.messagebox as tk2
import tkinter.simpledialog as tk3
from time import sleep
from algo import *
def operate(res,text):
        res2=[]
        res3=[]
        for i in range(0,len(text)):
                if(text[i]=='\n'):
                      res2.append(i)            
        if len(res2)==1:
               for val in res:
                       res3.append("1."+str(val))
               return res3
        else:
                
                res2.append(len(text)+10)
                k=0
                res2[k-1]=-1
                for val in res:
                        while val>res2[k]:
                                k+=1
                        count=val-res2[k-1]-1
                        res3.append(str(k+1) + '.'+str(count))       
                return res3                             
                
        
class JATE(Frame):
	def __init__(self,master):
		super(JATE,self).__init__(master)
		self.create_widgets()
		self.set_keyboard_shortcuts()

	def create_widgets(self):
		self.text1 = Text(width = 20, height = 20, undo = True, font = ("Georgia","12"))
		self.text1.pack(expand = YES, fill = BOTH)

		
		
		menubar = Menu(self)
		fmenu = Menu(menubar)
		emenu = Menu(menubar)
		tmenu = Menu(menubar)
		fontmenu = Menu(menubar)
		#fsizemenu = Menu(menubar)
		hcmenu = Menu(menubar)
		#fsizemenu = Menu(menubar)
		hcmenu.add_command(label = 'Red', command = self.red)
		hcmenu.add_command(label = 'Blue', command = self.blue)
		hcmenu.add_command(label = 'Green', command = self.green)
		hcmenu.add_command(label = 'Black', command = self.black)
		hcmenu.add_command(label = 'Highlight', command = self.hyellow)
		hcmenu.add_command(label = 'Remove Highlight', command = self.remh)
		fontmenu.add_command(label = 'Georgia + 12 + Normal', command = self.f1)
		fontmenu.add_command(label = 'Georgia + 8 + Normal', command = self.f2)
		fontmenu.add_command(label = 'Georgia + 16 + Normal', command = self.f3)
		fontmenu.add_command(label = 'Georgia + 12 + Bold', command = self.f4)
		fontmenu.add_command(label = 'Georgia + 8 + Bold', command = self.f5)
		fontmenu.add_command(label = 'Georgia + 16 + Bold', command = self.f6)
		fontmenu.add_command(label = 'Georgia + 12 + Italic', command = self.f7)
		fontmenu.add_command(label = 'Georgia + 8 + Italic', command = self.f8)
		fontmenu.add_command(label = 'Georgia + 16 +Italic', command = self.f9)
		fontmenu.add_command(label = 'Georgia + 12 + Bold Italic', command = self.f10)
		fontmenu.add_command(label = 'Georgia + 8 + Bold Italic', command = self.f11)
		fontmenu.add_command(label = 'Georgia + 16 + Bold Italic', command = self.f12)
		fmenu.add_command(label = 'New', command = self.newDoc)
		fmenu.add_command(label = 'Open', command = self.openDoc)
		fmenu.add_command(label = 'Save', command = self.saveDoc)
		emenu.add_command(label = 'Copy', command = self.copy)
		emenu.add_command(label = 'Paste', command = self.paste)
		emenu.add_command(label = 'Clear', command = self.clear)
		tmenu.add_command(label = 'Word Count', command = self.wordCount)
		tmenu.add_command(label = 'Search', command = self.searchText)
		menubar.add_cascade(label ='File', menu = fmenu)
		menubar.add_cascade(label ='Edit', menu = emenu)
		menubar.add_cascade(label ='Tools', menu = tmenu)
		#menubar.add_cascade(label ='Font', menu = fontmenu)
		#menubar.add_cascade(label ='Size', menu = fsizemenu)
		tmenu.add_command(label = 'Search and Replace', command = self.searchRep)
		menubar.add_cascade(label ='Font Themes', menu = fontmenu)
		menubar.add_cascade(label ='Colour & Highlight', menu = hcmenu)
		root.config(menu = menubar)

	def newDoc(self):
		if(tk2.askyesno("Message","Continue without saving ? All the unsaved data will be lost....")):
			self.text1.delete("1.0",END)

	def saveDoc(self):
		
		savefile = tk.asksaveasfile(mode = 'w', defaultextension = '.txt')
		text2save = str(self.text1.get("1.0", END))
		savefile.write(text2save)
		savefile.close()

	def openDoc(self):
		openfile = tk.askopenfile(mode = 'r')
		text = openfile.read()
		self.text1.insert(END, text)
		openfile.close()

	def copy(self):
		var = str(self.text1.get(SEL_FIRST,SEL_LAST))
		self.clipboard_clear()
		self.clipboard_append(var)
	

	def paste(self):
		result = self.selection_get(selection = "CLIPBOARD")   #get text from clipboard
		self.text1.insert("1.0", result)

	def clear(self):
		self.text1.delete("1.0", END)

	def wordCount(self):
		userText = self.text1.get("1.0", END)
		wordList = userText.split()
		number_of_words = len(wordList)
		tk2.showinfo('Word Count', 'Words:  ' + str(number_of_words))

	def f1(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',font = ("Georgia","12","normal"))

	def f2(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',font = ("Georgia","8","normal"))

	def f3(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',font = ("Georgia","16","normal"))

	def f4(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',font = ("Georgia","12","bold"))

	def f5(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',font = ("Georgia","8","bold"))

	def f6(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',font = ("Georgia","16","bold"))

	def f7(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',font = ("Georgia","12","italic"))

	def f8(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',font = ("Georgia","8","italic"))

	def f9(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',font = ("Georgia","16","italic"))

	def f10(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',font = ("Georiga","12","bold italic"))

	def f12(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',font = ("Georgia","16","bold italic"))

	def f11(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',font = ("Georgia","8","bold italic"))

	def red(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',foreground = 'red')

	def yellow(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',foreground = 'yellow')

	def green(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',foreground = 'green')

	def black(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',foreground = 'black')

	def blue(self):
		self.text1.tag_remove('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_add('f1',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f1',foreground = 'blue')

	def hyellow(self):
		self.text1.tag_add('f17',SEL_FIRST,SEL_LAST)
		self.text1.tag_config('f17',background = 'yellow')

	def remh(self):
		self.text1.tag_remove('match','1.0',END)
		self.text1.tag_remove('f17',SEL_FIRST,SEL_LAST)
		


	def searchRep(self):
		
		x = tk3.askstring('Search','Enter the word to be searched')
		userText = self.text1.get("1.0", END)
		res=Boyer_Moore(userText.lower() ,x)
		res=operate(res,userText)
		for val in res:
			pos = val
			if not pos: 
				break
			lastpos = '%s+%dc' % (pos, len(x))
			self.text1.tag_add('match', pos, lastpos)
			self.text1.tag_config('match', foreground='blue',background='yellow')
			if(tk2.askyesno("Message","Replace the highlighted word ?")):
				y = tk3.askstring('Search','Enter the new word')
				self.text1.delete(pos,lastpos)
				self.text1.insert(pos,y)
			pos = lastpos
		self.text1.tag_remove('match', '1.0', END)	
	def searchText(self):
		
		x = tk3.askstring('Search','Enter the word to be searched')
		userText = self.text1.get("1.0", END)
		res=Boyer_Moore(userText.lower() ,x)
		res=operate(res,userText)
		for val in res:
			pos = val
			if not pos: 
				break
			lastpos = '%s+%dc' % (pos, len(x))
			self.text1.tag_add('match', pos, lastpos)
			pos = lastpos
			self.text1.tag_config('match', foreground='blue',background='yellow')

		
		if(tk2.askyesno("Message",str(len(res)) +" matches found\nCancel Highlight ?")):self.text1.tag_remove('match', '1.0', END)


	def set_keyboard_shortcuts(self):
		#print("dsd")
		self.bind('<Control-o>', self.openDoc)
		self.bind('<Control-s>', self.saveDoc)
		self.bind('<Control-f>', self.searchText)






root = Tk()
root.title("J.A.T.E. (Just Another TeXt Editor)")
root.geometry('1028x720')
app = JATE(root)
app.mainloop()
