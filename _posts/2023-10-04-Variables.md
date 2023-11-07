---
toc: True
comments: False
title: Variables
type: hacks
courses: {'csp': {'week': 8, 'categories': ['4.A']}}
categories: ['C1.4']
---


```python
exampleString = "this is a string"
print(f"{exampleString} and the name is exampleString")
```

    this is a string  and the name is exampleString



```python
welcomeMsg = "Hello World!"
myAge = 16
isAdult = False
print(f"{welcomeMsg} I am {str(myAge)} years old. Am I an adult? {str(isAdult)}")
```

    Hello World! I am 16 years old. Am I an adult? False



```python
myAge = 16
realAge = myAge
realAge+=1
print(realAge)
```

    17



```python
myClasses = ['USH', 'AP CALC', 'AMLIT', 'CSP', 'AP PHYSICS']
print("My second class is " + myClasses[1])
```

    My second class is AP CALC



```python
evenList = [2,4,6,8,10]
evenNum = []
evenNum = evenList
print(evenNum)
```

    None



```python
# Variable 1

numStudents = 26
#print(numStudents)

#Variable 2

car = "Tesla"
#print(car)

groupMates = ["Nikki", "Monika", "Ankit", "Varun"]
#print(groupMates)

#Variable 4

dogsbeatcats = True
#print(dogsbeatcats)

print(f"Variable 1 = {numStudents} and is an integer")
print(f"Variable 2 = {car} and is a string")
print(f"Variable 3 = {groupMates} and is a list")
print(f"Variable 4 = {dogsbeatcats} and is a boolean")
```

    Variable 1 = 26 and is an integer
    Variable 2 = Tesla and is a string
    Variable 3 = ['Nikki', 'Monika', 'Ankit', 'Varun'] and is a list
    Variable 4 = True and is a boolean



```python
import json
numPets = 1
siblings = ['Anna', 'Grace', 'Michelle']
isAdult = False
name = 'Matthew'
listString = json.dumps(siblings)
x = input('How many siblings do you have?')
if int(x) == len(siblings):
    x = input('Are you an adult?')
    if str(x).lower() == "false":
        print(f"You passed! Your name is {name}, you have {len(siblings)} siblings named {listString}, and your adult status is {isAdult}.")
```

    You passed! Your name is Matthew, you have 3 siblings named ["Anna", "Grace", "Michelle"], and your adult status is False.

