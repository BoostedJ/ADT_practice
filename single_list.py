from node import Node
# TODO: Sort


class SingleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        curr_node = self.head
        if not self.head:
            print()
            return -1
        while curr_node.next:
            print(f'{curr_node.data}, ', end='')
            curr_node = curr_node.next
        print(f'{curr_node.data}')

    def display_reverse(self):
        temp_tail = self.tail
        curr_node = self.head
        if self.tail != self.head:
            for _ in range(self.get_length()-1):
                while curr_node.next != temp_tail:
                    curr_node = curr_node.next
                print(temp_tail.data, end=', ')
                temp_tail = curr_node
                curr_node = self.head
        print(self.head.data)

    def sort(self, node):
        if not node or not node.next:
            return self.head
        left = node
        right = self.get_mid(node)
        temp = right.next
        right.next = None
        right = temp

        left = self.sort(left)
        right = self.sort(right)
        return self.merge(left, right)

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
        for _ in range(index):
            curr_node = curr_node.next
        self.remove(curr_node.data)

    def append(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if not self.head:
            self.head = value
            self.tail = value
        else:
            self.tail.next = value
            self.tail = value

    def prepend(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        temp_head = self.head
        self.head = node
        node.next = temp_head

    def insert_after(self, value_to_insert, value):
        curr_node = self.head
        try:
            while curr_node.data != value:
                curr_node = curr_node.next
            new_node = value_to_insert if isinstance(value_to_insert, Node) else Node(value_to_insert)
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

    def get_mid(self, head=None):
        if not head:
            head = self.head
        curr_node = head
        i = 0
        while i != self.get_length()//2 and curr_node.next:
            i += 1
            curr_node = curr_node.next
        return curr_node

    def get_length(self):
        curr_node = self.head
        i = 0
        while curr_node:
            curr_node = curr_node.next
            i += 1
        return i


if __name__ == '__main__':
    nodes = [Node(i*10) for i in range(1, 11)]
    list1 = SingleList()
    list2 = SingleList()
    for node in nodes:
        list1.append(node)
    list1.append(5)
    list1.display()
    print(list1.get_mid().data)
