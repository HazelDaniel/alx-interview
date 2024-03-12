#!/usr/bin/python3
from collections import deque


class Queue:
    """a class implementation of a queue"""
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    @property
    def size(self):
        return len(self.items)

    def __str__(self):
        return ", ".join([f"{x}" for x in self.items])


def canUnlockAll(boxes):
    """a function that solves the lockbox problem"""
    if (not len(boxes)):
        return False
    num_boxes = len(boxes)
    boxes = [set(i) for i in boxes]
    visited = [False] * num_boxes
    visited[0] = True

    queue = Queue()
    queue.enqueue(0)

    while (queue.size):
        try:
            u = queue.dequeue()
            for i in boxes[u]:
                if (not visited[i] and i < num_boxes):
                    visited[i] = True
                    queue.enqueue(i)
        except Exception as _:
            return

    return all(visited)
