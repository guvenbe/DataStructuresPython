from LinkedList import my_linked_list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop

        temp =self.get(index)
        temp.prev.next =temp.next
        temp.next.prev = temp.prev
        temp.prev = None
        temp.next = None
        self.length -= 1

        # before = self.get(index - 1)
        # temp = before.next
        # after = temp.next
        #
        # before.next = after
        # after.prev = before
        # temp.prev = None
        # temp.next = None
        # self.length -= 1
        return temp




my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()
print("Testing POP")
print(my_doubly_linked_list.pop().value)
print("\n")
my_doubly_linked_list.print_list()
print("Testing prepend")
my_doubly_linked_list.append(2)
my_doubly_linked_list.prepend(0)
my_doubly_linked_list.print_list()
print("Testing pop_fist\n\n")
print(my_doubly_linked_list.pop_first().value)
print(my_doubly_linked_list.pop_first().value)
print(my_doubly_linked_list.pop_first().value)
# print(my_doubly_linked_list.pop_first())
print("Testing get")
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.prepend(0)
my_doubly_linked_list.print_list()
print(my_doubly_linked_list.get(2).value)
print(my_doubly_linked_list.get(3).value)
print(my_doubly_linked_list.get(4).value)
my_doubly_linked_list.set_value(1, 5)
print("after set to 5")
my_doubly_linked_list.print_list()
print("after insert")
my_doubly_linked_list.insert(1, 88)
my_doubly_linked_list.print_list()
print("after remove")
my_doubly_linked_list.remove(1)
my_doubly_linked_list.print_list()