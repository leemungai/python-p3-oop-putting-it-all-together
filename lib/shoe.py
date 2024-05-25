#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
      self.brand = brand
      self.size = size

    def cobble(self):
        print("Your shoe has been repaired.")
        self.condition = "New"  
    @property
    def size(self):
       return self._size 
    
    @size.setter
    def size(self,size):
        if isinstance(size, int):
          self._size = size
        else:
          print("size must be an integer")