import sys

sys.path.append("/input")
import input as i

if(i.error_flag == 0):
    num1 = i.num1
    num2 = i.num2
    operation = i.operation

    ans = 0

    if(operation == "plus"):
        ans = num1 + num2

    elif(operation == "minus"):
        ans = num1 - num2

    elif(operation == "cross"):
        ans = num1 * num2

    elif(operation == "devision"):
        ans = num1 / num2

else:
    ans = "error: incorrect input"

print("answer :" + str(ans))