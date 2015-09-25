#!/usr/bin/env python

class Marmot(object):
    _belly = {}

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'My name is %s' % self.name    

    def whistle(self):
        if self._belly:
            key = list(self._belly)[0]
            if self._belly[key] > 0:
                self._belly[key] -= 1
            else:
                del self._belly[key]
            return True
        else:
            return False
            
    def feed(self, food):
        if food in self._belly:
            self._belly[food] += 1
        else: 
            self._belly[food] = 0


class MarmotList(Marmot):
    _belly = []

    def feed(self, food):
        self._belly.append(food)
    
    def whistle(self):
        if len(self._belly) > 0: 
            #self.belly = self.belly[:-1]
            del self._belly[-1]
            return True
        else:
            return False
