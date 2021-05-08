#Mohamed Diallo - Day 2: 05/05/2021
#Description: Show how much times an element appear in a given string.

elements = ['a', 'b', 'c', 'd', 'e']
count = 0
my_string = input('Type anything: ')
for i in elements:
    for j in my_string:
        if(i == j):
            count += 1
    print(i +" appears " +str(count)+ " times")
    count = 0
    