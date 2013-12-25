import feedparser

d = feedparser.parse("http://feeds.feedburner.com/RockPaperShotgun.xml")

#print "Elements: " + len([d.entries])
print "Title: " + d.entries[0].title
print "Link: " + d.entries[0].link
print "Desc: " + d.entries[0].description.replace("&#8217;", "\'")
print "Published: " + d.entries[0].published
print "Id " + d.entries[0].id
