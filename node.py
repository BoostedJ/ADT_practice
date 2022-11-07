class single_node:
    def __init__(self, data):
        self.data = data
        self.next = None

class single_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        curr_node = self.head
        if self.head == None:
            print()
            return -1
        while curr_node.next != None:
            print(f'{curr_node.data}, ',end='')
            curr_node = curr_node.next
        print(f'{curr_node.data}')
	
    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            curr_node = self.head
            while curr_node.data != None:
                if curr_node.next == None:
                    curr_node.next = node
                    break
                curr_node = curr_node.next
            self.tail = node
	
    def remove(self, node):
        curr_node = self.head
        if self.head == node:
            if self.tail == node:
                self.head = None
                self.tail = None
            self.head = node.next
        elif self.tail == node:
            while curr_node.next.next != None:
                curr_node = curr_node.next
            curr_node.next = None
        else:
            while curr_node.next != node:
                curr_node = curr_node.next
            if curr_node.next == node:
                curr_node.next = curr_node.next.next
                if curr_node.next == None:
                    self.tail = curr_node


if __name__ == '__main__':
    node1 = single_node(10)
    node2 = single_node(20)
    node3 = single_node(30)
    list1 = single_list()
    list2 = single_list()
    list1.append(node1)
    list1.append(node2)
    list1.append(node3)
    list1.display()
    list2.display()