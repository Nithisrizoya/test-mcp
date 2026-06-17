def check_even_odd(number):
    """Check if a number is even or odd"""
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Main program
if __name__ == "__main__":
    print("Even or Odd Predictor")
    print("-" * 40)
    
    try:
        num = int(input("Enter a number: "))
        result = check_even_odd(num)
        print(result)
    except ValueError:
        print("Please enter a valid integer!")
