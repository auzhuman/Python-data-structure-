# num = 0
# num1 = 1
# for i in range(5):
#     num2 = num+ num1
#     print(num)
#     num = num1
#     num1 = num2
#     # print(num)


# # 0+1 = 1
# # 1+1 = 2
# # 1+2 = 3
class primenumclass:
    def __init__(self,number):
        self.number = number

    def primenum(self):
        flag = 0

        if ( self.number == 1 ):
            # print(self.number, " not a prime self.number")
            flag = 1

        elif(self.number>1):
            for i in range(2,self.number):
            # print(i)

                rem =self.number%i 
                print(self.number ,  "/" ,i,"=",rem)
                if (rem == 0 ):
                    # print(self.number,"not a prime num")
                    flag = 1
                    break 
                # elif (i == self.number-1):
                    # print(self.number,"is a prime num")
        else:
            # print(self.number,"it is not a prime self.number")
            flag = 1

        if flag == 0 :
            print(self.number," is a prime self.number")
        else : 
            print(self.number," is not a prime self.number")

                

num = primenumclass(7)
num.primenum()