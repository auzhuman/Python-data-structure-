import singly_linked_list

p = singly_linked_list.linkedlists()

list1 = p.makeLlist([1,2,5])
p.prints(list1)

q = singly_linked_list.linkedlists()
list2 = q.makeLlist([1,3,4])
q.prints(list2)



head = singly_linked_list.nodes()
dummy = head

while list2 and list1:
    # print("initial values ",list1.val,list2.val)
    if list1.val <= list2.val:
        print("initial values ",list1.val,"<=",list2.val)
        dummy.next = list1
        list1 = list1.next
    else :
        print("initial values ",list1.val,">",list2.val)

        dummy.next = list2
        list2 = list2.next
    print("inserted val is ",dummy.next.val)
    dummy = dummy.next

if list1:
    print("remaining values from list 1")
    p.prints(list1)
    dummy.next = list1
if list2:
    print("remaining values from list 2")
    p.prints(list2) 
    dummy.next = list2
p.prints(head.next)