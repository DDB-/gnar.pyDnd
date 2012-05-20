import math

class Player:

    stats = {
        'str':10,
        'dex':10,
        'con':10,
        'int':10,
        'wis':10,
        'cha':10,
        'bab':4
    }

    saves = {
        'fort':0,
        'refl':0,
        'will':0
    }

    weapons = []

    level = 1

    def __init__( self, s = 10, d = 10, c = 20, i = 10, w = 10, C = 10 ):
        self.stats['str'] = s
        self.stats['dex'] = d
        self.stats['con'] = c
        self.stats['int'] = i
        self.stats['wis'] = w
        self.stats['cha'] = C

    def calcAc(self):
        pass

    def melee(self):
        return self.calcBonus( self.stats['str'] ) + self.stats['bab']

    def ranged(self):
        return self.calcBonus( self.stats['dex'] ) + self.stats['bab']

    def calcCmb(self):
        pass

    def strBonus(self):
        pass

    def calcBonus(self, x):
        return math.ceil( (x - 10)/2 )
