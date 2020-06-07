class CircularQueue:
      def __init__(self, maxsize):
            self.queue= list()
            # taking input for the size of the Circular queue
            self.maxsize = maxsize
            self.head = 0
            self.tail = 0
            
       # add element to the queue 
      def enqueue(self, data):
            if self.size() == (self.maxsize - 1):
                  return ("Queue is full.")
            else:
                  self.queue.append(data)
                  self.tail = (self.tail+1) % self.maxsize
                  return data
            
      # remove element from the queue       
      def dequeue(self):
            if self.size() == 0:
                  return ("Queue is empty.")
            else:
                  data = self.queue[self.head]
                  self.head = (self.head+1) % self.maxsize
                  return data
            
       # find the size of the queue
      def size(self):
            if self.tail >= self.head:
                  Queuesize = self.tail - self.head
            else:
                  Queuesize = self.maxsize - (self.head - self.tail)
            return Queuesize
      
      def display(self):
        for i in range(self.head, self.tail):
            print(self.queue[i], end=",")

      
size = input("Enter the size of the Circular Queue =")
Queue = CircularQueue(int(size))

print(Queue.enqueue("Jan"))
print(Queue.enqueue("Feb"))
print(Queue.enqueue("Mar"))
print(Queue.enqueue("Apr"))
print(Queue.enqueue("May"))
print(Queue.enqueue("Jun"))
print(Queue.display())
print(Queue.size())
print(Queue.dequeue())
print(Queue.dequeue())
print(Queue.dequeue())
print(Queue.size())





















                  
                        
