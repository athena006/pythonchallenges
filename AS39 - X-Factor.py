import random 
Songs = []
for j in range(9):
	Songs.append(["Song1", "Song2", "Song3", "Song4", "Song5", "Song6", "Song7", "Song8", "Song9", "Song10"])

ran_artist = random.randint(0,9)
ran_songs = random.randint(0,9)
Artists = ["Taylor Swift", "Katy Perry", "Shawn Mendes", "Rihanna", "The Weeknd", "Miley Cyrus", "Drake", "Justin Bieber", "Ed Sheeran", "Shakira"]
new = []
for i in range (0,19):
	ran_songs = random.randint(0,9)
	ran_artist = random.randint(0,9)
    if i == 0:
        pass
    elif i == 1:
    	while ran_artist == new[i-1]:
    		ran_artist = random.randint(0,9)
    else:
    	while ran_artist == new[i-1] or ran_artist == new[i-2]:
    		ran_artist = random.randint(0,9)
	print(Artists[ran_artist])
	print(Songs[ran_artist][ran_songs])
	new.append(ran_artist)
    
print(new)
