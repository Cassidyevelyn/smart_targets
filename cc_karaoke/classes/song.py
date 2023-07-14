# Write a song class with a constructor function (init) which takes arguments for:
# name and band_name
# and assign each one to a property/attribute

# Then follow the tests to write methods
# Once you have all the song test passing move onto writing the guest class and pass the tests 
# and then finally write up the room class

class Song:
    def __init__(self, title, album):
        self.title = title
        self.album = album
        