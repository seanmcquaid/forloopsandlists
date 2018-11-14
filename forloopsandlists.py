# #For loops

# # # a for loop expects a starting point, and an ending point
# # the ending point is non-inclusive, meaning it will stop when/before it get there

# # i = the thing that we change each time through, does not have to be i
# for i in range(1,10):
#     print i
# # i += 1 is not neccessary

# # a 3rd argument you can hand, is called "step"
# # by default, the step is 1
# for i in range(1,10,2):
#     print i

# # Lists

# # Lists = arrays in any other language
# # a list is a list of variables
# student1 = "Brian"
# student2 = "Brandon"
# student3 = "Zac"
# student4 =  "J.R."

# # print student1
# # print student2
# # print student3
# # print student4

# # a list groups stuff together and indexes them by number
# # a list index always starts at 0
# # a list is made with []
# # when making a list, seperate each index with a comma

# students = [
#     "Brian",
#     "Brandon",
#     "Zach",
#     "J.R"
# ]

# # or

# students = ["Brian","Brandon", "Zach","J.R"]
# # positive number means start from beginning, negative means start from the end
# #print 0 = get first element in list
# print students[0]
# #print -1 = one from the end 
# print students[-1]
# print students[3]
# #print students[4] = error

# teams = [
#    [
#        "Falcons",
#         "Panthers",
#         "Saints",
#         "Bucs",
#         "Bills",
#     ],

#     [
#     "Dolphins",
#     "49ers"
#     ]
# ]

# print teams[0]
# print teams[0][0] # = falcons


# #all lists have a length you can find with len()
# numOfStudents = len(students)
# for i in range(0, numOfStudents):
#     print students[i]

# # a tuple is a list whose elements cannot be changed
# # a tuple is made with () instead of []
# # use a tuple to house data that will not be changed
# students = ("Michael", "Matt", "Cody", "Conner")
# # students[3] = "Connor" = Will create type error because we can't change this

# create an empty list
atlanta_teams = []
#to add something to the end of a list
# use append
atlanta_teams.append("Falcons")
print atlanta_teams
atlanta_teams.append("Braves")
print atlanta_teams
atlanta_teams.append("Hawks")
print atlanta_teams

#insert = inserts an item to a list at the index specified = (index, item)
atlanta_teams.insert(2, "United")

#if you want to remove the last item on the list
# listname.pop(x) removes the xth element
# listname.pop() removes the last item
# use pop
atlanta_teams.pop()
print atlanta_teams
atlanta_teams.append("United")

# a sort method for lists
# will print in natural order
atlanta_teams.sort()
print atlanta_teams

sortedAtlantaTeams = sorted(atlanta_teams)
print sortedAtlantaTeams

# reversesort is the .reverse() method
# will reverse the order
atlanta_teams.reverse()
print atlanta_teams

# if you have a string and want to turn it into a list....
# you can split!
reindeer = "Dasher, dancer, prancer, vixon"
# split expects a delimiter. The delimiter is what you want split to look for
# and each time it finds it, it will create a new element
reindeerAsAList = reindeer.split(", ")
print reindeerAsAList

# If you want part of a list
# you use [x:y]
# this will create a COPY of the array but will not change/mutate the original
# It will start copying at the xth index and it will stop at the yth
# IF we wanted just dancer and prancer
dancerPrancer = reindeerAsAList[1:3]
print dancerPrancer

print atlanta_teams[1:3]