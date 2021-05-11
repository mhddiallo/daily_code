"""
Mohamed Diallo - Day 6: 05/09/2021
Description: Guess the number thas has been fixed. The user only have 5 attempts
"""
def guess_number():
    number, count = 18, 1
    while (count <= 5):
        given_number = int(input("Give a number: "))
        if(given_number > number):
            print(f"It's smaller, {5 - count} attempts left")
        elif(given_number < number):
            print(f"It's bigger, {5 - count} attempts left")
        else:
            print(f"Great! You got it after {count} attempts")
            break
        count += 1

print(guess_number())

            

