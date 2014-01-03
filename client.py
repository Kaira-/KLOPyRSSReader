import feedparser
import Tkinter
import ttk
import tkMessageBox
import tkHyperlinkManager
import webbrowser

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
        self.currentarticleindex = 0
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
        self.lb.grid(row = 0, column = 0, sticky=Tkinter.NW)
        
        self.textbox = Tkinter.Text(self, width=48, wrap=Tkinter.WORD, state=Tkinter.DISABLED)
        self.textbox.grid(row = 0, column = 1, columnspan=4, rowspan=4, sticky=Tkinter.NW)
        #self.textbox.insert(0.0, "Hello world!")

        self.hyperlinkManager = tkHyperlinkManager.HyperlinkManager(self.textbox)

        self.currentfeed = ""

        self.refreshbutton = Tkinter.Button(self, text="Refresh feed")
        self.refreshbutton.grid(row=4, column=1, sticky=Tkinter.W)

        self.previousbutton = Tkinter.Button(self, text="Previous article", command=self.previousButtonClick)
        self.previousbutton.grid(row=4, column=2, sticky=Tkinter.W)

        self.nextbutton = Tkinter.Button(self, text="Next article", command=self.nextButtonClick)
        self.nextbutton.grid(row=4, column=3, sticky=Tkinter.W)

        self.deletefeedbutton = Tkinter.Button(self, text="Delete selcted feed")
        self.deletefeedbutton.grid(row = 4, column = 0, sticky = Tkinter.W)

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
        c = Tkinter.Button(top, text="Cancel", command = self.cancel)
        b.pack()
        c.pack()

    def ok(self):
        feed = self.e.get()
        print "value is " + feed
        
        self.insertFeedToFile(feed)

        self.top.destroy()

    def cancel(self):
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
    
    #refreshes the feed by selecting it and sets the current index to 0
    def onDouble(self, event):
        self.currentarticleindex = 0
        widget = event.widget
        selection = widget.curselection()
        index = selection[0]
        self.currentfeed = feedparser.parse(self.feedslist[int(index)])
        self.loadArticle()


    def linkClick(self, link):
        webbrowser.open(link)

    def loadArticle(self):
        #hack to fix if we somehow read beyond the articles that exist in the feed
        if self.currentarticleindex + 1 > len(self.currentfeed.entries):
            self.currentarticleindex = len(self.currentfeed.entries) - 1

        title = self.currentfeed.entries[self.currentarticleindex].title
        link = self.currentfeed.entries[self.currentarticleindex].link
        description = self.currentfeed.entries[self.currentarticleindex].description
        description = description.replace("&#8217;", "\'").replace("&#8211;", "-")
        self.textbox.config(state=Tkinter.NORMAL)
        self.textbox.delete(1.0, Tkinter.END)
        self.textbox.insert(Tkinter.END, title, self.hyperlinkManager.add(lambda: self.linkClick(link)))
        self.textbox.insert(Tkinter.END, "\r\n\r\n")
        self.textbox.insert(Tkinter.END, description)
        self.textbox.config(state=Tkinter.DISABLED)

    def nextButtonClick(self):
        self.currentarticleindex = self.currentarticleindex + 1
        self.loadArticle()

    def previousButtonClick(self):
        if self.currentarticleindex == 0:
            return
        else:
            self.currentarticleindex = self.currentarticleindex - 1
            self.loadArticle()


if __name__  == "__main__":
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

