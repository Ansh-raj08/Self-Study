
# # Check Armstrong number
# # def is_armstrong_number(num):
# #     """Return True if num is an Armstrong number, else False.

# #     An Armstrong number equals the sum of its digits raised to
# #     the power of the number of digits. Example: 153 -> 1^3+5^3+3^3 = 153
# #     """
# #     # work with positive integers only
# #     if num < 0:
# #         return False
# #     s = str(num)
# #     power = len(s)
# #     total = 0
# #     for ch in s:
# #         digit = int(ch)
# #         total += digit ** power
# #     return total == num


# # # Example tests (you can run and then try your own numbers)
# # print('\n=== Armstrong Number Tests ===')
# # tests = [153, 9474, 407, 123, 1, 0]
# # for t in tests:
# #     print(f"{t}:", "Armstrong" if is_armstrong_number(t) else "Not Armstrong")

# # # Interactive check
# # while True:
# #     val = input('\nEnter a positive integer to check (or type quit to exit): ')
# #     if val.strip().lower() in ('q', 'quit', 'exit'):
# #         print('Exiting Armstrong checker.')
# #         break
# #     if not val.strip().lstrip('-').isdigit():
# #         print('Please enter a valid integer.')
# #         continue
# #     n = int(val)
# #     if is_armstrong_number(n):
# #         print(f"{n} is an Armstrong number.")
# #     else:
# #         print(f"{n} is NOT an Armstrong number.")
# # DATA TYPE CHECK
# # innt = 5.5
# # print(type(innt))

# # DATA TYPE CONVERSION
# # num = 5 
# # convnum = float(num)
# # print(type(convnum))
# # print(convnum)
# # stri = "123"
# # constr = int(stri)
# # print(type(constr))

# # gemini

# # a = 5
# # total_sum = 0

# # for i in range(1, a+1):
# #     total_sum = total_sum + i

# # print(total_sum)

# # Reverse the digits

# # n = 12345
# # r = 0

# # while n > 0:
# #     last_digit = n % 10
# #     r = r * 10 + last_digit
# #     n = n // 10
# # print(r)

# # Even no. counter
# # sam = [1,2,3,4,5,6,7,8,9,10]

# # for num in sam:
# #     if num % 2 == 0:
# #         print(num)

# # To print 1 to 100 using while loop
# # i = 1
# # while i <= 100:
# #     print(i)
# #     i += 1

# # reverse countdown problem
# # n = 100
# # while n >= 0:
# #     print(n)
# #     n -= 1

# # Factorial calculator [Ex. 5! = 5x4x3x2x1]
# # N = int(input("Enter Number: "))
# # fact = 1
# # while N >= 1:
# #     fact = fact * N
# #     N -= 1
# # print(fact)

# # FizzBuzz Logic: Loop from 1 to 20.
# # If the number is divisible by 3, print "Fizz".
# # If divisible by 5, print "Buzz".
# # If divisible by both, print "FizzBuzz".
# # Otherwise, print the number.
# # N = 1
# # while N <= 20:
# #     if (N % 3 == 0) and (N % 5 == 0):
# #         print(f"{N} is FizzBuzz")
# #     elif N % 5 == 0:
# #         print(f"{N} is Buzz")
# #     elif N % 3 == 0:
# #         print(f"{N} Fizz")
# #     else:
# #         print("Nothing")
# #     N += 1

# # check if palindrome
# # n = int(input("enter a number: "))
# # m = n
# # pal = 0
# # while n > 0:
# #     digit = n % 10
# #     pal = (pal * 10) + digit
# #     n = n // 10
# # if pal == m:
# #     print("palindrome")
# # else:
# #     print("not a palindrome")

# # reverse a number

# # n = int(input("enter a number: "))
# # rev = 0
# # while n > 0 :
# #     digit = n % 10
# #     rev = ( rev * 10 ) + digit
# #     n = n // 10
# # print(rev)

# # Basic Stack Implementation for BCA Students

# class Stack:
#     def __init__(self, max_size=None):
#         # Initialize an empty list to store stack elements
#         self.stack = []
#         # Optional maximum size for the stack (for overflow demonstration)
#         self.max_size = max_size

#     def push(self, item):
#         # Check if stack is full before adding item
#         if self.is_full():
#             return "Stack overflow - Cannot add more items"
#         # Add item to the end of the list (top of stack)
#         self.stack.append(item)
#         return "Item added successfully"

#     def pop(self):
#         # Check if stack is empty before removing item
#         if self.is_empty():
#             return "Stack underflow - No items to remove"
#         # Remove and return the last item (top of stack)
#         return self.stack.pop()

#     def peek(self):
#         # Check if stack is empty before viewing top item
#         if self.is_empty():
#             return "Stack underflow - No items to view"
#         # Return the last item without removing it
#         return self.stack[-1]

#     def is_empty(self):
#         # Return True if stack has no elements
#         return len(self.stack) == 0

#     def is_full(self):
#         # Return True if stack has reached maximum size
#         return self.max_size is not None and len(self.stack) >= self.max_size

#     def size(self):
#         # Return the number of items in the stack
#         return len(self.stack)

# # Example usage for understanding stack operations
# print("=== Stack Operations Demo ===")
# s = Stack(max_size=3)  # Create stack with maximum 3 items

# print("\n1. Pushing items:")
# print("Push 1:", s.push(1))
# print("Push 2:", s.push(2))
# print("Push 3:", s.push(3))
# print("Push 4 (should overflow):", s.push(4))

# print("\n2. Checking stack status:")
# print("Stack size:", s.size())
# print("Top element (peek):", s.peek())

# print("\n3. Popping items:")
# print("Pop:", s.pop())
# print("Pop:", s.pop())
# print("Pop:", s.pop())
# print("Pop (should underflow):", s.pop())

# print("\n4. Final status:")
# print("Stack size:", s.size())
# print("Is empty:", s.is_empty())


# ---------------------------
# Beginner-friendly Stack and Queue tutorials
# ---------------------------

# STACK - Explanation:
# A stack follows LIFO (Last In, First Out). The last item added
# is the first one removed. Think of a stack of plates: you add/remove
# plates only from the top.

# Time complexities (for this simple list-based implementation):
# push: O(1), pop: O(1), peek: O(1), is_empty: O(1), display: O(n)

# class StackTutorial:
# 	"""Simple Stack implementation using Python list.

# 	Designed for 2nd-semester BCA students: clear comments and simple methods.
# 	"""
# 	def __init__(self):
# 		# Use a list; the end of the list is the top of the stack
# 		self.items = []

# 	def push(self, item):
# 		# Add item to top -> O(1)
# 		self.items.append(item)

# 	def pop(self):
# 		# Remove and return top item -> O(1)
# 		if self.is_empty():
# 			return None  # Underflow: no items to pop
# 		return self.items.pop()

# 	def peek(self):
# 		# Return top item without removing -> O(1)
# 		if self.is_empty():
# 			return None
# 		return self.items[-1]

# 	def is_empty(self):
# 		# True if stack has no elements -> O(1)
# 		return len(self.items) == 0

# 	def display(self):
# 		# Return a copy of stack from bottom to top -> O(n)
# 		return self.items[:]


# def stack_tutorial_demo():
# 	# Simple demo showing how stack works
# 	print('\n=== Stack Tutorial Demo ===')
# 	st = StackTutorial()
# 	print('Push 10')
# 	st.push(10)
# 	print('Push 20')
# 	st.push(20)
# 	print('Push 30')
# 	st.push(30)
# 	print('Current stack (bottom->top):', st.display())
# 	print('Peek (top item):', st.peek())
# 	print('Pop (removes top):', st.pop())
# 	print('After pop:', st.display())


# QUEUE - Explanation:
# A queue follows FIFO (First In, First Out). The first item added
# is the first one removed. Think of a line of people: the first person
# to join the line is the first to be served.

# Time complexities (list-based):
# enqueue (append at end): O(1), dequeue (pop from front): O(n) because pop(0) shifts
# peek: O(1), is_empty: O(1), display: O(n)

# class QueueTutorial:
# 	"""Simple Queue implementation using Python list.

# 	This is beginner-friendly. For large queues, `collections.deque` is better,
# 	but here we use list so you understand the basics.
# 	"""
# 	def __init__(self):
# 		# Use a list where index 0 is the front of the queue
# 		self.items = []

# 	def enqueue(self, item):
# 		# Add item at the rear (end) -> O(1)
# 		self.items.append(item)

# 	def dequeue(self):
# 		# Remove and return front item -> O(n) with list.pop(0)
# 		if self.is_empty():
# 			return None  # Underflow: no items to remove
# 		return self.items.pop(0)

# 	def peek(self):
# 		# View front item without removing -> O(1)
# 		if self.is_empty():
# 			return None
# 		return self.items[0]

# 	def is_empty(self):
# 		# True if queue has no elements -> O(1)
# 		return len(self.items) == 0

# 	def display(self):
# 		# Return a copy of queue from front to rear -> O(n)
# 		return self.items[:]


# def queue_tutorial_demo():
# 	# Simple demo showing how queue works
# 	print('\n=== Queue Tutorial Demo ===')
# 	q = QueueTutorial()
# 	print('Enqueue A')
# 	q.enqueue('A')
# 	print('Enqueue B')
# 	q.enqueue('B')
# 	print('Enqueue C')
# 	q.enqueue('C')
# 	print('Current queue (front->rear):', q.display())
# 	print('Peek (front):', q.peek())
# 	print('Dequeue (removes front):', q.dequeue())
# 	print('After dequeue:', q.display())


# # Note for students:
# # To run the tutorial demos, call `stack_tutorial_demo()` and `queue_tutorial_demo()`
# # at the bottom of this file or from a Python REPL. They are NOT called automatically
# # to avoid interrupting the existing interactive Armstrong checker in this file.

# creating an empty stack
stack = []

# push operation
def push():
    element = int(input("Enter element to push: "))
    stack.append(element)
    print("Element pushed")

# pop operation
def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print("Popped element:", stack.pop())

# peek operation
def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

# display stack
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:", stack)

push()
pop()
pop()
display()



n = int(input("enter no : "))
rev = 0

while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10

print("reversed no: ",rev)

n= int(input("enter no: "))
temp = n
rev =0

while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp ==rev:
    print("palindrome")
else:
    print("not palindrome")


n= int(input("enter no: "))
temp=n
sum = 0
digit = len(str(n))

while n>0:
    digit=n%10
    sum += digit * digit 
    n=n//10

if sum == temp:
    print("armstrong no ")
else:
    print("not armstrong ")

n = int(input("enter no: "))
binary = " "

while n>10:
    binary = str (n%2)+binary
    n=n//2

print ( "binary no: ",binary)

arr = [1,2,3,3,4]
for i in range(0,len[arr],2):
 print (arr[i])

arr = [1,2,3,4]
sum = 0
product = 1

for i in arr:
    sum += 1
    product *= 1

    print("sum: ", sum)
    print("product: ", product)

arr = [1,2,3,4,5]
if arr == Sorted(arr):
    print("sorted forward")
elif arr == sorted(arr,reverse=true):
    print("sorted backward")
else:
    print("not sorted") 

arr=[1,2,3,4]

distinct=list(set(arr))
print(distinct)



 

