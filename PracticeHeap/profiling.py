import cProfile
from FibonacciHeap import FibonacciHeap, FibonacciTree

# Profile Insert
fibonacci_heap = FibonacciHeap()
cProfile.run('fibonacci_heap.insert_node(7)')
cProfile.run('fibonacci_heap.insert_node(3)')
cProfile.run('fibonacci_heap.insert_node(17)')
cProfile.run('fibonacci_heap.insert_node(24)')

#Profile Get Min
cProfile.run('fibonacci_heap.get_min()')

#Profile Delete
cProfile.run('fibonacci_heap.extract_min()')