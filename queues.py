# fifo
class nodes :
    def __init__(self,val):
        self.val = val
        self.next = None
class queue:
    def __init__(self) -> None:
        self.left = self.right = None

    def enqueue(self,val):
        # for non-empty queues
        if self.right :
            
            #pointer to next node
            self.right.next = nodes(val)
            
            # next node
            self.right = self.right.next

        # for empty queues
    
        else : 
            self.left = self.right = nodes(val)

    def dequeue(self):
        if not self.left :
            return None
        val = self.left.val
        self.left = self.left.next
        return val
    
    def print(self):
        curr = self.left
        # print(curr.val)
        while curr :
            print(curr.val ,"->",end="")
            curr = curr.next
        print()

p = queue()

p.enqueue(1)
p.enqueue(2)
p.enqueue(3)
p.enqueue(4)
lists = []
for i in range(3):
    print("i",i)
    lists.append(p.dequeue())

print(lists)


# p.print()
        

