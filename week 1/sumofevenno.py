def sum_of_numbers(n):
    # Initialize variables
    even_sum = 0
    odd_sum = 0
    even_numbers = []
    odd_numbers = []

    # Using a while loop to check each number from 1 to n
    i = 1
    while i <= n:
        if i % 2 == 0:  # Even number check
            even_sum += i
            even_numbers.append(i)
        else:  # Odd number check
            odd_sum += i
            odd_numbers.append(i)  # Add odd numbers to the list
        i += 1

    # Print all even numbers and their sum
    print("Even numbers:", even_numbers)
    print("Sum of even numbers:", even_sum)

    # Print all odd numbers and their sum
    print("Odd numbers:", odd_numbers)
    print("Sum of odd numbers:", odd_sum)

if __name__ == "__main__":
    # Get input from the user
    try:
        n = int(input("Please enter a positive integer n: "))
        if n <= 0:
            print("Please enter a number greater than zero.")
        else:
            sum_of_numbers(n)
    except ValueError:
        print("Invalid input. Please enter an integer.")
