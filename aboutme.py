first_name = "Camilla"
last_name = "Chepkirui"
age = 21
height = 154
weight = 47
university = "EUL"
course = "software engineering"

def myfunc():
    global course
    course = "Information tech"
myfunc()
print("FIRST_NAME:",first_name)
print("LAST_NAME:",last_name)
print("AGE:",age)
print("HEIGHT:",height)
print("WEIGHT:",weight)
print("UNIVERSITY:",university)
print("COURSE:",course)
