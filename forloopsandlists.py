#For loops

# # a for loop expects a starting point, and an ending point
# the ending point is non-inclusive, meaning it will stop when/before it get there

# i = the thing that we change each time through, does not have to be i
for i in range(1,10):
    print i
# i += 1 is not neccessary

# a 3rd argument you can hand, is called "step"
# by default, the step is 1
for i in range(1,10,2):
    print i

# Lists

# Lists = arrays in any other language
# a list is a list of variables
student1 = "Brian"
student2 = "Brandon"
student3 = "Zac"
student4 =  "J.R."

# print student1
# print student2
# print student3
# print student4

# a list groups stuff together and indexes them by number
# a list index always starts at 0
# a list is made with []
# when making a list, seperate each index with a comma

students = [
    "Brian",
    "Brandon",
    "Zach",
    "J.R"
]

# or

students = ["Brian","Brandon", "Zach","J.R"]
# positive number means start from beginning, negative means start from the end
#print 0 = get first element in list
print students[0]
#print -1 = one from the end 
print students[-1]
print students[3]
#print students[4] = error

teams = [
   [
       "Falcons",
        "Panthers",
        "Saints",
        "Bucs",
        "Bills",
    ],

    [
    "Dolphins",
    "49ers"
    ]
]

print teams[0]
print teams[0][0] # = falcons


#all lists have a length you can find with len()
numOfStudents = len(students)
for i in range(0, numOfStudents):
    print students[i]

