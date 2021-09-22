
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value
        self.next = next_node
        self.previous = previous_node

# Defines the singly linked list


class LinkedList:
    def __init__(self):
        self.head = None  # keep the head private. Not accessible outside this class
        self.tail = None
        self.size = 0

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        current = self.head

        if current == None:
            return None
        else:
            return current.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(n)

    def add_first(self, value):
        current = self.head
        new_node = Node(value)

        if current == None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
        else:
            current.previous = new_node
            new_node.next = current
            self.head = new_node
            self.size += 1

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def search(self, value):
        current = self.head

        if current == None:
            return False

        while current:
            if current.value == value:
                return True
            else:
                current = current.next

        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def length(self):
        return self.size

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def get_at_index(self, index):
        current = self.head
        count = 0

        if current is None:
            return None

        while current.value != None:
            if count != index:
                current = current.next
                count += 1
            elif count == index:
                return current.value

        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(1)
    # Space Complexity: ?

    def get_last(self):
        current = self.tail
        if current is None:
            return None

        return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def add_last(self, value):
        current = self.tail
        newNode = Node(value)

        if current == None:
            self.head = newNode
            self.tail = self.head
            self.size += 1
        else:
            current.previous = newNode
            self.tail = newNode
            self.size += 1

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        current = self.head

        if current == None:
            return None

        max_value = 0

        while current:
            if max_value < current.value:
                max_value = current.value
                current = current.next
            else:
                current = current.next

        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def delete(self, value):
        current = self.head
        tail = self.tail

        if current is None:
            return

        if current.value == value:
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1
            return

        if tail.value == value:
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
            return

        current = current.next

        while current:
            if current.value == value:
                current.previous.next = current.next.next
                current.next.previous = current.previous
                self.size -= 1
                return
            current = current.next

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next

        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverse(self):

        current = self.head

        while current:
            temp = current.previous
            current.previous = current.next
            current.next = temp
            current = current.previous

        temptail = self.tail
        temphead = self.head
        self.head = temptail
        self.tail = temphead

    # make head tail - make next none
    # ea node make previous next
    # make tail head - make previous none

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?

    def find_middle_value(self):
        pass

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        pass

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        pass

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head  # make the last node link to first node


test = LinkedList()

test.add_first(1)
test.add_first(2)
test.add_first(3)

test.visit()

test.reverse()

test.visit()
