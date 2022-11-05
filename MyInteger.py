class MyInteger:
    # value = 0
    def __init__(self, value : int) ->None:
        self.__value = value
    #getter method
    def getValue(self) -> int:
        return self.__value
    #setter method
    def setValue(self, value : int) -> None:
        self.__value = value

    def iseven(self)-> bool:
        if self.__value % 2 == 0:
            return True

    def isodd(self)-> bool:
        if self.__value % 2 == 1:
            return True

    def isprime(self)-> bool:
        num = self.__value
        if num > 1:
        # Iterate from 2 to n / 2
            for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    break
                else:
                    print(num, "is a prime number")
                    return True
        else:
            print(num, "is not a prime number")

    def add(self, other: 'MyInteger')->int:
        #that adds the value of the other object to the value of the self object.
        sum = self.__value + other.__value
        return  sum

    def sub(self, other : 'MyInteger')->int:
        #subtracts the value of the other object from the value of the self object
        return self.__value - other.__value  

    def __eq__(self, other : 'MyInteger')->bool:
        #returns true if the value in the self object is equal to the value of the other object.  
        if self.__value == other.__value:
            return True    

    def __gt__(self, other : 'MyInteger')->bool:
        # implementation of > operator. If the value of the self object
        # is greater than thevalue of the other object, it returns true otherwise false.  
        if self.__value > other.__value:
            print(str(self.__value) + " is greater than "+ str(other.__value))
            return True 
        else:
            print(str(self.__value) + " is smaller than "+ str(other.__value))
            return False

    def __str__(self) -> str:
        return " Number = {} ".format(self.__value)

    def __str__(self) -> str:
        return "Number = " + str(self.__value)
def main() -> None:
    number = MyInteger(22)
    num = number.getValue()
    print(str(number))
    if number.iseven():
        print( str(num) + " is an Even number")
    if number.isodd():
        print( str(num) + " is an odd number")
    number.isprime()
    number2 = MyInteger(97)
    num2 = number.getValue()
    print(number2)
    if number2.iseven():
        print( str(num2) + " is an Even number")
    if number2.isodd():
        print( str(num2) + " is an odd number")
    number2.isprime()
    sum = number2.add(number)
    print("Addition = " + str(sum) )
    sub = number2.sub(number)
    print("Subtraction = " + str(sub))
    if number.__eq__(number2):
        print("Equal")
    elif number.__gt__(number2):
        print("Greater Than")
    else:
        print("not equal")

if __name__ == '__main__':
    main()