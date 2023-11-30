# queue-using-linked-list
# Python Queue Implementation

This repository contains a basic implementation of a queue data structure in Python. The queue is implemented using a linked list.

## Features

- Enqueue: Add an element to the rear of the queue.
- Dequeue: Remove an element from the front of the queue.
- Get Front: Retrieve the element at the front of the queue.
- Get Rear: Retrieve the element at the rear of the queue.
- Size: Get the current size of the queue.
- Is Empty: Check if the queue is empty.

## Usage

```python
from queue import Queue

# Create a new queue
my_queue = Queue()

# Check if the queue is empty
print("Is the queue empty?", my_queue.is_empty())

# Enqueue elements
my_queue.enqueue(10)
my_queue.enqueue(20)

# Dequeue an element
my_queue.dequeue()

# Get the front and rear elements
my_queue.get_front()
my_queue.get_rear()

# Get the size of the queue
my_queue.size()
