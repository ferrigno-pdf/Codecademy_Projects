class Pokemon:
    def __init__(self, name, type, max_health, health, is_knocked_out=False):
        self.name = name
        self.type = type
        self.max_health = max_health
        self.health = health
        self.is_knocked_out = False
    
    def __repr__(self):
        return '%s has now %s health.' % (self.name, self.health)
    
    def lose_health(self, attack):
        self.health -= attack
        if self.health == 0:
            self.is_knocked_out = True
            return 'Your pokemon %s is knocked out!' % (self.name)
        elif self.health != 0:
            return 'Your pokemon has now %s health!' % (self.health)
    
    def gain_health(self, gain):
        self.gain = gain
        self.health += gain
        return 'Your %s has gained %s' % (self.name, self.gain)


charmander = Pokemon('Charmander', 'Fire', 500, 100)


charmander.gain_health(30)






        
    
    





