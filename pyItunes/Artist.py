class Artist:
    name = None
    songs = []
    score = 0

    ##Make an addsong method that appends to songs but also increments score

    def __eq__(self, other):
        return self.name == other.name

    def __init__(self, name):
        self.name = name

    def addSong(self, song):
        self.songs.append(song)
        self.score += song.play_count

    def rating(self):
        return self.score / len(self.songs)


    # def score(self):
    #     index = 0
    #     for x in self.songs:
    #         index += x.play_count
    #         print index
    #     return index


