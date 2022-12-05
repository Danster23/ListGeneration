print("This is problem 2")
list1 = ["A", "I", "B", "J", "C", "K", "D", "L"]

list2 = ["E", "M", "F", "N", "G", "O", "H", "P"]

list3 = list1 + list2 

list4_dramire6 = []
#[1::2]
for i in range(1, len(list3), 2):
  list4_dramire6.append(list3[i])
    

print(list4_dramire6)