import feedparser
import Tkinter
from Tkinter import *
import ttk
import tkMessageBox

class App(ttk.Frame):
    def __init__(self, parent):
        self.root = parent
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.feedslist = []
        self.readFeedsFromFile()
        self.initUI()
        
    def initUI(self):
        self.menu = Tkinter.Menu(self.parent)
        self.root.config(menu = self.menu)
        self.fileMenu = Tkinter.Menu(self.menu)
        self.menu.add_cascade(label="File", menu = self.fileMenu)
        self.fileMenu.add_command(label="Import new feed...", command=self.hello)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.root.destroy)
        self.parent.title("KLOPyRSSReader2013")
        self.pack(fill=Tkinter.BOTH, expand=1)
        self.style = ttk.Style()
        self.root.minsize(600,400)
        ttk.Style.configure(self.style, "TFrame", background="#333")
        
        self.lb = Tkinter.Listbox(self, width=20)

        #when inserting feeds into the listbox, use the user-given name instead of URL
        #we could also use the title of the feed, maybe that's even better
        for i in self.feedslist:
            self.lb.insert(Tkinter.END, i[0])
            self.lb.place(x=10,y=10)

    def hello(self):
        top = self.top = Toplevel(self)

        Label(top, text="Value").pack()
        
        self.e = Entry(top, text="default")
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        print "value is", self.e.get()

        self.top.destroy()
  
    def readFeedsFromFile(self):
        with open("feeds.txt") as f:
            for line in f.readlines():
                string = line.lstrip()
                if (string[0] == '#'):
                    continue
                self.feedslist.append(string)
        print "Number of feeds: " + str(len(self.feedslist))
        for i in self.feedslist:
            print i

if __name__ == "__main__":
    #d = feedparser.parse(feedsList[0])
    #print "Title: " + d.entries[0].title
    #print "Link: " + d.entries[0].link
    #print "Desc: " + d.entries[0].description.replace("&#8217;", "\'").replace("&amp;", "&")
    #print "Published: " + d.entries[0].published
    #print "Updated: " + d.entries[0].updated
    #print "Id " + d.entries[0].id
    root = Tkinter.Tk()
    app = App(root)
    root.mainloop()

