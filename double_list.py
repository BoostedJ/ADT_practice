from node import Node
# TODO: display_reverse, sort, search, remove_at_index, prepend, insert_after, remove, remove_after, get_length


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
            return self.head

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


if __name__ == '__main__':
    double_list = DoubleList()
    empty = DoubleList()
    for i in range(1, 11):
        double_list.append(i*10)
    double_list.display()
    empty.display()
