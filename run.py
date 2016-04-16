''' This file (hypothetically) runs the fetch_lyrics.py file and applies the markov chain
module to create a new song. For this version we import the files previously fetched 
from the lyrics_output.txt file.'''

from markov_python.cc_markov import MarkovChain

mc = MarkovChain()
mc.add_file('lyrics_output.txt')
outp = mc.generate_text()
outp_object = open('radiohead_song.txt', 'w')

for i in range(0,6):
	outp = outp + mc.generate_text()

	outp_object.write(str(outp))

print "Done."