# Find the least amount of coins needed
def convert_sents_to_coins(sents, avaliable_coins):
    # Empty coin array
    coin_values = []

    # Loop over coin values
    for coin in avaliable_coins:

        # If there are no sents add a zero to an array
        if sents == 0:
            coin_values.append(0)
            continue
        
        # Divide to floor value
        current_coin_count = sents // coin

        # Set new value for the sents based on floor count of the coin
        sents = sents - (current_coin_count * coin)

        # Add the count to array
        coin_values.append(current_coin_count)

    # Start output
    print('You need these coins for the amount of sents you have:')

    # Print coin values
    for index in range(len(coin_values)):
        
        # Don't print empty coin values
        if coin_values[index] != 0:
            # Print coin if coin value is not zero
            print(str(avaliable_coins[index]) + ' sent coins: ' + str(coin_values[index]))

    return True

    



# Define main fucntion
def main():
    # Current available coins
    current_coins = [50, 20, 10, 5, 1]

    print('Current coins: ' + str(current_coins))

    # Get user input for prime
    sents = int(input('Convert sents to coins: '))

    # If sent count is zero don't convert
    if sents == 0:
        print('Zero sents can not be divided into to coins')
        # Exit with one if 0 is given as an input
        exit(1)
    else:
        # Get coins from sents
        convert_sents_to_coins(sents, current_coins)

    # Exit main with zero if everythin went okey.
    exit(0)

# Init main
if __name__ == "__main__":
    main()