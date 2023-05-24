# class node :
#     def __init__(self,data=None,next_node = None) :
#         self.data = data
#         self.next_node = next_node


# class Linked_list:
#     def __init__(self):
#         self.head = None

#     def add_node(self,data):
#         new_node = node(data)
#         new_node.next_node = self.head
#         self.head = new_node
#         # print(new_node.data)

#     # def size(self):



import matplotlib.pyplot as plt

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        # new node has attribute next  as in class   
        new_node.next = self.head
        self.head = new_node
        # if self.head == None:
        #     self.head = new_node
        #     return
        # last_node = self.head
        # while last_node.next != None:
        #     last_node = last_node.next
        # last_node.next = new_node
    # to search a node we give up a data in that node 
    def search(self,data):
        currnt_node = self.head
        while currnt_node:
            if(currnt_node.data == data):
                return True
            else:
                currnt_node =currnt_node.next
        return False

    def delet(self,data):
        curret_node = self.head
        while curret_node:
            if(curret_node.data == data):
                curret_node = None
            




    # def display(self):
    #     current = self.head
    #     while current != None:
    #         print(current.data)
    #         current = current.next

    # def plot(self):
    #     x = []
    #     y = []
    #     current = self.head
    #     while current != None:
    #         x.append(current.data)
    #         y.append(id(current))
    #         current = current.next
    #     plt.plot(y, x, 'ro-')
    #     plt.title('Linked List')
    #     plt.xlabel('Node')
    #     plt.ylabel('Data')
    #     plt.show()

linked_list = LinkedList()
linked_list.append(3)
linked_list.append(4)
linked_list.append(9)
linked_list.append(5)
linked_list.append(8)
print(linked_list.search(10))

# linked_list.display()
# linked_list.plot()

# listone = Linked_list()
# listone.add_node(3)
# listone.add_node(5)
# listone.add_node(6)
