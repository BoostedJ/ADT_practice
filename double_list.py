from node import Node
# TODO: sort, search, remove_at_index, remove_after


class DoubleNode(Node):
    def __init__(self, data, next=None, prev=None):
        super().__init__(data, next)
        self.prev = prev


class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        curr_node = self.head
        try:
            while curr_node is not self.tail:
                print(curr_node.data, end=', ')
                curr_node = curr_node.next
            print(curr_node.data)
        except AttributeError:
            return

    def display_reverse(self):
        curr_node = self.tail
        try:
            while curr_node is not self.head:
                print(curr_node.data, end=', ')
                curr_node = curr_node.prev
            print(curr_node.data)
        except AttributeError:
            return

    def is_empty(self):
        if self.get_length() == 0:
            return True
        return False

    def append(self, value):
        if not isinstance(value, DoubleNode):
            value = DoubleNode(value)
        if not self.head:
            self.head = value
            self.tail = value
        else:
            value.prev = self.tail
            self.tail.next = value
            self.tail = value

    def prepend(self, value):
        if not isinstance(value, DoubleNode):
            value = DoubleNode(value)
        if not self.head:
            self.head = value
            self.tail = value
        else:
            value.next = self.head
            self.head.prev = value
            self.head = value

    def insert_after(self, value_to_insert, value):
        curr_node = self.head
        try:
            while curr_node.data != value:
                curr_node = curr_node.next
            new_node = value_to_insert if isinstance(value_to_insert, Node) else Node(value_to_insert)
            new_node.next = curr_node.next
            curr_node.next.prev = new_node
            new_node.prev = curr_node
            curr_node.next = new_node
        except AttributeError:
            print(f"No node with data {value}")

    def remove(self, value):
        if isinstance(value, DoubleNode):
            value = value.data
        if self.head.data == value:
            if self.tail.data == value:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif self.tail.data == value:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr_node = self.head
            try:
                while curr_node.data != value:
                    curr_node = curr_node.next
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
                curr_node = None
            except AttributeError:
                print(f"No node with data {value}")
                return -1

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
    double_list = DoubleList()
    empty = DoubleList()
    for i in range(1, 11):
        double_list.append(i*10)
    double_list.insert_after(15, 10)
    double_list.prepend(5)
    double_list.display()
