from hashlib import new
from logging import captureWarnings
from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    self.__length = 0
    self.__front = None
    self.__back = None
 
  def __dq_contents(self):
    if self.__length == 0:
      return self.__contents
    if self.__back >= self.__front:
      return self.__contents[self.__front:self.__back + 1]
    return self.__contents[self.__front:] + self.__contents[:self.__back + 1]
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    # Orient your string from front (left) to back (right).
    if self.__length == 0:
        return '[ ]'
    string = ''
    dq_contents = self.__dq_contents()
    for i in range(self.__length):
        string = string + str(dq_contents[i]) + ', '
    return '[ ' + string[0:len(string) - 2] + ' ]'
    #above line uses string slicing of the deque
    
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__length

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    self.__capacity = self.__capacity * 2
    temp = [None] * self.__capacity
    contents = self.__dq_contents()
    for i in range(self.__length):
      temp[i] = contents[i]
    self.__front = 0
    self.__back = self.__length - 1
    self.__contents = temp

  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__length == 0:
      self.__contents[0] = val
      self.__front = 0
      self.__back = 0
      self.__length += 1
      return
    if self.__front == (self.__back + 1) % self.__capacity:
      self.__grow()
    self.__front = (self.__front - 1) % self.__capacity
    self.__contents[self.__front] = val
    self.__length += 1
    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__length == 0:
      return
    self.__front = (self.__front + 1) % self.__capacity
    self.__length -= 1
    return self.__contents[(self.__front - 1) % self.__capacity]
    
  def peek_front(self):
    # TODO replace pass with your implementation.
    if self.__length == 0:
      return
    return self.__contents[self.__front]
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__length == 0:
      self.__contents[0] = val
      self.__front = 0
      self.__back = 0
      self.__length += 1
      return
    if self.__front == (self.__back + 1) % self.__capacity:
      self.__grow()
    self.__back = (self.__back + 1) % self.__capacity
    self.__contents[self.__back] = val
    self.__length += 1
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__length == 0:
      return
    self.__back = (self.__back - 1) % self.__capacity
    self.__length -= 1
    return self.__contents[(self.__front + 1) % self.__capacity]

  def peek_back(self):
    # TODO replace pass with your implementation
    if self.__length == 0:
      return
    return self.__contents[self.__back]

 #No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
  #pass