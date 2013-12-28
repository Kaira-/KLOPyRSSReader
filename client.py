import feedparser
from PIL import Image, ImageTk
import Tkinter
import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        self.initUI()

    def initUI(self): 
        self.parent.title("KLOPyRSSReader2013")
        self.pack(fill=Tkinter.BOTH, expand=1)
        self.style = ttk.Style()
        ttk.Style.configure(self.style, "TFrame", background="#333")
        
        #feeds have names as first element and UI as second
        self.feedslist = [["RPS","http://feeds.feedburner.com/RockPaperShotgun.xml"], ["Nedroid Picture Diary", "http:nedroid.com/feed/"]]
        self.lb = Tkinter.Listbox(self, width=20)

        #when inserting feeds into the listbox, use the user-given name instead of URL
        #we could also use the title of the feed, maybe that's even better
        for i in self.feedslist:
            self.lb.insert(Tkinter.END, i[0])

        self.lb.place(x=10,y=10)
	
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
    menu = Tkinter.Menu(root)
    root.config(menu = menu)
    fileMenu = Tkinter.Menu(menu)
    menu.add_cascade(label="File", menu = fileMenu)
    fileMenu.add_command(label="Import new feed...")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit")
    #root.geometry("600x600+300+300")
    root.minsize(600,400)
    root.mainloop()

