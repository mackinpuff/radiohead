'''Fetching lyrics from azlyrics.com'''


# Module import
from bs4 import BeautifulSoup
import urllib2
from time import sleep

# Main parameters
html_main = 'http://www.azlyrics.com/r/radiohead.html'

# Fetch the artist page

html = urllib2.urlopen(html_main)
radiohead = html.read()

soup = BeautifulSoup(radiohead, 'html.parser')
# radiohead = 

# List the hyperlinks to lyrics

# def print_songlinks(artistpage, artist):
	# linklist = []
	# for link in artistpage:
		# if str(artist) in link:
			# link2 = artistpage[:-5]+link
			# linklist.append(link2)
	# print(linklist)


# links = []
# for link in radiohead.a:
	# if 'radiohead' in link:
		# print link
	
# print_songlinks(radiohead.a, 'radiohead')
	
#http://www.azlyrics.com/lyrics/radiohead/

# Function to get anchors to all lyrics of radiohead
linklist = []
for link in soup.find_all('a'):
    if 'radiohead' in str(link.get('href')):
		linklist.append(link.get('href'))



# Function to fetch lyrics per song page
def fetch_lyrics(song,lyrics_object):
	lyrics = [] 
	line = song.readline()
	while line:
		if 'SongName' in line:
			lyrics.append(line[11:-3] + "\n")
		elif 'Usage of azlyrics.com content' in line:
			line = song.readline()
			while "</div>" not in line:
				lyrics.append(line)
				line = song.readline()
			else:
				break
		line = song.readline()

	lyrics_len = len(lyrics)
	for i in range(0, lyrics_len):
		lyrics[i]=lyrics[i].replace("<br>", "")
		lyrics_object.write(lyrics[i])
	lyrics_object.write("\n\n")
	lyrics_object.close()
	print 'Done with a song.'
	
linklist_len = len(linklist)
for i in range(1,linklist_len):
	html = 'http://www.azlyrics.com/' + linklist[i][3:]
	lyrics_object = open('lyrics_output.txt', 'a')
	print html
	song = urllib2.urlopen(html)
	fetch_lyrics(song, lyrics_object)
	sleep(5)

print 'Done.'

