

# imports





# global vars

prices = [123,2,32,65,6543,879,5,677,2,0,89,65]





# functions

def sum_all(numbers):

    sum = 0
    count = 0
    for price in numbers:
        sum += price
        

        if price < 50:
            count += 1
    print( " The result is " + str(sum))
    print( " The count is " + str(count))


def print_some_nums():
    for i in range(20):
        print(i)

def list_test():
    names = []

    names.append( "joe" ) 
    names.append( "mou" ) 
    names.append( "iss" ) 

    print(names[0])

def sum(str_num1, str_num2):
    num1 = float(str_num1)
    num2 = float(str_num2)
    print(num1 + num2)

def dev(str_num1, str_num2):
    num1 = float(str_num1)
    num2 = float(str_num2)
    if num2 == 0:
       print("Error: you violated the law of math")
    else:
       print(num1 /   num2)
def multi(str_num1, str_num2):
    num1 = float(str_num1)
    num2 = float(str_num2)
    print(num1 * num2)

def subs(str_num1, str_num2):
    num1 = float(str_num1)
    num2 = float(str_num2)
    print(num1 - num2)



      



# plain instructions


# print_some_nums
# sum_all(prices)

num1 = input("Please provide num1: ")
num2 = input("Please provide num2: ")
sum(num1, num2)


num1 = input("Please provide a number: ")
num2 = input("Please Provide a number: ")
dev(num1, num2)


num1 = input("Please provide a number: ")
num2 = input("Please provide a number: ")
multi(num1, num2)

num1 = input("Please provide a number: ")
num2 = input("Please provide a number: ")
subs(num1, num2)