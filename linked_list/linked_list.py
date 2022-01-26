
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
    # Space Complexity: O(1) - nothing new is being added, so memory is unaffected
    def get_first(self):
        # if the list is empty, return none
        if self.head == None:
            return None
        # if the list is not empty, return the value of the head
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)? Only 1 node is being added, so 0(1) sounds right memory-wise
    def add_first(self, value):
        self.head = Node(value, next_node=self.head)

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n) - traverses the whole list
    # Space Complexity: O(1) - nothing new is being added, so memory is unaffected
    def search(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n) - traverses the list
    # Space Complexity: O(1) - no new node is being added, so memory is unaffected
    def length(self):
        current = self.head
        # set variable to 0, to initiate counter
        list_length = 0
        while current != None: 
            # add to counter 
            list_length += 1
            # set current to next to traverse
            current = current.next
        # return list_length when while loops breaks 
        return list_length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n) - traverses the list to find value
    # Space Complexity: O(1) - no new node is being added, so memory is unaffected
    def get_at_index(self, index):
        current = self.head
        # return None if fewer nodes (can be equal!) than index value
        if index >= self.length():
            return None
        count = 0
        # check count versus index
        while current != None: 
            if count == index: 
                return current.value
            # set current to next 
            current = current.next
            # increment count
            count += 1

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n) - traverses list? 
    # Space Complexity: O(1) - no new node is being added, so memory is unaffected
    def get_last(self):
        current = self.head
        while current != None:
            # if next is None, end of list, so return value
            if current.next == None:
                return current.value
            else: 
                # set current to next, if next != None
                current = current.next
        # if list is empty return None
        return None

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(1) - only inserts 1 value
    # Space Complexity: O(n) - traverses the list in order to find the end, and then adds on value
    def add_last(self, value):
        # can set new_node to head, in the case of an empty list. That value also becomes 'last'
        new_node = Node(value)
        current = self.head
        if current == None:
            self.head = new_node
            return
        # set current to next, while not currently at end of list
        while current.next != None:
            current = current.next
        # set current.next to the new_node
        current.next = new_node

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        # set up an empty variable
        max_value = 0
        current = self.head
        # check if list empty, if so, we can return None
        if current == None: 
            return None
        # when list is not empty, check current value against value in max_value
        # if max_value is less than current value, set max_value to the current value
        while current != None: 
            if max_value < current.value:
                max_value = current.value
            # set current to next to traverse
            current = current.next
        # return max_value when loop breaks
        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n) - traverses list to find specified value
    # Space Complexity: O(1) - deletes only 1 value
    def delete(self, value):
        current = self.head
        previous = None
        # check if list is empty
        if current == None: 
            return
        
        # if not empty...
        while current != None:
            # check current value against passed in value
            if current.value == value:
                # if equal, check to see if end of list
                if current.next == None:
                    previous.next = None
                    return previous
                # set current value equal to the next node value
                current.value = current.next.value
                # set current next to the NEXT node
                current.next = current.next.next
                # continue loop 
                continue
                # return current
            # set previous equal to the current node
            previous = current
            # increment current
            current = current.next
        return current


    # method to print all the values in the linked list
    # Time Complexity: O(n) - traverses list
    # Space Complexity: O(n) - prints out every value
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n) - traverses/reverses entire list
    # Space Complexity: O(1) - no new nodes are being added
    def reverse(self):
        previous = None
        current = self.head
        next_node = current.next
        
        # reversing node order
        while current != None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

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

        current.next = self.head # make the last node link to first node
