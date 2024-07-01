class Node:
    def __init__(self,item=None,next=None):
        self.item = item 
        self.next = next

class SLL :
    def __init__(self,start=None) :
         self.start = start

    def Insert_first(self,data) :
        n = Node(data)
        if(self.start is None):
           self.start = n
           n.next = n
            
        else :
              n.next = self.start
              temp = self.start  
              while temp.next is not self.start :    
                  temp = temp.next 
              temp.next = n   
              self.start = n  
              
    def Is_empty(self):
        return self.start == None 
    def Insert_At_Last(self,data) :
        n = Node(data)
        if(self.Is_empty()):
            self.start = n
            n.next = n
        else :
            temp = self.start
            while(temp.next  is not self.start ) :
                temp = temp.next 
            temp.next = n 
            n.next = self.start     
    def delete_first(self):
        if(self.start.next is self.start) :
            self.start = None
            
        else :    
               
               temp = self.start
               while(temp.next is not self.start) :
                   temp = temp.next
               temp.next = self.start.next
               self.start = self.start.next 
    def delete_Last(self) :
        temp = self.start
        if(self.start.next is self.start):
            self.start = None 
        else :        
            while(temp.next.next is not self.start) :
                temp = temp.next
            temp.next = self.start
    def Search(self,data):
             
             
             
                temp = self.start
                while(True):
                    if(temp.item == data):
                        return temp

                    else : 
                        temp = temp.next 
                        if(temp == self.start):
                            return "Not find value"
                               
                
                else :
                       return  "not have value"                  
    def Insert_After(self,temp,data):
        if(temp is not None):
           n = Node(data)
           n.next = temp.next
           temp.next = n
        # if(temp == self.start and temp.next == self.start) :
        #     n.next = self.start   
       
         
            
    def print_all(self):
        if self.start is None:
            print("The list is empty.") 
            return
        temp = self.start 
        while True :
           print(temp.item)
           temp = temp.next
           if(temp == self.start) :
               break
        #    if(temp.next == self.start):
        #        break
        #    else :temp = temp.next
              


Cll = SLL()
# Cll.Insert_first(1)
# Cll.Insert_first(2)
Cll.Insert_first(3)
# Cll.Insert_first(4)
# Cll.Insert_At_Last(10)
# Cll.Insert_At_Last(20)
# Cll.Insert_At_Last(30)
Cll.Insert_After(Cll.Search(3),None)
# print(Cll.Search(0))
# Cll.delete_Last()
# Cll.delete_first()

Cll.print_all()