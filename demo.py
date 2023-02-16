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
    #might not need num spots
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
    #PART 1
    #could do linked list for hospitals unmatched
    #queue for each hospitals preference lists?
    #when queue 
    #convert all 
    file = open(filename, 'r')
    line1 = file.readline()
    num_hospital_and_students = line1.split()
    num_hospitals = int(num_hospital_and_students[0]) 
    num_students = int(num_hospital_and_students[1])


    #PART 2
    #grab the positions for each hospital and throw them in a dict 
    line2 = file.readline().split()
    
    hospital_positions = {}
    for i in range(num_hospitals):
        hospital_positions[i] = line2[i]

  


    
    #PART 3
    #creates a dictionary for hostpital preferences 
    #could do a queue cuz its first in first out and load preferences and dequeue them when they propose
    #Ex: {"hospital_0" : [0,2,1], "hospital_1" : [2,1,0]}

    hospital_prefs = {}
    iteration = 0

    result = []
    for i in range(num_hospitals):
        next_line = file.readline().split()
        nums = [int(num) for num in next_line[::-1]]
        result.append(nums)

    for i in range(num_hospitals):
        
        hospital_prefs[i] = result[i]


    

    

    # #PART 4
    # #creates a dictionary for student preferences 
    # #Ex: {"student_0" : [0,2,1], "student_1" : [2,1,0]}
    # student_prefs = {}
    # iteration = 0
    # for i in range(num_students):
    #     next_line = file.readline().split()
    #     pref_list = []
    #     for item in next_line:
    #         pref_list.append[item]

    #     student_prefs["student_" + i] = pref_list

    

    #Part 4 idea 2
    #Tyler- we could use the function below I modified from this if you think it'll work
    student_prefs_2 = loadStudentPreferences(file,num_students)
    



    #matching alg
    matches = {}
    for key in hospital_prefs:
        matches[key] = ""

    #determines the current hospital proposing
    i = 0
    while "" in matches.values():
        student = hospital_prefs[i].pop()

        if matches[i] == "":

            #grab the hospitals next preference
            
            
            #checks if s is unmatched
            if student not in matches.values():
                matches[i] = student
                i += 1
            
            #checks if s prefers h to current partner h'
         
            elif student_prefs_2[student][i] < student_prefs_2[student][list(matches.keys())[list(matches.values()).index(student)]]:
                booted_hosp = list(matches.keys())[list(matches.values()).index(student)]
                matches[booted_hosp] = ""
                matches[i] = student
                i = booted_hosp
            
            #student rejects
            # creating a new dictionary







                
        
        else:
            i += 1
        
     
    print(matches)

   


def loadStudentPreferences(file,num_students):
    """
    This function takes the file and num_student in as a paramter
    and then loads each students preference into
    a dictonary of dictionaries. The keys are
    student_num and the vals are a dictonary in which
    the keys are the hospitals num and it's ranking
    """
    #{student_x : {hospital_x : 1, hospital_z : 2}}
    student_preferences = {}
    for student_num in range(num_students):
        next_line = file.readline().split()  
        #start ranking at 1 and add one per iteration in below loop
        ranking=1
        student_preferences[student_num] = {}
        for hospital_num in next_line:
            hospital_num = int(hospital_num)
            
            
            student_preferences[student_num][hospital_num] = ranking
            ranking+=1
    
 
    return student_preferences


gale_shapley("input2.txt")
