
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# Defines the singly linked list
class LinkedList:
    def __init__(self):
      self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head == None:
            return None
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        self.head = Node(value, self.head)

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        current = self.head
        len = 0
        while current != None:
            len += 1
            current = current.next
        return len

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        current = self.head
        count = 0
        while current != None:
            if count == index:
                return current.value
            current = current.next
            count += 1
        return None


    def get_last_node(self):
        if self.head == None:
            return None
        current = self.head
        while current.next != None:
            current = current.next
        return current


    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        last_node = self.get_last_node()
        if last_node == None:
            return None
        else:
            return last_node.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        current = self.head
        if current == None:
            self.head = Node(value)
        else:  
            last_node = self.get_last_node()
            last_node.next = Node(value)

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_max(self):
        current = self.head
        if current == None:
            return None
        max = current.value
        while current != None:
            if current.value > max:
                max = current.value
            current = current.next
        return max

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if self.head == None:
            return None
        elif self.head.value == value:
            self.head = self.head.next

        current = self.head
        previous = None

        while current != None:
            if current.value == value:
                previous.next = current.next
            else:
                previous = current
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
    # Space Complexity: O(1)
    def reverse(self):
        if self.head == None:
            return None
        
        previous = None
        current = self.head
        temp = self.head

        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous

  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        middle = self.length()//2
        return self.get_at_index(middle)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        if self.head == None:
            return None
        elif self.length() < n:
            return None

        counter = 1
        current = self.head

        while counter < n and current != None:
            current = current.next
            counter += 1
        
        if current == None:
            return None
        
        temp = self.head
        while current != None:
            temp = temp.next
            current = current.next
        
        return temp.value




    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        if self.head == None:
            return False
        if self.length() == 1:
            return False
            
        step1 = self.head
        step2 = self.head

        while step1 != None and step2 != None:
            step1 = step1.next
            step2 = step2.next.next
            if step1 == step2:
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
