# This script generates random test cases and compares the output of your
# C++ solution with a brute force/correct solution.

# Import the necessary modules
import os

# Compares and finds the line of differ
def find_differ(s1, s2):
    l1 = s1.split('\n')
    l2 = s2.split('\n')

    size1, size2 = len(l1), len(l2)

    for i in range(max(size1, size2)):
        if (i == size1 or i == size2): return i+1
        if (l1[i].strip() != l2[i].strip()):
            return i+1
        
    return None

# Define the function to compare the output of the two solutions
def compare():
    """Compares the output of the two solutions."""

    # correct output
    os.system(f"correct.exe < test.txt > correct.txt")

    # wrong output
    os.system(f"wrong.exe < test.txt > wrong.txt")
    
    correct = open("correct.txt", "r")
    wrong = open("wrong.txt", "r")

    ans = find_differ(correct.read(), wrong.read())

    correct.close()
    wrong.close()

    if ans != None:
        return [False, ans]
    return [True, None]



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
    print('-'*30) # separator

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
        if (res[0]):
            print("PASSED")
        else:
            print(f"FAILED :( \n-> Output differs in line {res[1]}")
            return
        

# Call the main function
if __name__ == "__main__":
    main()
    response = input("\nAnother test [Y, N]: ").strip()
    while response.lower() == 'y':
        main()
        response = input("\nAnother test [Y, N]: ").strip()
