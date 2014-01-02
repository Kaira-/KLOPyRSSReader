import feedparser
import Tkinter
import ttk
import tkMessageBox

class App(ttk.Frame):
    def __init__(self, parent):
        self.root = parent
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.feedslist = []
        self.feedstitles = []
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
        self.pack(fill = Tkinter.BOTH, expand=1)
        self.style = ttk.Style()
        self.root.minsize(600,400)
        ttk.Style.configure(self.style, "TFrame", background="#333")
        
        self.lb = Tkinter.Listbox(self, width=36)
        #bind doubleclick to onDouble-function
        self.lb.bind("<Double-Button-1>", self.onDouble)
        self.lb.grid(row = 0, column = 0)
        
        self.textbox = Tkinter.Text(self, width=48, wrap=Tkinter.WORD)
        self.textbox.grid(row = 0, column = 1)
        #self.textbox.insert(0.0, "Hello world!")

        for i in self.feedslist:
            d = feedparser.parse(i)
            self.feedstitles.append(d.feed.title)

        #when inserting feeds into the listbox, use the user-given name instead of URL
        #we could also use the title of the feed, maybe that's even better
        for i in self.feedstitles:
            self.lb.insert(Tkinter.END, i)

    def hello(self):
        top = self.top = Tkinter.Toplevel(self)

        Tkinter.Label(top, text="Value").pack()
        
        self.e = Tkinter.Entry(top, text="default")
        self.e.pack(padx=5)

        b = Tkinter.Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        feed = self.e.get()
        print "value is " + feed
        
        self.insertFeedToFile(feed)

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

    def insertFeedToFile(self, feed):
        self.feedslist.append(feed)
        with open("feeds.txt", "a") as f:
            f.write(feed)

        self.refreshFeedsList()

    def refreshFeedsList(self):
        self.lb.delete(0, Tkinter.END)
        self.feedstitles = []
        for i in self.feedslist:
            d = feedparser.parse(i)
            self.feedstitles.append(d.feed.title)

        for i in self.feedstitles:
            self.lb.insert(Tkinter.END, i)
    
    def onDouble(self, event):
        widget = event.widget
        selection = widget.curselection()
        index = selection[0]
        self.textbox.insert(Tkinter.END, self.feedstitles[int(index)] + "\r\n")

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

