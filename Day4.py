#Mohamed Diallo - Day 4: 05/07/2021
#Description: Given a list of numbers, find the maximum and the minimum.

numbers = [3, 2, 4, 8, 10, -5, 7, 6, 5, 20, 9]
maxi, mini = numbers[0], numbers[0]

for i in range(1, len(numbers)):
    if(mini > numbers[i]):
        mini = numbers[i]
    elif(maxi < numbers[i]):
        maxi = numbers[i]

print("The minimum is: ", mini, "\nThe maximum is: ", maxi)

