# Name: PSA1
# Author(s): Garrett and Tyler
# Date: 2-20-23
# Description: This program takes in hospital and student prefrences for the Gale Shapley Algorithim
#   and outputs stable matchings for hospital-student connections.


#Create a Queue class which will be used later for determining what hospital proposes next
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

def gale_shapley(filename):
    """
    Runs Gale-Shapley algorithm on input
    from file filename.  Format of input file
    given in problem statement.
    Returns a list containing hospitals assigned to each 
    student, or None if a student is not assigned to a hospital.
    """
    #PART 1
    #Get the number of hospitals and number of students
    file = open(filename, 'r')
    line1 = file.readline()
    num_hospital_and_students = line1.split()
    num_hospitals = int(num_hospital_and_students[0]) 
    num_students = int(num_hospital_and_students[1])

    #PART 2
    #grab the number of positions for each hospital and throw them in a dict 
    line2 = file.readline().split()
    
    hospital_positions = {}
    for i in range(num_hospitals):
        hospital_positions[i] = int(line2[i])

    #PART 3
    #creates a dictionary for hostpital preferences 
    #Ex: {"hospital_0" : [0,2,1], "hospital_1" : [2,1,0]}

    hospital_prefs = {}

    result = []
    for i in range(num_hospitals):
        next_line = file.readline().split()
        nums = [int(num) for num in next_line[::-1]]
        result.append(nums)

    for i in range(num_hospitals):
        hospital_prefs[i] = result[i]

    #Part 4
    #Load the student preferences
    student_prefs_2 = loadStudentPreferences(file,num_students,num_hospitals)
    
    #Part 5
    #Get proposal order which is a Queue of hospital numbers
    propose_order = loadProposalOrder(num_hospitals,hospital_positions)

    #Part 6
    #Get matches
    matches = getMatches(hospital_prefs,student_prefs_2,propose_order)

    #Part 7
    #Convert Dict to List
    return_list = convertDictToList(matches,num_students)
    return return_list

def getMatches(hospital_prefs, student_prefs_2, propose_order):
    """
    propose order is queue.
    hostpital_prefs is dictonary of lists.
    student_prefs is dictonary of dictonaries.
    This function is the implementation of the Gale Shapley Algorithim.
    """
    matches = {}

    #determines the current hospital proposing
    #idea use a queue to keep track of hospitals who are proposing
    while (not propose_order.isEmpty()):
        hospital_num = propose_order.dequeue()

        #Check if hospital has proposed to every student in their preference list
        if(len(hospital_prefs[hospital_num])==0):
            continue
        else:
            #grab the hospitals next preference
            student = hospital_prefs[hospital_num].pop()

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
                #student rejects hospital h
                propose_order.enqueue(hospital_num)
    return matches

def loadProposalOrder(num_hospitals,hospital_positions):
    """
    This function takes in int num_hospitals and the hospital_position dictonary 
        and returns a queue where the queue is the order of hospital proposals.
        Each hospital is in the Queue for as many positions they have.
    """
    proposal_order = Queue()
    for hosp_num in range(num_hospitals):
        for i in range(hospital_positions[hosp_num]):
            proposal_order.enqueue(hosp_num)
    return proposal_order

def loadStudentPreferences(file,num_students, num_hospitals):
    """
    This function takes the file, num_students and num_hospitals in as a parameter
    and then loads each students preference into
    a dictonary of dictionaries. The keys are
    student_num and the vals are a dictonary in which
    the keys are the hospitals num and it's ranking
    {student_x : {hospital_x : 1, hospital_z : 2}}
    """
    #Load student pref dict setting all student rankings of every hospital to -1
    student_preferences = {}
    for stu in range(num_students):
        student_preferences[stu] = {}
        for hosp in range(num_hospitals):
            student_preferences[stu][hosp]=-1

    #now load the real preferences in
    for student_num in range(num_students):
        next_line = file.readline().split() 
        #start ranking at 1 and add one per iteration in below loop
        ranking=1
        student_preferences[student_num] = {}
        for hospital_num in next_line:
            hospital_num = int(hospital_num)
            student_preferences[student_num][hospital_num] = ranking
            ranking+=1
    #Now any student that deams a hospital unnaceptable has -1 assigned as its ranking for that hopsital
    return student_preferences


def convertDictToList(matches,num_students):
    """
    This function takes the matches and puts them into the format that is to be compared by test_pa1.py
    """
    return_list = []
    for i in range(num_students):
        if(i not in matches):
            return_list.append(None)
        else:
            return_list.append(matches[i])
    return return_list
