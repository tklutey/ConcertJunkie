from pyItunes.Artist import Artist
class Collection:

    # collection = []

    def __init__(self):
        self.collection = []

    def fill_collect(self, library):

        for id, song in library.songs.items():
            self.add_artist(song)
        self.sort_by_rating()
        return self.collection

    def add_artist(self, song):
         for a in self.collection:
             if song.artist == a.name:
                 a.addSong(song)
                 return
         ##make new artist
         a = Artist(song.artist)
         a.addSong(song)
         self.collection.append(a)

    def sort_by_rating(self):
            """ Implementation of bubble sort """
            for i in range(len(self.collection)):
                for j in range(len(self.collection) - 1 - i):
                    if self.collection[j].rating() < self.collection[j+1].rating():
                        self.collection[j], self.collection[j + 1] = self.collection[j + 1], self.collection[j]  # Swap!

