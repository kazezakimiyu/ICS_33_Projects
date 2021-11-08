def bubblesort(array):
    for i in range(
        len(array) - 1, 0, -1
    ):  # from lenght of the array - 1 to the 0 with -1 each loop.
        for j in range(0, i): #from 0 to range of the i.
            if array[j] > array[j + 1]: #compare the two number
                new_array = array[j]
                # to store the array j without affect the line below
                array[j] = array[j + 1]
                # store the array in the back to the front
                array[j + 1] = new_array
                # store the number in the array that in the back replace with the number in the front.


if __name__ == "__main__":
    try:
        test_round = int(input("How many number do you want to enter to the array? "))
        if test_round >= 1:
            test_array = []  # store the input number
            for i in range(0, test_round):
                test_array_enter = int(input("Please Enter: "))
                test_array.append(test_array_enter)
            print("Inital Array: ", test_array) #print initial array
            bubblesort(test_array)
            print("Bubble Sort Array: ", test_array) #print sort array.

        else:
            print("You enter a number euqal or lower than 0. Please try again! ")
            pass
            #consider the value enter for the input.

    except ValueError:
        print("Enter invalid input, please try again!")
        pass
        #consider the value error with invalid input


def count(array, length, summ):
    #if the goal sum is equal to 0, the only solution is include no coin
    if summ == 0:
        return 1

    #if the goal sum is less than 0, there is no solution at all
    if summ < 0:
        return 0
    
    #if the length of array is less or equal to 0(no coin) and goal sum is greater than 1
    #the only solution is 0 since there is no coin
    if length <= 0 and summ >= 1:
        return 0

    #other than exceptions, get the count of sums
    return count(array, length - 1, summ) + count(
        array, length, summ - array[length - 1]
    )


if __name__ == "__main__":
    try:
        #decide how many coins are there in the array
        test_round = int(input("How many number do you want to enter to the array? "))
        array = []
        #enter the coins one by one and append them to the array
        for i in range(0, test_round):
            array_enter = int(input("Please Enter: "))
            array.append(array_enter)
        #define variables
        length = len(array)
        summ = int(input("N = "))
        #call function
        print(count(array, length, summ))
    #exceptions
    except ValueError:
        print("Entered invalid input, please try again!")
        pass
