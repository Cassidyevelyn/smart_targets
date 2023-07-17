class Room:
    def __init__(self, name, capacity, fee):
        self.name = name
        self.capacity = capacity
        self.till = 0
        self.guests = []
        self.fee = fee
        self.songs = []

    def add_to_till(self, amount):
        self.till += amount
    
    def check_in_guest(self, guest):
        if (len(self.guests)) < self.capacity: 
            self.guests.append(guest)
    
    def check_out_guest(self, guest):
        self.guests.remove(guest)
    
    def add_song(self, song):
        self.songs.append(song)

    def get_capacity(self):
        return self.capacity

    def number_of_guests(self):
        return len(self.guests)

    def number_of_songs(self):
        return len(self.songs)