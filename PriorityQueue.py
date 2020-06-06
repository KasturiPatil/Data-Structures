class Node:
      def __init__(self,data,prio):
            self.data = data
            self.prio = prio
            
class PriorityQueue:
      def __init__(self):
            self.queue =list()
            
      def insert(self, node):
            if self.size() == 0:
                  self.queue.append(node)
            else:
                  for i in range(0,self.size()):
                        if node.prio >= self.queue[i].prio:
                              if i ==(self.size()-1):
                                    self.queue.insert( i+1, node)
                              else:
                                    continue
                        else:
                              self.queue.insert( i, node)
                              return True
      def delete(self):
            return self.queue.pop(0)

      def show(self):
            for x in self.queue:
                  print (str(x.data)+" - "+str(x.prio))
                  
      def size(self):
            return len(self.queue)

Q = PriorityQueue()
node1 = Node("C", 3)
node2 = Node("B", 2)
node3 = Node("A", 1)
node4 = Node("D", 26)

Q.insert(node1)
Q.insert(node2)
Q.insert(node3)
Q.insert(node4)

Q.show()
print("_____________")
Q.delete()
Q.delete()
Q.show()                 
                  
            
            
