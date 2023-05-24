from typing import List, Optional
class nodes :
    def __init__(self,val=0):
        self.val = val
        self.next = None

class linkedlists :
    def __init__(self):      
        self.tail = self.head = nodes(None)
    
    def insertnodes(self,val): 
        '''to add nodes we insert at tails and update
         tails next and tail'''
        self.tail.next = nodes(val) 
        self.tail = self.tail.next
    
    def makeLlist(self,list:list) -> Optional[nodes]:
        for i in list:
            self.insertnodes(i)
        return self.head.next
    

    def deletefromindex(self,index:int):
        i = 0
        curr = self.head
        while i < index :
            i = i+1
            curr = curr.next
            print(curr.val)
        # if curr :
        curr.next = curr.next.next

    def reverse(self):

        curr = self.head.next
        # print(curr.next.val)
        
        self.head = None #previ
        while curr :
            temp = curr.next
            # print(temp.val)
            curr.next =  self.head
            
            self.head = curr
            curr = temp
            # print(previ.val)
        # return (head)

    def prints(self,head:Optional[nodes]):
       
        curr = head

        while curr :
            print(curr.val,end= "-->> ")
            
            curr = curr.next
        print()
    

# p = linkedlists()

# list1 = p.makeLlist([1,2,5,8,9])
# p.prints(list1)

# p = linkedlists()
# list2 = p.makeLlist([1,3,4,5,6,28])
# p.prints(list2)



# head = nodes()
# dummy = head

# while list2 and list1:
#     # print("initial values ",list1.val,list2.val)
#     if list1.val <= list2.val:
#         print("initial values ",list1.val,"<=",list2.val)
#         dummy.next = list1
#         list1 = list1.next
#     else :
#         print("initial values ",list1.val,">",list2.val)

#         dummy.next = list2
#         list2 = list2.next
#     print("inserted val is ",dummy.next.val)
#     dummy = dummy.next

# if list1:
#     print("remaining values from list 1")
#     p.prints(list1)
#     dummy.next = list1
# if list2:
#     print("remaining values from list 2")
#     p.prints(list2) 
#     dummy.next = list2
# p.prints(head.next)
        

# p.prints(dummy)
# print(dummy.next.next.val)



# p.reverse()
# p.prints()

# p.deletefromindex(2)
# p.print(q)






