def reverse( x):
    """
    :type x: int
    :rtype: int
    """
    flag = 0
    if x<0:
       x = abs(x)
       flag = 1
    
    num_str = list(str(x))

    for i in range(len(num_str)//2):
        num_str[-i-1],num_str[i] = num_str[i],num_str[-i-1]

    x = int(("".join(num_str)))

    if len(bin(x)[2:]) >= 32:
        return 0
    
    if flag == 1:
        return x * -1
    else :
        return x

print(reverse(120))

print(3//2)