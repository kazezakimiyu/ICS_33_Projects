#Name: Lingling Wang, Xiaohan Zhao, Ruixin Li
#Program 4
#Question 1
import re

string = input()

patterns= ['[A-Z]+']
#accept upper case letters only
    
for p in patterns:
    match= re.findall(p, string)
    #find all p that match the requirement

string1 = ""

for ele in match: 
    string1 += ele
print("Original string:", string)
print("After removing lowercase letters, above string becomes:", string1)
#reference: http://www.learningaboutelectronics.com/Articles/How-to-extract-lowercase-characters-from-a-string-in-Python-using-regular-expressions.php
#print upper case letters out

#Question 2
Prints all nodes of linked list in reverse order

#Quesiton 3
lst = []
class Node:
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):  
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    #function to create elements of the linked list

    def display(self):
        current = self.head
        while(current):
            a = current.data
            lst.append(a)
            current = current.next
    #add all the elements that the user would create from both linked list to an empty list

def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    for i in repeated:
        print(i)
#find repeated elements from the empty list and print it out
        
LL = LinkedList()
n = int(input("How many elements would you like to add for Linked List 1? "))
for i in range(n):
    data = int(input("Enter data item: "))
    LL.insert(data)
LL.display()
LL2 = LinkedList()
n = int(input("How many elements would you like to add for Linked List 2? "))
for i in range(n):
    data = int(input("Enter data item: "))
    LL2.insert(data)
LL2.display()
#to let the user customize their two linked list

Repeat(lst)
#call the function to make it work

#Question 4

class array_integers(object):
    def sum(self, number, target):
        res = {}
        #Define one map to hold the result called res
        for i in range(0, len(number)):
        #For index i in range 0 to n – 1 (where n is the number of elements in the array)
            if target - number[i] in res:
                #if target − A[i] is present in res
                return [res[target - number[i]], i]
                #return res[target − A[i]] and i as indices
            else:
                res[number[i]] = i
                #Otherwise put i into the res as res[A[i]]  = i


if __name__ == "__main__":
    try:
        round = int(input("How many integers you want to have? "))
        input_list = []
        #create a list to hold the number
        for i in range(0, round):
            single_input = int(input("Enter a num to list: "))
            input_list.append(single_input)
            #append the input within the range

        print("The input list: ", input_list)

        test = array_integers()
        total_check = int(input("Which sum you want to check? "))

        print(test.sum(input_list, total_check), end="")
        #test the input.
        print(" = ", total_check)
    except ValueError:
        print("Please enter correct input!")
        pass


#Question 5
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def isBST(mid, prev = None):
    if mid == None:
        return True
    
    if mid.left != None and mid.data <= mid.left.data:
        return False

    if mid.right != None and mid.data >= mid.right.data:
        return False
    
    if prev != None:
        subtrees = 0
        data = []
        if prev.left.left != None:
            subtrees += 1
            data.append(prev.left.left)
        if prev.left.right != None:
            subtrees += 1
            data.append(prev.left.right)
        if prev.right.left != None:
            subtrees += 1
            data.append(prev.right.left)
        if prev.right.right != None:
            subtrees += 1
            data.append(prev.right.right)

        if subtrees == 3:
            if data[0].data < data[1].data < data[2].data:
                pass
            else:
                return False
            
    return isBST(mid.left, mid) and isBST(mid.right, mid)





root = Node(6)
root.left = Node(4)
root.right = Node(19)
root.left.left = Node(3)
root.left.right = Node(8)
root.right.left = Node(5)
 
if isBST(root):
    print("is BST")
else:
    print("not a BST")
