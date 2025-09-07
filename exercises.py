# Exercise 1: Create a function that checks if a word is a palindrome
def is_palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.lower().replace(" ", "")
    return word == word[::-1]

# Exercise 2: Create a function that finds the sum of all even numbers in a list
def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# Exercise 3: Create a function that converts a string to title case
def custom_title_case(text):
    return " ".join(word.capitalize() for word in text.split())

# Exercise 4: Create a function that finds the most frequent element in a list
def most_frequent(lst):
    return max(set(lst), key=lst.count)

# Exercise 5: Create a function that generates a Fibonacci sequence up to n terms
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Test the functions
if __name__ == "__main__":
    # Test palindrome function
    print("Palindrome Tests:")
    print(is_palindrome("radar"))  # True
    print(is_palindrome("hello"))  # False
    print(is_palindrome("A man a plan a canal Panama"))  # True
    
    # Test sum of even numbers
    print("\nSum of Even Numbers Test:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sum_even_numbers(numbers))  # 30
    
    # Test title case
    print("\nTitle Case Test:")
    print(custom_title_case("hello world python programming"))  # Hello World Python Programming
    
    # Test most frequent element
    print("\nMost Frequent Element Test:")
    test_list = [1, 2, 3, 2, 4, 2, 5, 3]
    print(most_frequent(test_list))  # 2
    
    # Test Fibonacci
    print("\nFibonacci Sequence Test:")
    print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
