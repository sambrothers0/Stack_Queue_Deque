from audioop import lin2adpcm
from multiprocessing.sharedctypes import Value
from operator import index
from re import M


class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.value = val
            self.next = None
            self.prev = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__length = 0
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__length

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        new = self.__Node(val)
        new.next = self.__trailer
        new.prev = self.__trailer.prev
        new.prev.next = new
        new.next.prev = new
        self.__length += 1

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        if index >= self.__length or index < 0 or self.__length == 0:
            raise IndexError
        elif (self.__length/2) >= index:
            new = self.__Node(val)
            cur = self.__header.next
            for i in range(index):
                cur = cur.next
            new.next = cur
            new.prev = cur.prev
            cur.prev.next = new
            cur.prev = new
            self.__length += 1
        else:
            new = self.__Node(val)
            cur = self.__trailer.prev
            for i in range(self.__length-index-1):
                cur = cur.prev
            new.next = cur
            new.prev = cur.prev
            cur.prev.next = new
            cur.prev = new
            self.__length += 1

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if index >= self.__length or index < 0 or self.__length == 0:
            raise IndexError
        if (self.__length/2) >= index:
            cur = self.__header.next
            for i in range(index):
                cur = cur.next
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            self.__length -= 1
        else:
            cur = self.__trailer.prev
            for i in range(self.__length-index-1):
                cur = cur.prev
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            self.__length -= 1
        return cur.value

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if index >= self.__length or index < 0 or self.__length == 0:
            raise IndexError
        if (self.__length/2) >= index:
            cur = self.__header.next
            for i in range(index):
                cur = cur.next
        else:
            cur = self.__trailer.prev
            for i in range(self.__length-index-1):
                cur = cur.prev
        return cur.value
        
    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self.__length == 0:
            return
        self.append_element(self.remove_element_at(0))
        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        if self.__length == 0:
            return '[ ]'
        string = ''
        for node in self:
            string = string + str(node) + ', '
        return '[ ' + string[0:len(string) - 2] + ' ]'
        
    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.cur = self.__header
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.cur.next != self.__trailer:
            self.cur = self.cur.next
            return self.cur.value
        else:
            raise StopIteration
        
    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        reversed = Linked_List()
        cur = self.__trailer.prev
        while cur != self.__header:
            reversed.append_element(cur.value)
            cur = cur.prev
        return reversed
        


if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests
    my_list = Linked_List()
    for i in range(5):
        my_list.append_element(i)
    print(my_list)
    
    try:
        my_list.insert_element_at('a',0)
        print(my_list)
    except IndexError:
        print("Unable to unsert 'a' at index 0: IndexError")
    try:
        my_list.insert_element_at('a',55)
        print(my_list)
    except IndexError:
        print("Unable to unsert 'a' at index 55: IndexError")
    try:
        my_list.insert_element_at('a',-5)
        print(my_list)
    except IndexError:
        print("Unable to unsert 'a' at index -5: IndexError")

    try:
        print('Index 2 value: ' + str(my_list.get_element_at(2)))
    except IndexError:
        print("Unable to get element at index 2: IndexError")
    try:
        print('Index 55 value: ' + str(my_list.get_element_at(55)))
    except IndexError:
        print("Unable to get element at index 55: IndexError")
    try:
        print('Index -5 value: ' + str(my_list.get_element_at(-5)))
    except IndexError:
        print("Unable to get element at index -5: IndexError")

    try:
        my_list.remove_element_at(0)
        print(my_list)
    except IndexError:
        print("Unable to remove element at index 0: IndexError")
    try:
        my_list.remove_element_at(5)
        print(my_list)
    except IndexError:
        print("Unable to remove element at index 5: IndexError")
    try:
        my_list.remove_element_at(55)
        print(my_list.remove_element_at)
    except IndexError:
        print("Unable to remove element at index 55: IndexError")
    try:
        my_list.remove_element_at(-5)
        print(my_list)
    except IndexError:
        print("Unable to remove element at index -5: IndexError")
        
    for node in my_list:
        print(node)    
    for node in reversed(my_list):
        print(node)
