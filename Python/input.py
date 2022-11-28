import sys

args = sys.argv

error_flag = 0
for i in range(1, len(args) - 1):
    st = len(args[i])
    if("0" <= args[i][0] <= "9" or args[i][0] == "-"):
        pass
    else:
        error_flag = 1

    for n in range(1, st):
        
        if("0" <= args[i][n] <= "9"):
            pass
        else:
            error_flag = 1
            break
    
if(error_flag == 0):
    num1 = int(args[1])
    num2 = int(args[2])
    operation = args[3]
        

