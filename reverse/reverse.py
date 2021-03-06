class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:
            return None
        if node.next_node is not None:
            new_node = node.next_node  
            node.next_node = prev  
            self.reverse_list(new_node, node)
        else:
            self.head = node
            node.next_node = prev

    def iterative_reverse(self, node):
        if node is None:
            return None
        current = self.head
        prev = None
        while current is not None:
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        self.head = prev
            
        
            



linklist = LinkedList()

linklist.add_to_head(10)
linklist.add_to_head(20)
linklist.add_to_head(30)
linklist.add_to_head(40)
linklist.add_to_head(50)

# linklist.reverse_list(linklist.head, None)

linklist.iterative_reverse(linklist.head)
print(linklist.head.next_node.value)


