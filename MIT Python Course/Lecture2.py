#lecture 2

"""
Strings
    sequence of case-sensitive letters and any character counts include tab space digits etc
        enclosed in single quotations or double quotes

        a = "me"
        z = 'you'

    Concatenate and repeat strings
        b = "myself"
        c = a + b           c = "memyself"
        d = a + " " + b     d = " me myself"
        silly = a * 3       silly = "mememe"

        b = ":"
        c = ")"
        s1 = b + 2*c  s1 = :))

        f = "a"
        g = " b"
        h = "3" (string three)
        s2 = (f+g)*((int)h) (integer three)
           = "a ba ba b"

        If the 3 was not type casted a type error would appear

        len() is a function that tells us the length of a string inside the parenthesis
        s = "abc"
        length = len(s)
        length = 3!

    Slicing
        grabbing a char from a string
            s + "abc"
            s[0] = "a"
            s[1] = "b"
            s[2] = "c"
            s[3] = out of bounds error

            you can also use negative indices
            s[-1] = "c"

            slicing to get a substring
                [start:stop:step]
                get characters at start up to and including stop-1 taking every step characters

                if given [start:stop] then step is automatically 1

                if given one number, you are back to indexing for the character at one location

                you can also omit numbers and leave just colons

                when using a positive step you read left to right and when using a negative step you read right to left

                s = "abcdefgh"

                s[3:6] = "def"
                s[3:6:2] = "df"
                s[4:1:-2] = "ec"
                s[:] = "abcdefgh"
                s[::-1] = "hgfdecba"

    immutable strings
        strings are immutable - cannot be modified

        you can create new objects that are versions of the original one

        variable name can only be bound to one object

        s = "car"
        s[0] = "b"  (gives an error)
        s = 'b'+s[1:len(s)]  (is allowed, s is bound to a new object)

    Input/Output
        printing
            used to output something to the console

            print(3+2) => 5
                must be same type to concatenate
                ex: print("a" + 3) Fail         print("a"+"3") SUCCESS

        Input
            x = input(s)
                prints the value of string s
                user types in a value and hits enter
                that value is assigned to the variable x

                text = input("Type anything: ")
                print(5*text)

                input will always return a string and you must type cast if you're expecting a different object type

    Newtons Method
        Find roots of a polynomial
            find g such that f(g,x) = g^3 - x = 0

        Algorithm uses succesive apporoximation
            next_guess = guess - f(guess)/f^1(guess)
            partial code:
                x = int(input("what x: ")
                g = int(input("what is your starting guess?: ")
                print("current estimate cubed= ", g**3)
                next_g = g - (g**3-x)/(3g**2))
                print("next guess to try = ", next_g)

     F-Strings
        available starting python 3.6
        character f followed by a formatted string literal
            anything that can be appear in a normal string literal

            expressions bracketed by curly braces {}

        Expressions in curly braces evaluated at runtime, automatically converted to strings, and concatenated to the string preceding them

        num =3000
        fraction = 1/3
        print(num*fraction, 'is', fraction*100, '% of', num)    =>    print(num*fraction, 'is', str(fraction*100), '% of', num)   =>    print(f'{num*fraction} is {fraction*100}% of {num}')

    Binding variables and Values
        In CS there are two notions of equal
            variable = value

            some expression == other expression
                this is a boolean in other words a true or false statement rather than assigning a given value and does not assign any value, only returns true or false

    Comparison Operators
        includes:
             >
             <
             >=
             <=
             ==
             !=

    Logical Operators
        a or b, true false, true
        a or b, false false, false
        a or b, false true, true
        a or b, true true, true

        a and b, true false, false
        a and b, false false, false
        a and b, false true, false
        a and b, true true, true

    Branching
        if
        else
        elseif (elif)
        while
        for

        indentation matters in python



"""
def main():
    verb = input("Choose a verb: ")
    print("I can "+verb+" better than you")
    print((verb+" ")*4 + verb)


main()