# This script generates random test cases and compares the output of your
# C++ solution with a brute force/correct solution.

# Import the necessary modules
import random
import os
from colorama import Fore, Style


# Define the function to generate a random test case
def generate_test_case():
    test = open("test.txt", "w")
    n = random.randint(1, 20)
    test.write(str(n) + '\n')

    for i in range(n):
        test.write(str(random.randint(1, 500)) + ' ')

    q = random.randint(1, 5)
    test.write('\n' + str(q) + '\n')
    for i in range(q):
        x = random.randint(0, n-1)
        y = random.randint(x, n-1)
        test.write(str(x) + ' ' + str(y) + '\n')

    test.close()


# Define the function to compare the output of the two solutions
def compare():
    """Compares the output of the two solutions."""
    file = open("test.txt", "r")
    test = file.read().strip()
    file.close()

    # correct output
    os.system(f"correct.exe < test.txt > correct.txt")

    # wrong output
    os.system(f"wrong.exe < test.txt > wrong.txt")
    
    correct = open("correct.txt", "r")
    wrong = open("wrong.txt", "r")

    ans = (correct.read().strip() == wrong.read().strip())
    correct.close()
    wrong.close()

    return ans



# Define the main function
def main():
    """The main function."""
    # Get the name of the brute force/correct solution file
    correct_file = input("Correct cpp [default -> correct.cpp]: ").strip()
    if (correct_file == ""): correct_file = "correct.cpp"

    # Get the name of the C++ solution file
    wrong_file = input("Wrong cpp [defult -> wrong.cpp]: ").strip()
    if (wrong_file == ""): wrong_file = "wrong.cpp"

    # Get number of test cases
    tests = int(input("# of tests: "))
    print('-'*20) # separator

    os.system(f"g++ {wrong_file} -o wrong.exe")
    os.system(f"g++ {correct_file} -o correct.exe")
    
    # Generate random test cases
    for i in range(1, tests+1):
        print(f"Test {i}:", end=' ')

        # Generate the test case and push it to the file
        generate_test_case()

        # Compare the output of the two solutions on the current test case
        res = compare()
        if (res):
            print(Fore.GREEN + "Passed" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Failed :(" + Style.RESET_ALL)
            return

# Call the main function
if __name__ == "__main__":
    main()
