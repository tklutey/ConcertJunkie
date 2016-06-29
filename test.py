#!/usr/bin/env python
# coding=utf-8


from FindShows import FindShows
from pyItunes import *

# name = unicode("Sigur Rós", "utf-8")
#
# d = FindShows(name, "New York")
# d.get_show()

l = Library("itunes.xml")


collection = Collection()
artists = collection.fill_collect(l)

top_ten = len(artists) * .2

for x in range(int(top_ten)):
    # name = unicode(artists[x].name, "utf-8")
    name = artists[x].name
    # print name
    d = FindShows(name, "New York")
    d.get_show()
# for x in artists:
#     print x.name
#     print x.score



