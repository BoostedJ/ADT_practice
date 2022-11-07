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

    def prepend(self, node):
        temp_head = self.head
        self.head = node
        node.next = temp_head
	
    def insert_after(self, to_insert, node_after):
        curr_node = self.head
        while curr_node != node_after:
            curr_node.next
       # if curr_node == node_after:
            #if 

    def remove(self, node):
        if self.head == None:
            return -1
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

    def remove_after(self, node):
        if self.head == self.tail or node == self.tail:
            return -1
        curr_node = self.head
        while curr_node != node:
            curr_node = curr_node.next
        if curr_node == node:
            if curr_node.next == self.tail:
                self.tail = curr_node
                curr_node.next = None
            elif curr_node.next.next != None:
                curr_node.next = curr_node.next.next
        return -1
        
    def get_length(self):
        curr_node = self.head
        i = 0
        while curr_node != None:
            curr_node = curr_node.next
            i += 1
        return i

if __name__ == '__main__':
    node1, node2, node3, node4, node5 = [single_node(i*10) for i in range(1, 6)]
    nodes = [node1, node2, node3, node4, node5]
    list1 = single_list()
    for node in nodes:
        list1.append(node)
    list1.display()
    print(list1.get_length())