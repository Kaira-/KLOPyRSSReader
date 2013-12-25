import Tkinter
import feedparser

class App:
    def __init__(self, master):
        self.w = Tkinter.Canvas(master, width=500, height=400)
        self.w.pack()
        self.w.create_rectangle(10, 350, 500, 10, fill="white")
        self.canvas_id = self.w.create_text(15,10,anchor="nw")
        self.e = Tkinter.Entry(root, width=80)
        self.e.pack()
        self.e.delete(0, Tkinter.END)
        self.e.insert(0, "default value")
        self.s = self.e.get()
        self.w.itemconfig(self.canvas_id, text=self.s)
        self.w.insert(self.canvas_id, 12, "")
        self.w.update()	
	
if __name__ == "__main__":
    feedsList = ["http://feeds.feedburner.com/RockPaperShotgun.xml", "http://nedroid.com/feed/"]
    d = feedparser.parse(feedsList[1])
    print "Title: " + d.entries[0].title
    print "Link: " + d.entries[0].link
    print "Desc: " + d.entries[0].description.replace("&#8217;", "\'").replace("&amp;", "&")
    print "Published: " + d.entries[0].published
    print "Updated: " + d.entries[0].updated
    print "Id " + d.entries[0].id
    root = Tkinter.Tk()
    app = App(root)
    menu = Tkinter.Menu(root)
    root.config(menu = menu)
    fileMenu = Tkinter.Menu(menu)
    menu.add_cascade(label="File", menu = fileMenu)
    fileMenu.add_command(label="Import new feed...")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit")
    rtitle = root.title("KLOPyRSSReader")
    root.geometry("600x600+300+300")
    root.mainloop()

