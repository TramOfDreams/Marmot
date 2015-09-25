#!/usr/bin/env python

class Marmot(object):
    belly = {}

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'My name is %s' % self.name    

    def whistle(self):
        if self.belly:
            key = self.belly.keys()[0]
            if self.belly[key] > 0:
                self.belly[key] -= 1
            else:
                del self.belly[key]
            return True
        else:
            return False
            
    def feed(self, food):
        if food in self.belly:
            self.belly[food] += 1
        else: 
            self.belly[food] = 0


class MarmotList(Marmot):
    belly = []

    def feed(self, food):
        self.belly.append(food)
    
    def whistle(self):
        if len(self.belly) > 0: 
            #self.belly = self.belly[:-1]
            del self.belly[-1]
            return True
        else:
            return False


