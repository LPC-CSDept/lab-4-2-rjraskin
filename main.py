def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    sum = 0
    for i in range(5):
        number = int(input('Enter a number '))
        sum += number
    print (sum)

    ########################################
    # Do not delete the return statement
    ########################################
    return sum


if __name__ == '__main__':
    main()
