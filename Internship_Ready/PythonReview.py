# Start here
from pyexpat.errors import messages

print("Hey Gregs Student in Intership Ready")

message = "Welcome to FIU"
print(len(message))
print(message[0])
print(type(message))
print(type(3))
print(type("3"))
print(3*3)
print(3*"3")
print(len("greg")==4)

a = 10
b = 3

print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a//b) # division
print(10/2)
print(a//b) # floor division
print(a**b) # a to the power of b
print(a%b) # modulo

professor = ["greg", "kianoosh", "richard", "patricia", "debra"]
print(professor[0])
print(professor[-1])
professor.append("leo")
print(professor)
professor.extend(["heather", "kevin", "jason"])
print(professor)
professor.insert(2, "trevor")
print(professor)
professor[3] = "mark"
print(professor)
print(professor[3:5]) # accessing professor in positions 2 and 4
print(professor[5:])
print(professor[:3])
print(professor[:]) #interview question what is happening here
print(professor.remove("kianoosh"))
print(professor)
print(professor.index("mark"))
x = professor.pop(6)
print(professor)
print(x)
print(len(professor))
print(type(professor))
professor.sort()
print(professor)
professor.sort(reverse=True)
print(professor)

for i in professor:
    print(i.title())
print("FIU")

water_data = {
    "temperature": [40, 89, 92],
    "pH" : [6.5, 6.7, 6.3],
    "oxygen" : [7.2, 5.6, 3.5],
}

print(water_data["oxygen"])
print(water_data.keys())
print(water_data.values())

import pandas as pd

df = pd.DataFrame(water_data)
print(df)

