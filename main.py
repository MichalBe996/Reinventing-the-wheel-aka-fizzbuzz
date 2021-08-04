

# fizz buzz


def fizzbuzz(number):
    for x in range(number):
        if x % 3 == 0 and x % 5 == 0:
            print("FIZZBUZZ")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)



fizzbuzz(51)