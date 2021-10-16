from dataclasses import dataclass
from typing import Any



@dataclass
class Node:
    value: int = None
    nxt: Any = None  


@dataclass
class Deque:
    head: Node = None     
    tail: Node = None     
    size: int = 0

    def add_first(self, n):
        new_node = Node(n, None)
        new_node.nxt = self.head
        self.head = new_node
        self.size +=1
  
    def add_last(self, n):
        temp = Node(n, None)
        if(self.tail == None):
           self.head = self.tail = temp
        
        else: 
            self.tail.nxt = temp
            self.tail = temp
        self.size += 1
            


    def to_string(self):
        s = "{ "
        node = self.head
        while node is not None:
            s += str(node.value) + " "
            node = node.nxt
        s += "}"
        return s


    def get_last(self):
        if(self.size == 0):
            print('You cant access an empty queue')
        else:            
            return self.tail.value
            
            

    def get_first(self):
        if(self.size == 0):
            print("You can't access an empty queue") 
        else:
            return self.head.value


    def remove_first(self):
        if(self.size == 0):
            print("You can't access an empty queue")
            return 
        else:
            temp = self.head
            self.head = self.head.nxt
            if(self.head == None):
                self.tail = None
            self.size -=1
            return temp.value
        
            
    def remove_last(self):
        node = self.head
        
        if self.head is None:
            print("You can't acess an empty queue")
            return None

        else:
            if node.nxt is not None:
                while node.nxt is not None:
                    prev = node 
                    node = node.nxt
                prev.nxt = None
                self.size -= 1
                return node.value
            else:
                self.size -=1
                self.head = None
                return node.value

    def sort(self):
        if self.size == 0:
            return
        else:
            node = self.head
        
        
    
               
            

            
