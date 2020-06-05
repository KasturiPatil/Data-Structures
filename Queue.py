class Queue:
      def __init__(self):
            self.queue = []

      def enqueue(self,data):
            self.queue.append(data)
            print(self.queue)

      def dequeue(self):
            if (len(self.queue) < 1):
                  print("No elements in queue")
            else:
                  print(self.queue.pop(0))

      def size(self):
            print(len(self.queue))
