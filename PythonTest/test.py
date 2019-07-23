def mult(number):
   mult = number * number
   return mult
print(3*3)
def add(a,b):
    add = a + b
    return add
print(1+3)
#Data structure
numbers = [1,2,3,6]
def sumOfListNumbers(someList):
    index = 0
    for num in numbers:
        index+=num
    return index
print(sumOfListNumbers((1,2,3,6)))
#Assertions to make sure that the values are correct
assert sumOfListNumbers(numbers) == 12
assert mult(3) == 9
assert add(1,3) == 4
