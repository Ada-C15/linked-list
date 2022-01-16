
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

# Defines the singly linked list


class LinkedList:
    def __init__(self):
        self.head = None  # keep the head private. Not accessible outside this class
        self.size = 0

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head is not None:
            return self.head.value
        return None

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        node = Node(value, self.head)
        self.head = node
        self.size += 1

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1) constant space w/ no additional space in memory
    def search(self, value):
        if self.head is None:
            return False
        current = self.head
        while current:  # is not None
            if current.value == value:
                return True
            current = current.next
        return False  # didn't find the value

    # method that returns the length of the singly linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def length(self):
        return self.size
        # current = self.head
        # length = 0
        # while current is not None:
        #     current = current.next
        #     length += 1
        # return length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1) -1

    def get_at_index(self, index):
        if index > self.size - 1:
            return None
        current = self.head
        # -1 index until 0
        while index > 0:
            index -= 1
            current = current.next
        return current.value

    # def get_at_index_no_size(self, index):
    #     current = self.head
    #     while current is not None:
    #         if (index == 0):
    #             return current
    #         current = current.next
    #         index -= 1
    #     return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.size > 0:
            return self.get_at_index(self.size - 1)
        return None

        # if self.head is None:
        #     return None
        # current = self.head
        # while current.next is not None:
        #     current = current.next
        # return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value)
        current = self.head

        if current is None:
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_max(self):
        if self.head is None:
            return None

        current = self.head
        max_value = current.value
        while current is not None:
            if max_value < current.value:
                max_value = current.value
            current = current.next
        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if self.head is None:
            return None
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
        else:
            current = self.head
            found = False
            while current is not None and current.next is not None and not found:
                if current.next.value == value:
                    found = True
                    current.next = current.next.next
                    self.size -= 1
                current = current.next  # didnt find

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
    # Space Complexity: O(1)
    def reverse(self):
        current = self.head  # head is still untouched
        prev_node = None
        next_node = current.next

        while next_node is not None:
            current.next = prev_node

            prev_node = current
            current = next_node
            next_node = next_node.next
        current.next = prev_node
        self.head = current

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def find_middle_value(self):
        middle = self.size//2
        return self.get_at_index(middle)
        # current = self.head
        # slow = self.head
        # advanced = False
        # while current is not None:
        #     current = current.next
        #     if advanced:
        #         advanced = False
        #         slow = slow.next
        #     else:
        #         advanced = True
        # return slow.value

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def find_nth_from_end(self, n):
        fast = self.head
        slow = self.head
        if self.head is None:
            return None
        while fast.next is not None:
            fast = fast.next
            if n <= 0:
                slow = slow.next
            n -= 1
        if n > 0:
            return None  # n is bigger than self.size
        return slow.value

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def has_cycle(self):
        fast = self.head
        slow = self.head
        advance = False
        while fast is not None:
            fast = fast.next
            if advance:
                slow = slow.next
                advance = False
            else:
                advance = True
            if fast == slow:
                return True
        return False

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
