class Guest:
    def __init__(self, name, cash, song ):
        self.name = name
        self.cash = cash
        self.favourite_song = song
    
    def can_afford(self, amount):
        return self.cash >= amount
    
    def pay(self, amount):
        if self.can_afford(amount): # (if statements are booleans), doesn't the can_afford func doesnt do this
            self.cash -= amount
    
    def cheer(self, songs):
        for song in songs: 
            if song == self.favourite_song:
                return "Whoo Hoo!"
        return None 