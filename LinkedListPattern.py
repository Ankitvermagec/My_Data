'''
elements = 5
array = [99, 88, 3, 4, 5]
 ___________      ___________      ___________      ___________ 
|      |    |    |      |    |    |      |    |    |      |    |
|  99  |    ---->|  88  |    ---->|  77  |    ---->|  66  |    ---->NULL
|_____ |____|    |_____ |____|    |_____ |____|    |_____ |____|


'''
elements = 5
array = [99, 88, 77, 66, 55]
line1_element = " ___________     " * elements
line2_element = "|      |    |    " * elements
line3_element = ""
for element in array:
    line3_element += "|  "+str(element)+"  |    ---->"
line3_element += "NULL"
line4_element = "|_____ |____|    " * elements

print(line1_element)
print(line2_element)
print(line3_element)
print(line4_element)