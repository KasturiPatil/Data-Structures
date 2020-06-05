class Stack:
      def __init__(self):
            self.stack=[]
            
      def add(self,data):
            self.stack.append(data)
            print(self.stack)
            
      def isempty(self):
            return self.stack == []
      
      def pop(self):
            return self.stack.pop()
      
      def size(self):
            return len(self.stack)
      
      def peek(self):
            return self.stack[len(self.stack)-1]

s=Stack()
print(s.isempty())
s.add("Monday")
s.add("Tuesday")
print(s.size())
s.add("Wednesday")
print(s.peek())
print(s.pop())
print(s.size())
