

class _DoublyLinkedBase:

    class _Node:
        __slots__ = '_element' , '_prev', '_next'           # streamline memory usage
        def __init__ (self, element, prev, next ):          # initialize node’s fields
            self._element = element                         # reference to user’s element
            self._prev = prev                               # reference to next node
            self._next = next                               # reference to next node

    def __init__ (self):
        self._header = self._Node(None, None, None)                                  
        self._trailer = self._Node(None, None, None)                                  
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0                                     

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, pred, succ):
        newest = self._Node(e, pred, succ)
        pred._next = newest
        succ._prev = newest
        self._size += 1

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                 # record deleted element
        node._prev = node._next = node._element = None # deprecate node
        return element


class LinkedDeque(_DoublyLinkedBase): 


    def first(self):

        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._trailer._prev._element 

    def insert_first(self, e):

        self._insert_between(e, self._header, self._header._next) # after header

    def insert_last(self, e):
 
        self._insert_between(e, self._trailer._prev, self._trailer) # before trailer

    def delete_first(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._delete_node(self._header._next) # use inherited method

    def delete_last(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        return self._delete_node(self._trailer._prev)


myList = LinkedDeque()
myList.insert_first(10)
print(len(myList))
myList.insert_last(22)
print(len(myList))
print(myList.first())
print(myList.last())