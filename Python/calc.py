import input

def calc(error_flag, operation, num1, num2):
    ans = 0

    if (error_flag == 0):
        if(operation == "plus"):
            ans = num1 + num2

        elif(operation == "minus"):
            ans = num1 - num2

        elif(operation == "cross"):
            ans = num1 * num2

        elif(operation == "devision"):
            ans = num1 / num2

        print("answer :" + str(ans))

    else:
        ans = "error: incorrect input"
        print(ans)
    #return ans

ans = calc(input.error_flag, input.operation, input.num1, input.num2)
