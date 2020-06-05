class Node:
      def __init__(self, data=None):
            self.data = data
            self.next = None
        
class Linked:
            def __init__(self):
                  self.head = None
               
             # This function prints contents of linked list
            def Print(self):
                  
                  printval = self.head
                  while printval is not None:
                        print(printval.data) 
                        printval = printval.next

            #Inserting at the Beginning of the Linked List
            def AtFront(self,new_data):
                  new_node = Node(new_data)
                  new_node.next = self.head
                  self.head = new_node

            #Add a node after a given node
            def Mid(self,prev_node,new_data):
                  if prev_node is None:
                        print("Previous node must be in linked list")
                        return
                  mid_node = Node(new_data)
                  mid_node.next = prev_node.next
                  prev_node.next = mid_node
                  
                  

            #Inserting at the End of the Linked List
            def AtEnd(self,new_data):
                  newnode = Node(new_data)
                  if self.head is None:
                        self.head= newnode
                        return
                  last= self.head
                  while(last.next):
                        last = last.next
                  last.next = newnode
                  
            #Deleting a Node
            def remove(self,key):
                  temp= self.head
                  if (temp is not None):
                        if (temp.data == key):
                              temp = None
                              return
                        
                  while (temp is not None):
                        if temp.data == key:
                              break
                        prev_node = temp
                        temp = temp.next
                        
                  if (temp == None):
                        return
                  
                  prev_node.next = temp.next
                  temp = None

            #Reverse a linked list
            def reverse(self):
                  prev_node= None
                  curr= self.head
                  while(curr is not None):
                        next= curr.next
                        curr.next  = prev_node
                        prev_node = curr
                        curr = next
                  self.head = prev_node
                  
llist=Linked()

llist.head= Node("Monday")
second= Node("Tuesday")
third= Node("Wednesday")

llist.head.next= second
second.next= third

llist.AtFront("Sunday")

llist.Mid(llist.head.next,"Mid")

llist.AtEnd("Thursday")

llist.remove("Mid")

llist.reverse()
llist.Print()


                  

