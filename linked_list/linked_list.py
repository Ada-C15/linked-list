
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
    # Time Complexity: O(1)/constant
    # Space Complexity: O(1)/constant
    def get_first(self):
        if self.head == None:
            return None
        
        return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)/constant
    # Space Complexity: O(1)/constant
    def add_first(self, value):
        
        #create a new node
        new_node = Node(value) 
        #set the new node to point to the current head
        # new_node.next = self.head
        # #Assign the new node to the head variable
        # self.head = new_node

        #How could this be performed in one line?
        self.head = Node(value, next_node=self.head)

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: o(n)/linear complexity
    # Space Complexity: o(n)/linear complexity
    def search(self, value):

        if self.head == None:
            return False

        current_node = self.head
        while current_node.next != None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        
        if current_node.value == value:
            return True
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: o(n)/linear complexity
    # Space Complexity: o(n)/linear complexity
    def length(self):
        count = 0
        current_node = self.head

        while current_node != None:
            count = count + 1
            current_node = current_node.next
        
        return count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: o(n)/linear complexity
    # Space Complexity: o(n)/linear complexity
    def get_at_index(self, index):
        current_node = self.head
        count = 0

        while current_node != None:
            if count == index:
                return current_node.value

            count += 1
            current_node = current_node.next
        
        return None


    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: o(n)/linear complexity
    # Space Complexity: o(n)/linear complexity
    def get_last(self):
        
        #make sure list is not empty
        if self.head == None:
            return None

        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        
        return current_node.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_last(self, value):
        new_node = Node(value)

        if self.head == None: 
            self.head = new_node
            return 
        else:
            current_node = self.head

            while current_node.next != None:
                current_node = current_node.next
                
            current_node.next = new_node 

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        
        current_node = self.head

        if self.head == None: 
            return None

        list_values = []
        max_val = None
        while current_node != None:
            list_values.append(current_node.value)
            current_node = current_node.next

        max_val = max(list_values)
        return max_val

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        temp = self.head
        prev = self.head

        if self.head == None: 
            return None

        if temp.value == value:
            if temp.next is None:
                return None
            else:
                temp.value = temp.next.value
                temp.next = temp.next.next
        

        while temp.next is not None and temp.value != value:
            prev = temp
            temp = temp.next

        if temp.next is None and temp.value != value:
            prev = temp
            temp = temp.next
        
        elif temp.next is None and temp.value == value:
            prev.next = None

        else:
            prev.next = temp.next    

    # method to print all the values in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: ?
    # Space Complexity: ?
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev 

 
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
    
    # def print_list(self):

    #     current = self.head
    #     while current != None:
    #         print(current.data)
    #         current = current.next


# ll = LinkedList()
# ll.add_first(2)
# ll.add_first(4)
# ll.add_first(6)
# ll.add_first(7)
# ll.print_list()

# # Examples from Learn
# # Create head node
# head = Node('node1')

# # Create another node to link
# other_node = Node('node2')


# # To link them together:
# head.next = other_node

# # To link other_node to other_node
# other_node = Node('node3')
# head.next.next = other_node

# # to print with a statement 
# print(head.data)
# print(head.next.data)
# print(head.next.next.data)

# #print with a loop
# current = head

# while current != None:
#     print(current.data)
#     current = current.next