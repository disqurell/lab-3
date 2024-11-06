from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


class CustomPriorityQueue:
    def __init__(self, maxsize=0):
        self.priority_queue = PriorityQueue(maxsize=maxsize)
        self.regular_queue = []

    def put(self, item: PrioritizedItem):
        self.priority_queue.put(item)

    def put_regular(self, item: Any):
        self.regular_queue.append(item)

    def get(self):
        if not self.priority_queue.empty():
            return self.priority_queue.get().item
        elif self.regular_queue:
            return self.regular_queue.pop(0)
        return None

    def empty(self):
        return self.priority_queue.empty() and not self.regular_queue
