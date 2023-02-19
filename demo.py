# Name: pa1.py
# Author(s):
# Date:
# Description:

class Queue:
    class Node:
        def __init__(self, value,next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = self.Node(value)
        if self.rear is None:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        else:
            value = self.front.value
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return value
        
    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False
    def getNumPositions(self):
        return self.num_positions



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
    student_prefs_2 = loadStudentPreferences(file,num_students,num_hospitals)
    




        

    propose_order = loadProposalOrder(num_hospitals,hospital_positions)
    
    matches = getMatchesMach2(hospital_prefs,student_prefs_2,propose_order,hospital_positions)
    #print(matches)
    return_list = convertDictToList(matches)
    #print(return_list)
    return return_list

def getMatchesMach2(hospital_prefs, student_prefs_2, propose_order,hospital_positions):
    #propose order is queue
    #hostpital_prefs is dictonary of lists
    #student_prefs is dictonary of dictonaries
    #{student_num: hospital}

    #change matches to be 
    #matching alg
    matches = {}

    #determines the current hospital proposing
    #idea use a queue to keep track of hospitals who are proposing
    while (not propose_order.isEmpty()):
        hospital_num = propose_order.dequeue()

        student = hospital_prefs[hospital_num].pop()

        #grab the hospitals next preference
        
        
        #checks if s is unmatched
        if student not in matches:
            matches[student] = hospital_num
        
        #checks if s prefers h to current partner h'
        
        elif student_prefs_2[student][hospital_num] < student_prefs_2[student][matches[student]]:
            booted_hosp = matches[student]
            propose_order.enqueue(booted_hosp)
            del matches[student]
            matches[student] = hospital_num
        else:
            propose_order.enqueue(hospital_num)
        
        #student rejects
        # creating a new dictionary

    return matches

def loadProposalOrder(num_hospitals):
    proposal_order = Queue()
    for hosp_num in range(num_hospitals):
        proposal_order.enqueue(hosp_num)
    return proposal_order


def getMatchesMach1(hospital_prefs, student_prefs_2):
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
    return matches

def loadStudentPreferences(file,num_students, num_hospitals):
    """
    This function takes the file and num_student in as a paramter
    and then loads each students preference into
    a dictonary of dictionaries. The keys are
    student_num and the vals are a dictonary in which
    the keys are the hospitals num and it's ranking
    """
    #preload for num students a dictonary of 0-num_students where key is hosp_num and val is 1
    #when loading preferences del the key value pair so that any pair in the dict at the end of loop any val still in dict
    #initialize in hospital_prefs as -1
    #{student_x : {hospital_x : 1, hospital_z : 2}}
    unacceptable_dict = {}
    for stu in range(num_students):
        unacceptable_dict[stu] = {}
        for hosp in range(num_hospitals):
            unacceptable_dict[stu][hosp]=-1
    student_preferences = {}
    for student_num in range(num_students):
        next_line = file.readline().split()  
        #start ranking at 1 and add one per iteration in below loop
        ranking=1
        student_preferences[student_num] = {}
        for hospital_num in next_line:
            hospital_num = int(hospital_num)
            del unacceptable_dict[student_num][hospital_num]
            student_preferences[student_num][hospital_num] = ranking
            ranking+=1
    for student in unacceptable_dict:
        for hospital in unacceptable_dict[student]:
            student_preferences[student][hospital] = -1
    
 
    return student_preferences

def convertDictToList(matches):
    return_list = []
    # for i in range(num_hospitals):
    #     print(print_list.append(matches[i]))
    # print(print_list)
    for i in range(len(matches)):
        return_list.append(matches[i])
    return return_list



my_list = gale_shapley("input5.txt")
file = open("solution5.txt", 'r')
solution_list_string = file.readline().split()
solution_list = [int(i) for i in solution_list_string]
print(my_list)
print(solution_list)
if(my_list==solution_list):
    print("The lists are equal")
else:
    print("The lists are not equal")

