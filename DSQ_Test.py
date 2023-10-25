import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_
  def test_empty_string_dq(self):
    self.assertEqual('[ ]', str(self.__deque))

  def test_empty_len_dq(self):
    self.assertEqual(0, len(self.__deque))

  def test_push_front_dq(self):
    self.__deque.push_front(1)
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_push_front_len_dq(self):
    self.__deque.push_front(6)
    self.assertEqual(1, len(self.__deque))

  def test_push_back_dq(self):
    self.__deque.push_back(1)
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_push_front_len_dq(self):
    self.__deque.push_front(6)
    self.assertEqual(1, len(self.__deque))

  def test_push_front_twice_dq(self):
    self.__deque.push_front('vanilla')
    self.__deque.push_front('strawberry')
    self.assertEqual("[ strawberry, vanilla ]", str(self.__deque))

  def test_push_front_twice_len_dq(self):
    self.__deque.push_front('vanilla')
    self.__deque.push_front('strawberry')
    self.assertEqual(2, len(self.__deque))

  def test_push_back_twice_dq(self):
    self.__deque.push_back('orange')
    self.__deque.push_back(None)
    self.assertEqual("[ orange, None ]", str(self.__deque))

  def test_push_front_twice_len_dq(self):
    self.__deque.push_front('vanilla')
    self.__deque.push_front('strawberry')
    self.assertEqual(2, len(self.__deque))
  
  def test_push_front_10_dq(self):
    for i in range(10):
      self.__deque.push_front(i)
    self.assertEqual('[ 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ]', str(self.__deque))

  def test_push_front_10_len_dq(self):
    for i in range(10):
      self.__deque.push_front(i)
    self.assertEqual(10, len(self.__deque))

  def test_push_back_10_dq(self):
    for i in range(10):
      self.__deque.push_back(i)
    self.assertEqual('[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]', str(self.__deque))

  def test_push_back_10_len_dq(self):
    for i in range(10):
      self.__deque.push_back(i)
    self.assertEqual(10, len(self.__deque))

  def test_pop_front_empty_dq(self):
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_empty_return_dq(self):
    self.assertEqual(None, self.__deque.pop_front())

  def test_pop_front_empty_len_dq(self):
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))

  def test_pop_back_empty_dq(self):
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_empty_return_dq(self):
    self.assertEqual(None, self.__deque.pop_back())

  def test_pop_back_empty_len_dq(self):
    self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))
  
  def test_pop_front_dq(self):
    self.__deque.push_front('lime')
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_return_dq(self):
    self.__deque.push_front('lime')
    self.assertEqual('lime', self.__deque.pop_front())

  def test_pop_front_len_dq(self):
    self.__deque.push_front('lime')
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))

  def test_pop_back_dq(self):
    self.__deque.push_front('lime')
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_return_dq(self):
    self.__deque.push_front('cucumber')
    self.assertEqual('cucumber', self.__deque.pop_back())

  def test_pop_back_len_dq(self):
    self.__deque.push_front('lime')
    self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))

  def test_pop_front_5_times_dq(self):
    for i in range(10):
      self.__deque.push_back(i)
    for i in range(5):
      self.__deque.pop_front()
    self.assertEqual('[ 5, 6, 7, 8, 9 ]', str(self.__deque))

  def test_pop_front_5_dq(self):
    for i in range(10):
      self.__deque.push_back(i)
    for i in range(5):
      self.__deque.pop_front()
    self.assertEqual(5, len(self.__deque))

  def test_pop_back_5_dq(self):
    for i in range(10):
      self.__deque.push_back(i)
    for i in range(5):
      self.__deque.pop_back()
    self.assertEqual('[ 0, 1, 2, 3, 4 ]', str(self.__deque))

  def test_pop_back_5_dq(self):
    for i in range(10):
      self.__deque.push_back(i)
    for i in range(5):
      self.__deque.pop_back()
    self.assertEqual(5, len(self.__deque))

  def test_peek_front_empty_dq(self):
    self.assertEqual(None, self.__deque.peek_front())

  def test_peek_front_empty_len_dq(self):
    self.__deque.peek_front()
    self.assertEqual(0, len(self.__deque))

  def test_peek_back_empty_dq(self):
    self.assertEqual(None, self.__deque.peek_back())

  def test_peek_back_empty_len_dq(self):
    self.__deque.peek_back()
    self.assertEqual(0, len(self.__deque))

  def test_peek_front_dq(self):
    self.__deque.push_back(33)
    self.assertEqual(33, self.__deque.peek_front())

  def test_peek_front_len_dq(self):
    self.__deque.push_back(33)
    self.__deque.peek_front()
    self.assertEqual(1, len(self.__deque))

  def test_peek_back_dq(self):
    self.__deque.push_front(2)
    self.assertEqual(2, self.__deque.peek_back())

  def test_peek_back_len_dq(self):
    self.__deque.push_front(2)
    self.__deque.peek_back()
    self.assertEqual(1, len(self.__deque))

  def test_empty_string_q(self):
    self.assertEqual('[ ]', str(self.__queue))

  def test_empty_len_q(self):
    self.assertEqual(0, len(self.__queue))

  def test_enqueue_q(self):
    self.__queue.enqueue('grapefruit')
    self.assertEqual("[ grapefruit ]", str(self.__queue))

  def test_enqueue_len_q(self):
    self.__queue.enqueue('grapefruit')
    self.assertEqual(1, len(self.__queue))

  def test_enqueue_10_q(self):
    for i in range(10):
      self.__queue.enqueue(i)
    self.assertEqual('[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]', str(self.__queue))

  def test_enqueue_10_len_q(self):
    for i in range(10):
      self.__queue.enqueue(i)
    self.assertEqual(10, len(self.__queue))

  def test_dequeue_empty_q(self):
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_empty_len_q(self):
    self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))

  def test_dequeue_empty_return_q(self):
    self.assertEqual(None, self.__queue.dequeue())

  def test_dequeue_q(self):
    self.__queue.enqueue('potatoes')
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_len_q(self):
    self.__queue.enqueue('potatoes')
    self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))

  def test_dequeue_return_q(self):
    self.__queue.enqueue('avocado')
    self.assertEqual('avocado', self.__queue.dequeue())

  def test_dequeue_5_q(self):
    for i in range(10):
      self.__queue.enqueue(i)
    for i in range(5):
      self.__queue.dequeue()
    self.assertEqual('[ 5, 6, 7, 8, 9 ]', str(self.__queue))

  def test_dequeue_5_len_q(self):
    for i in range(10):
      self.__queue.enqueue(i)
    for i in range(5):
      self.__queue.dequeue()
    self.assertEqual(5, len(self.__queue))

  def test_peek_empty_q(self):
    self.assertEqual(None, self.__queue.peek())

  def test_peek_empty_len_q(self):
    self.__queue.peek()
    self.assertEqual(0, len(self.__queue))

  def test_peek_q(self):
    self.__queue.enqueue(5)
    self.assertEqual(5, self.__queue.peek())

  def test_peek_len_q(self):
    self.__queue.enqueue(5)
    self.__queue.peek()
    self.assertEqual(1, len(self.__queue))

  def test_empty_stack(self):
    self.assertEqual('[ ]', str(self.__stack))

  def test_empty_len_stack(self):
    self.assertEqual(0, len(self.__stack))

  def test_push_stack(self):
    self.__stack.push(6)
    self.assertEqual('[ 6 ]', str(self.__stack))

  def test_push_len_stack(self):
    self.__stack.push(6)
    self.assertEqual('[ 6 ]', str(self.__stack))

  def test_push_10_stack(self):
    self.__stack.push(6)
    self.assertEqual('[ 6 ]', str(self.__stack))

  def test_push_10_stack(self):
    for i in range(10):
      self.__stack.push(i)
    self.assertEqual('[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]', str(self.__stack))

  def test_push_10_len_stack(self):
    for i in range(10):
      self.__stack.push(i)
    self.assertEqual(10, len(self.__stack))

  def test_pop_empty_stack(self):
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_empty_return_stack(self):
    self.assertEqual(None, self.__stack.pop())

  def test_pop_empty_length_stack(self):
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack))

  def test_pop_5_stack(self):
    for i in range(10):
      self.__stack.push(i)
    for i in range(5):
      self.__stack.pop()
    self.assertEqual('[ 0, 1, 2, 3, 4 ]', str(self.__stack))

  def test_pop_5_len_stack(self):
    for i in range(10):
      self.__stack.push(i)
    for i in range(5):
      self.__stack.pop()
    self.assertEqual(5, len(self.__stack))

  def test_peek_empty_stack(self):
    self.__stack.peek()
    self.assertEqual('[ ]', str(self.__stack))

  def test_peek_empty_len_stack(self):
    self.__stack.peek()
    self.assertEqual(0, len(self.__stack))

  def test_peek_empty_return_stack(self):
    self.assertEqual(None, self.__stack.peek())

  def test_peek_stack(self):
    self.__stack.push(23)
    self.__stack.peek()
    self.assertEqual('[ 23 ]', str(self.__stack))

  def test_peek_len_stack(self):
    self.__stack.push(23)
    self.__stack.peek()
    self.assertEqual(1, len(self.__stack))

  def test_peek_return_stack(self):
    self.__stack.push(23)
    self.assertEqual(23, self.__stack.peek())

if __name__ == '__main__':
  unittest.main()

