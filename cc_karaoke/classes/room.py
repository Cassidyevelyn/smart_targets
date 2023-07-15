class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capcity = capacity
        self.till = 0
        self.guests = []

    def add_to_till(self, amount):
        self.till += amount
    
    def check_in_guest(self, guest):
        if (len(self.guests)) < self.capacity: 
            self.guests.append(guest)
    
    def check_out_guest(self, guest):
        self.guests.remove(guest)
    
    def add_song(self, song):
        self.songs.append(song)