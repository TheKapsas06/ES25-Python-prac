# Get if numbers modal is zero
def is_modal_zero(number, devider):
    # Get number modal
    number_modal = number % devider

    # return true if modal equals zero
    if number_modal == 0:
        return True
    
    # Return false if it didn't return on modal equal 0
    return False


# Get if number is a prime number
def is_prime_number(number):
    
    # Set an array empty array for all the numbers which equal with 0 modal
    modal_zero_numbers = []

    # loop all numbers till our number
    for currentNumber in range(1, number):
        
        # Get if modal is zero
        modal_statement = is_modal_zero(number, currentNumber)

        # If modal is zero add to array the current number
        if modal_statement:
            modal_zero_numbers.append(currentNumber)

    # If length is one it is a prime
    if len(modal_zero_numbers) == 1:
        return True
    # If has any else length the number is not a prime
    else:
        print('Found ' + str(len(modal_zero_numbers) - 1) + ' other number to devide the number with.')
        print('Besides 0 and the number itself (' + str(number) + ')')
        return False
    
# Define main fucntion
def main():
    # Get user input for prime
    number = int(input('Input number to check: '))
    is_prime = is_prime_number(number)

    if is_prime:
        print('Number is a prime number!')
    else:
        print('Number is not a prime number')
    
    exit(0)


# Init main
if __name__ == "__main__":
    main()

