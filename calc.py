import input



ans = 0
#print(num1)
print(input.error_flag)
print(input.num1)
if (input.error_flag == 0):
    if(input.operation == "plus"):
        ans = input.num1 + input.num2

    elif(input.operation == "minus"):
        ans = input.num1 - input.num2

    elif(input.operation == "cross"):
        ans = input.num1 * input.num2

    elif(input.operation == "devision"):
        ans = input.num1 / input.num2

    #print("answer :" + str(ans))

else:
    ans = "error: incorrect input"

print("answer :" + str(ans))