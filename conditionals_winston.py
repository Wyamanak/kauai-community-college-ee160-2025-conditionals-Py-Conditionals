#---------------------------------------------------------
# Name: Winston Yamanaka
# File Creation Date: 2025-05-08
# Last Edit Date: 2025-05-08
# Description: messing with conditionals 
#---------------------------------------------------------

# get input from user
stuff = input("type something: ")

# trying to see if it's a number 
try:
    n = float(stuff)  # float just in case it's a decimal
    print("its a number")

    # check if int
    if n.is_integer():  # I saw this on a forum
        print("whole number detected")
        n = int(n)  # easier to work with

        # even or odd??
        if n % 2 == 0:
            print("even number confirmed")
        else:
            print("odd one")

        # now checking if prime but only for small numbers
        if n < 10 and n > 1:
            prime = True
            for x in range(2,n):
                if n % x == 0:
                    prime = False
                    break  # not prime 
            if prime:
                print("probably a prime ")
            else:
                print(" not prime")
    else:
        print("it's not an int, it's a float I guess")

except:
    print("not a number ")

# okay now let's get another one
another = input("type more stuff: ")

# try to add up
try:
    first = float(stuff)
    second = float(another)
    print("adding  gives:", first + second)
except:
    print("can't add these, one of them's not a number")
