def solution(num_list):
    num1=1
    num2=0
    for i in range(len(num_list)):
        num1 = num1*num_list[i]
        num2 += num_list[i]
    num2 = num2**2
    if num1<num2:
        return 1
    else:
        return 0