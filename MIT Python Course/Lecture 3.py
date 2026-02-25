"""
Lecture 3

Control Flow: while loops
    while(condition):
        inner code
    condition evaluates to a boolean, if true it continues, if false it stops, loops over and over again

    Example
            where = input("Go left or Right")
            while(where == "Right"):
                where = input("Go left or Right")
            print("you got out of the forest")

            This is case-sensitive

            n = int(input("Enter a non-negative integer: "))
            while(n > 0):
                print('x')
                n = n - 1

            missing the n-- will make the code run forever

            A Common Pattern

            find 4!
            i is the loop variable
            factorial tracks product
            while i<=x:
                factorial*=i
                i+=1
            print(f'{x} factorial is {factorial}')

Structure of For Loops
    for variable in sequence of values:
        code

        each loop the variable takes value ++ or --

    EX:
        for n in range(5):     (range(5) means 0 => 4 not including 5)
            print(n)

    Range
        range(start,stop,step)
            start: first int generated
            stop: last int generated going up to int but not including
            step: generate next int in sequence
        Like slicing

        Often Omit start and stop
            for i in range(4)
            or
            for i in range(3,5)
            or
            for i in range(3,5,2)

    Running Sum
        mysum is a variable to store the runing sum
        range(10) makes i be 0 then 1 then 2 then n

        mysum= 0
        for i in range(10):
            mysum = mysum + i or mysum++ or mysum += 1
        print(mysum)



"""

