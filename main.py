# factorial
def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
print(iterative_factorial(5))


def recur_factorial(n):
    if n == 1:
     return n 
    else:
        temp = recur_factorial(n-1)
        temp = temp * n
    return temp


print(recur_factorial(5))


# permutation
# example 3! = 3*2*1 = 6

def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range((len(string))):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)
print(permute("ABC", ""))


#lesson 2
print("algorithms within data structures")

# dimensional array
# linear search
def search(arr, target):
    for i in range(len(arr)):

        if arr[i] == target:
            return i



arr = [2, 5, 8, 9, 10, 16, 22]
target = 10

print(search(arr, target))


# Binary search
  # itarativ binary search
def binary_itr(arr , start, end, target):
    while start <= end:

        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid

    return start 
    #return -1

arr = [2, 5, 8, 10, 16, 22, 25]
target = 10

result = binary_itr(arr, 0, len(arr) - 1, target)

if result != -1:
    print("elemen is present at index %d" % result)
else:
    print("element is not present in array")


  # recursive binary search
def binary_recur(arr, start, end, target):
    if end >= start:

        mid = start + end - 1 // 2

        if arr[mid] < target:
            binary_recur(arr, min + 1, end, target)

        elif arr[mid] > target:
            return binary_recur(arr, start, mid - 1, target)
        else:
            return -1

arr = [2, 5, 8, 10, 16, 22, 25]
target = 10
result = binary_recur(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")



# Bubble sort
  # bubble sort -optimized VS unoptimized
def bubble_optimized(A):
    iterations = 0
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            iterations += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A, iterations

A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_optimized(A))


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubble_sort_un_op(A):
    iterations = 0 

    for i in A:
        for j in range(len(A)-1):
            iterations += 1
            if A[j] > A[j+1]:
                swap(A, j, j + 1)
    return A, iterations

A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_sort_un_op(A))



# Insertion sort
def insert_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

A = [5, 2, 4, 6, 1, 3]
print(insert_sort(A))


# Linked lists (travese,search,add,deled,header,nodes,tail)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    #pass
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next



family = LinkedList()
family.head = Node("Bob")
wife = Node("Any")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

family.traversal()



#1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    pass



family = LinkedList()
family.head = Node("Bob")
wife = Node("Any")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

#    (family.traversal())



#2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 



family = LinkedList()
family.head = Node("Bob")
wife = Node("Any")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

# family.traversal()
family.insert_new_header("Dave")
# family.traversal()


#3 +list (add)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False

family = LinkedList()
family.head = Node("Bob")
wife = Node("Any")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

# family.traversal()
family.insert_new_header("Dave")
family.traversal()
print(family.search("Bob"))


# 4 delete list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False

    def delete_node(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next


family = LinkedList()
family.head = Node("Bob")
wife = Node("Any")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

family.insert_new_header("Dave")

#family.delet_taili()

#print(family.search("Bob"))
family.delete_node("Bob")
#family.delete_tail()
family.traversal()




#5
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False

family = LinkedList()
family.head = Node("Bob")
wife = Node("Any")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

# family.traversal()
family.insert_new_header("Dave")
family.traversal()
print(family.search("Bob"))




#lesson 3 (eses,benefits and more)
# Merge sort
  # an efficient merge sort
    # 1
A = [-5, -23, 5, 0, 23, -6, 23, 67]
c = []
while A:
    minimum = A[0]
    for x in A:
        if x < minimum:
            minimim = x
    c.append(minimum)
    A.remove(minimum)
print(c)

    # 2
def marging(left, right):
    C = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            insert = right.pop(0)
            C.append(insert)
        elif left[0] <= right[0]:
            insert = left.pop(0)
            C.append(insert)
    if len(left) > 0:
        for i in left:
            C.append(i)
    if len(right) > 0:
        for i in right:
            C.append(i)
    return C

left =[2, 5, 6, 10]
right = [3, 4, 12, 20]
print(marging(left, right))

    # 3
def sortArray(A):
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    left = sortArray(A[:middle])
    right = sortArray(A[:middle])
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.extend(right.pop(0))
    merged.extend(right if right else left)
    return merged
print(sortArray(A))


# getting python to do the work for us with sorted(this data not be executy)
def sortArray(self, nums):
    #brute force merge sort!:
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    left_sorted = []
    while left:
        minimum = left[0]
        for x in left:
            if x < minimum:
                minimum = x
        left_sorted.append(minimum)
        left.remove(minimum)


    right = nums[mid:]
    right_sorted = []
    while right:
        minimum = right[0]
        for x in right:
            if x < minimum:
                minimum = x
        right_sorted.append(minimum)
        right.remove(minimum)

    merged = []
    while left_sorted and right_sorted:
        if left_sorted[0] <= right_sorted[0]:
            merged.append(left_sorted[0])
        else:
           merged.append(right_sorted[0]) 
    merged.extend(right_sorted , left_sorted)
    return marged


#solotion
class Solution(object):
    def sortArray(self, nums):
        #iterative marge sort using SORTED
        mid = len(nums)//2
        left = sorted(nums[:mid])
        right = sorted(nums[mid:])
        C = []
        while mid(len(left), len(right)) > 0:
            if left[0] > right[0]:
                insert = right.pop(0)
                C.append(insert)
        if len(left) > 0:
            for i in left:
                C.append(i)
        if len (right) > 0:
            for i in right:
                C.append(i)
        return C




# Matrix multiplication
# Naive Method: Multiplying two matrices using nested loops
#2X2 matrix "X"
X = [[1, 2],
    [2, 3]]

#2X2 matrix "Y"
Y = [[2, 3],
     [3, 4]]

# 2X2 matrix of "0", which added to our answer, gives the answer
result = [[0, 0],
          [0, 0]]

#iterate though rows of X
for i in range(len(X)):
    # iterate though columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for K in range(len(Y)):
            result[i][j] += X[i][K] * Y[K][j]

for end in result:
      print(end)



# Strassen algorithm
  # Iteration
impotr_numpy as np 

X = np.array([[1, 2], [2, 3]])
Y = np.array([[2, 3], [3, 4]])

def stressena_iter(X, Y):
    
    #splitting the matrices into quadrants, see graphic
    a, b, c, d = X[0, 0], X[1, 0], X[1, 0], X[1, 1]
    e, f, g, h = Y[0, 0], Y[0, 1], Y[1, 0], Y[1, 1]

    # Computting the 7 products - this is where the magic happens!
    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e) 
    p5 = (a + b) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)

    # Computing the values of the 4 quadrants of the final matrix 
    c1 = (p5 + p4 - p2 + p6)
    c2 = (p1 + p2)
    c3 = (p3 + p2)
    c4 = (p1 + p5 - p3 - p7)
    
    return np.array([[c1, c2], [c3, c4]])

print(strassen_iter(X, Y))