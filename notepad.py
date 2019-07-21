from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

class notepad:
    def __init__(self, frame):
        self.frame = frame
        self.frame.title('Untitled - Notepad')
        self.frame.geometry('800x600')
        self.textarea = Text(self.frame, font=("Courier New",12,'bold'))
        self.textarea.pack(fill = BOTH, expand = 1)
        self.menu = Menu(self.frame)
       
        self.file = Nonehnvvv
        
        self.filemenu = Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="New", command=self.new_fun)
        self.filemenu.add_command(label="Open", command=self.open_fun)
        self.filemenu.add_command(label="Save", command=self.save_fun)
        self.filemenu.add_command(label="Exit", command=self.exit_fun)
        self.menu.add_cascade(label="File", menu=self.filemenu)
       
        self.editmenu = Menu(self.menu, tearoff = 0)
        self.editmenu.add_command(label="Cut",command=self.cut_fun)
        self.editmenu.add_cascade(label="Copy", command=self.copy_fun)
        self.editmenu.add_cascade(label="Paste", command=self.paste_fun)
        self.menu.add_cascade(label="Edit", menu=self.editmenu)
       
        self.helpmenu = Menu(self.menu, tearoff = 0)
        self.helpmenu.add_command(label="About Notepad", command=self.about_fun)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
       
        self.frame.config(menu = self.menu)
       
      
        
    def new_fun(self):
        #global self.file
        self.frame.title("Untitled - Notepad")
        self.file = None
        self.textarea.delete(1.0, END)
        
    def open_fun(self):
        #global self.file
        self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                       ("text Documents", "*.txt")])
        if self.file=="":
            self.file = None
        else:
            self.frame.title(os.path.basename(self.file) + " - Notepad")
            self.textarea.delete(1.0, END)
            f = open(self.file, "r")
            self.textarea.insert(1.0, f.read())
            f.close()
        
    
    def save_fun(self):
        if self.file==None:
            self.file = asksaveasfilename(initialfile = "'Untitled.txt", defaultextension = ".txt", 
                                        filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])
            if self.file=="":
                self.file = None
            else:
                f = open(self.file, "w")
                f.write(self.textarea.get(1.0, END))
                f.close
                self.frame.title(os.path.basename(self.file) + " - Notepad")
        else:
            f = open(self.file, "w")
            f.write(self.textarea.get(1.0, END))
            f.close()
    
    def exit_fun(self):
        self.frame.destroy()
        
    def cut_fun(self):
        self.textarea.event_generate(("<<Cut>>"))
        
    def copy_fun(self):
        self.textarea.event_generate(("<<Copy>>"))
        
    def paste_fun(self):
        self.textarea.event_generate(("<<Paste>>"))
    
    def about_fun(self):
        showinfo("Notepad", "GUI of Notepad")
    

root = Tk()
app = notepad(root)

root.mainloop()