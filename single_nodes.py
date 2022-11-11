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

    def search(self, value):
        curr_node = self.head
        i = 0
        try:
            while curr_node.data != value:
                curr_node = curr_node.next
                i += 1
            print(f'{value} was found at index {i}')
            return i
        except AttributeError:
            print(f'No node with data {value} was found')
            return -1
	
    def remove_at_index(self, index):
        length = self.get_length()
        if index >= length:
            return -1
        curr_node = self.head
        for index in range(length):
            curr_node = curr_node.next
        self.remove(curr_node)

    def append(self, value):
        if not isinstance(value, single_node):
            value = single_node(value)
        if self.head == None:
            self.head = value
            self.tail = value
        else:
            self.tail.next = value
            self.tail = value

    def prepend(self, node):
        if not isinstance(node, single_node):
            node = single_node(node)
        temp_head = self.head
        self.head = node
        node.next = temp_head
	
    def insert_after(self, value_to_insert, value):
        curr_node = self.head
        try:
            while curr_node.data != value:
                curr_node = curr_node.next
            new_node = value_to_insert if isinstance(value_to_insert, single_node) else single_node(value_to_insert)
            new_node.next = curr_node.next
            curr_node.next = new_node
            print(curr_node.next.data)
        except AttributeError:
            print(f"No node with data {node.data}")

    def remove(self, value):
        curr_node = self.head
        if self.head.data == value:
            if self.tail.data == value:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif self.tail.data == value:
            while curr_node.next != self.tail:
                curr_node = curr_node.next
            curr_node.next = None
            self.tail = curr_node
        else:
            try:
                while curr_node.next.data != value:
                    curr_node = curr_node.next
                curr_node.next = curr_node.next.next
            except AttributeError:
                print(f"No node with data {value}")
                return -1

    def remove_after(self, value):
        if self.head == self.tail or value == self.tail.data:
            return -1
        curr_node = self.head
        try:
            while curr_node.data != value:
                curr_node = curr_node.next
            curr_node.next = curr_node.next.next
        except AttributeError:
            print(f"No node with data {value}")
            return -1
        
    def is_empty(self):
        if self.get_length() == 0:
            return True
        return False

    def get_length(self):
        curr_node = self.head
        i = 0
        while curr_node != None:
            curr_node = curr_node.next
            i += 1
        return i

    # TODO: PrintReverse, Sort

if __name__ == '__main__':
    nodes = [single_node(i*10) for i in range(1, 11)]
    list1 = single_list()
    list2 = single_list()
    for node in nodes:
        list1.append(node)
    list1.remove_at_index(2)
    list1.display()
    print(list1.get_length())