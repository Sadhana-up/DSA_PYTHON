#Deque is an abstract data type (pronounce deck) Do not get confused with
# dequeue Operation of a Queue

#We import it for using all of it's functionalitiesss :)

from collections import deque
#Making an array of subjects 

arr = ["DSA","Calc-2","Stats-2","AI"]
deq = deque(arr) ##making a deque data type of arr
#OPERATIONS IN A DEQUE ->
# 1. POPLEFT 2.APPENDLEFT 3.POP(it pops from right ) 4. Append(adds from right)

#Using:
#Append from left
deq.appendleft("R-PRG")
print(deq)

#Pop from left
deq.popleft()
print(deq)

#Append from right 
deq.append("SUBJECTS")
print(deq)

#Pop from right :
deq.pop()
print(deq)

#Some addtional functions:
deq.extend(["Clc-1","Stats 2"]) ##ADDS AT THE END 
print(deq)

deq.rotate() #rotates without order
print(deq)

deq.reverse() #to reverse everything