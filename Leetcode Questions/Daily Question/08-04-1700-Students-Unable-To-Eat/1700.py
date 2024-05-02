def countStudents1(students: list[int], sandwiches: list[int]) -> int:
    circle_lovers = students.count(0)
    square_lovers = students.count(1)
    for sandwich in sandwiches:
        if sandwich == 0: # ie circle sandwich
            if circle_lovers == 0:
                return square_lovers # no one wants what's in front of the stack, here circle - abort
            circle_lovers -= 1
        else: #sandwich == 1 ie square sandwich
            if square_lovers == 0:
                return circle_lovers
            square_lovers -= 1
            
    return 0


def countStudents2(students: list[int], sandwiches: list[int]) -> int:
    cntr = 0
    while True:
        if len(students) == 0:
            return 0
        if len(students) ==  cntr:
            return cntr
        if students[0] == sandwiches[0]:
            cntr = 0
            students.pop(0)
            sandwiches.pop(0)
        else:
            cntr+=1
            students.append(students.pop(0))
            
            
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1] 

print(countStudents1(students, sandwiches))
print(countStudents2(students, sandwiches))           