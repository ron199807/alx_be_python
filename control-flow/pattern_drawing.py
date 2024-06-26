# pattern draw

# prompting user for size of the pattern
size = int(input("Enter the size of the pattern: "))

# validate positive interger input
while size <= 0:
    print("please enter a positive integer." )
    size = int(input("Enter the size of the pattern: "))
    
    # draw the square pattern
    row = 0
    while row < size:

        # print asterrisks in a row without going to the nex line
        for column in range(size):
            print("*", end="")

            #move to next line
            print()
            row += 1
