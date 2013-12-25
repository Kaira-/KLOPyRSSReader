import feedparser

d = feedparser.parse("http://feeds.feedburner.com/RockPaperShotgun.xml")

# print "Items: " + len(d['items'])
print "Title: " + d.entries[0].title
print "Link: " + d.entries[0].link
print "Desc: " + d.entries[0].description.replace("&#8217;", "\'")
print "Published: " + d.entries[0].published
print "Updated: " + d.entries[0].updated
print "Id " + d.entries[0].id
