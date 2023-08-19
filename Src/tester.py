# This script generates random test cases and compares the output of your
# C++ solution with a brute force/correct solution.

# Import the necessary modules
import os


# Define the function to compare the output of the two solutions
def compare():
    """Compares the output of the two solutions."""

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
    # Get the path of the brute force/correct solution file
    correct_file = input("Correct cpp file path [./correct.cpp]: ").strip()
    if (correct_file == ""): correct_file = "correct.cpp"

    # Get the path of the C++ solution file
    wrong_file = input("Wrong cpp file path [./wrong.cpp]: ").strip()
    if (wrong_file == ""): wrong_file = "wrong.cpp"

    # Get the path of generator.cpp
    gen_file = input("Generator cpp file path [./gen.cpp]: ").strip()
    if (gen_file == ""): gen_file = "gen.cpp"

    # Get number of test cases
    tests = int(input("# of tests: "))
    print('-'*20) # separator

    os.system(f"g++ {correct_file} -o correct.exe")
    os.system(f"g++ {wrong_file} -o wrong.exe")
    os.system(f"g++ {gen_file} -o gen.exe")
    
    # Generate random test cases
    for i in range(1, tests+1):
        print(f"Test {i}:", end=' ')

        # Generate the test case and push it to the file
        os.system("gen.exe > test.txt")

        # Compare the output of the two solutions on the current test case
        res = compare()
        if (res):
            print("PASSED")
        else:
            print("FAILED :(")
            return

# Call the main function
if __name__ == "__main__":
    main()
    response = input("\nAnother test [Y, N]: ").strip()
    while response.lower() == 'y':
        main()
        response = input("\n\nAnother test [Y, N]: ").strip()
