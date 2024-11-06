from queues import CustomPriorityQueue, PrioritizedItem


class Reader:
    def __init__(self, name, priority, service_time):
        self.name = name
        self.priority = priority
        self.service_time = service_time

    def enter_queue(self, queue: CustomPriorityQueue):
        queue.put(PrioritizedItem(self.priority, self))


class Librarian:
    def __init__(self):
        self.queue = CustomPriorityQueue()
        self.served_count = 0
        self.current_time = 0

    def serve_reader(self):
        reader = self.queue.get()
        if reader:
            print(f"[{self.current_time} s] Serving {reader.name} with priority {reader.priority}")
            self.current_time += reader.service_time
            self.served_count += 1
            print(f"[{self.current_time} s] Finished serving {reader.name}")

    def add_reader(self, reader: Reader):
        reader.enter_queue(self.queue)
