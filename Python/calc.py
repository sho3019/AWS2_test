import input

def calc(operation, num1, num2):
    ans = 0

    if(operation == "plus"):
        ans = num1 + num2

    elif(operation == "minus"):
        ans = num1 - num2

    elif(operation == "cross"):
        ans = num1 * num2

    elif(operation == "devision"):
        ans = num1 / num2
    ans = "answer : " + str(ans)
    
    return ans
if(input.error_flag == 0):
    num1 = input.num1
    num2 = input.num2
    error_flag = input.error_flag
    operation = input.operation
    ans = calc(operation, num1, num2)
    print(ans)
else:
    print("error: incorrect input")
#error_flag = 0
#operation = "plus"
#num1 = 1
#num2 = 2

#ans = calc(operation, num1, num2, error_flag)
#print(ans)