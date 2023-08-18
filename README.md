# Competitive-Programming-Solution-Validator
This is a simple python script that genarates random testcases to stress test your solution

### Needed scripts and edits
- your-solution.cpp file
- brute-force/correct-solution.cpp file
- editing the generator function in tester.py

### Supported OS
Hopefully, It's cross-platform and works on:
- Windows
- Linux
- Mac


### How To Use
1. First, you need to run "tester.py" from terminal, Type:
    ```
    python ./tester.py
    ```
    -> if that doesn't work try "python3" instead

2. You should see three prompts like this

    <b>how to use image</b>
    
    <b>Correct cpp [default -> correct.cpp]:</b><br>
    You can type the brute-force/correct cpp file path here or click ENTER and default path is <b>"./correct.cpp"</b>.

    <b>Wrong cpp [default -> wrong.cpp]:</b><br>
    You can type the cpp file path that you wanna test here or click ENTER and default path is <b>"./wrong.cpp"</b>.

    <b># of tests: </b><br>
    You need to type the number of random test cases to test your code.<br>
    <span><b style="color: yellow">Warning:</b></span> no default values for this one.

3. After passing the files you need to wait for couple of seconds and your result for all test cases will appear like this if all passed<br>
    
    <b>passed image</b>

    and when a testcase breaks your solution stress-test will terminate and show like this
    
    <b>failed image</b>
    
    leaving: 
    - This test case in <b>"./test.txt"</b>
    - Brute-force/correct output in <b>"./correct.txt"</b>
    - Your code output in <b>"./wrong.txt"</b> 


### Future updates
I actually made this script for new cp students who use C++ to help them debug their code but I think that most of them does have to know python
So, I change the generator function concept to be a gen.cpp file that its path is taken as an input.