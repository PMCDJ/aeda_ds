from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList

class HashTable(Dictionary):
    def __init__(self, size=101):
        self.array_size = size
        self.num_elements = 0
        self.table = (self.array_size * ctypes.py_object)()
        for i in range (self.array_size):
            self.table[i] = SinglyLinkedList()
    
    def hash_function(self,k):
        return sum([ord(c) for  c in k]) % self.array_size

    def size(self):
        return self.array_size

    def is_full(self):
        if self.array_size == 0:
            return True
        return False


    def insert(self, k, v): 
        if is_full == False:
            
    def update(self, k, v): pass

    def remove(self, k): pass

    def keys(self): pass

    def values(self): pass

    def items(self): pass