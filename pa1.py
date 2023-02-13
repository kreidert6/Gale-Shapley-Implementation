# Name: pa1.py
# Author(s):
# Date:
# Description:

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = QueueNode(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        current_head = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return current_head.data




class LinkedListNode:
    def __init__(self, queue,spots):
        self.queue = queue
        self.num_spots = spots
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, queue,spots):
        new_node = LinkedListNode(queue,spots)
        new_node.next = self.head
        self.head = new_node


def gale_shapley(filename):
    """
    Runs Gale-Shapley algorithm on input
    from file filename.  Format of input file
    given in problem statement.
    Returns a list containing hospitals assigned to each 
    student, or None if a student is not assigned to a hospital.
    """
    #could do linked list for hospitals unmatched
    #queue for each hospitals preference lists?
    #when queue 
    #convert all 
    file = open(filename, 'r')
    line1 = file.readline()
    num_hospital_and_students = line1.split()
    num_hospitals = num_hospital_and_students[0] 
    num_students = num_hospital_and_students[1]

    line2= file.readline().split

    for i in range(len(line2)-1):
        pass


    while():

    
        pass


