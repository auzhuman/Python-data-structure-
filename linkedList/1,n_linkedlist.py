import singly_linked_list

p = singly_linked_list.linkedlists()
list1 = p.makeLlist([1,2])
# p.prints(list1)

head = list1   # 4
headonebefore = head.next


while head.next != None :
    print("head")
    p.prints(head)

    temp = head.next 
    curr = head
    lastcurr = None

    while curr.next != None :
        lastcurr = curr
        curr = curr.next
    
    # print("lastcurr",lastcurr.val)
    # print("head",head.val)
    if head == lastcurr:
        
        # for changing the last two values
        # temp2 = lastcurr
        # head.next = None
        # head = head.next
        # lastcurr.next = None
        # head.next = lastcurr
        break
        
        # p.prints(head)
    else :
        print("executed")
        lastcurr.next = None


        curr.next = temp #last value next is remaining
        print("curr is ")
        p.prints(curr)
        head.next = curr
    headonebefore= head.next
    head = head.next.next
    print("list")
    p.prints(list1)
    # print("head value is ",head.val)
    
   




print("list1 is") 
p.prints(list1)