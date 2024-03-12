#!/usr/bin/python3
"""this module provides a solution to the lockbox problem"""
from collections import deque


class Queue:
    """a class implementation of a queue"""
    def __init__(self):
        """the constructor method of the class"""
        self.items = deque()

    def enqueue(self, item):
        """this method enqueues items to the queue"""
        self.items.append(item)

    def dequeue(self):
        """this method dequeue items from the queue"""
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        """this method checks if the queue is empty"""
        return len(self.items) == 0

    @property
    def size(self):
        """this getter method returns the size of the queue"""
        return len(self.items)

    def __str__(self):
        """this returns the string value of the class"""
        return ", ".join([f"{x}" for x in self.items])


def canUnlockAll(boxes):
    """a function that solves the lockbox problem"""
    if (not len(boxes)):
        return False
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    queue = Queue()
    queue.enqueue(0)

    while (queue.size):
        try:
            u = queue.dequeue()
            for i in boxes[u]:
                if (not visited[i] and 0 <= i < num_boxes):
                    visited[i] = True
                    queue.enqueue(i)
        except Exception as _:
            return

    return all(visited)
