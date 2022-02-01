
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
      self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head:
            return self.head.value
        return None


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def add_first(self, value):
        new_first = Node(value, self.head)
        new_first.next_node = self.head
        self.head = new_first


    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head
        found = False
        while found is False and current is not None:
            if current.value == value:
                found = True
            else:
                current = current.next
        return found


    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length


    # method that returns the value at a given index in the linked list
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        current = self.head
        i = 0
        while i < index and current is not None:
            i += 1
            current = current.next
        if i == index:
            return current.value
        return None


    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        current = self.head
        if not current:
            return None
        while current.next:
            current = current.next
        return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_last = Node(value)
        if self.head is None:
            self.head = new_last
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_last


    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        current = self.head
        if current is None:
            return None
        max = current.value
        while current:
            if max < current.value:
                max = current.value
            current = current.next
        return max


    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # (should be able to be done in O(1) if just getting rid of pointer?)
    # Space Complexity: O(1)
    def delete(self, value):
        current = self.head
        if current:
            if current.value == value:
                self.head = current.next
                current = None
                return
        while current:
            if current.value == value:
                break
            previous = current
            current = current.next
        if current == None:
            return
        previous.next = current.next
        current = None
        

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
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
  

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        if not self.head:
            return None
        
        return self.get_at_index(int(self.length()/2))


    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        current = self.head
        if not current:
            return None
        len = self.length() - 1
        if n > len:
            return
        for i in range(0, len - n):
            current = current.next
        return current.value


    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        current = self.head
        visited = set()
        if current == None:
            return False
        while current.next != None:
            visited.add(current)
            current = current.next
            if current in visited:
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

        current.next = self.head # make the last node link to first node
