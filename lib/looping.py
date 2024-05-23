#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")
print(happy_new_year())

def square_integers(int_list):
    # code goes here!
    return [i ** 2 for i in int_list]
print(square_integers([1, 2, 3, 4, 5]))

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 ==0 and  i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else :
            print(i)

print(fizzbuzz())
