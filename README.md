# Competitive-Programming-Solution-Validator
This is a simple python script that genarates random testcases to stress test your solution

### Overview of how it works
This program is simply taking "gen.cpp" and compile it and then run it. Then, it takes generated testcase and push it into "./test.exe". After that, it compiles the other two (correct.cpp, wrong.cpp) and runs their exe files. Then it passes testcase which we got from "gen.cpp" and pass to both files and pass their outputs into ["correct.txt", "wrong.txt"] and compare the output results. If they are the same then PASSED, otherwise it's FAILED and the program terminates. Obviously, when the program terminates it will leave all text files with their last contents which is testcase that broke your code.
- "wrong.txt" will have the output of your code which has the problem.
- "correct.txt" will have the correct output/
- "test.txt" will have the test that broke your code.

### Requirements:
- your-solution.cpp file
- brute-force/correct-solution.cpp file
- generator.cpp file to generate test cases
- g++ compiler installed on your machine


### How To Use:
1. First, you open "tester.exe" file

2. You should have 4 prompts like these:

    <b>prompts</b>

    
    - <b>Correct cpp file path [./correct.cpp]:</b><br>
    You can type the brute-force/correct cpp file path here or click ENTER and default path is <b>"./correct.cpp"</b>.

    - <b>Wrong cpp file path [./wrong.cpp]:</b><br>
    You can type the cpp file path that you need to test here or click ENTER and default path is <b>"./wrong.cpp"</b>.

    - <b>Generator cpp file path [./gen.cpp]:</b>
    You can type generator.cpp file path here or click ENTER and default path is <b>"./gen.cpp"</b>.

    - <b># of tests: </b><br>
    <p>You need to type the number of random test cases to test your code.<br>
    <span style='color:yellow; font-weight: bold;'>Warning:</span> no default values for this one.</p>

3. After passing the files, you need to wait for couple of seconds and your result for all test cases will appear like this if all passed:<br>
    
    <b>passed</b>

    When a testcase breaks your code, stress-tester will terminate and show like this:
    
    <b>failed</b>

    leaving 3 text files:
    - This test case that broke your solution in <b>"./test.txt"</b>
    - Brute-force/correct output in <b>"./correct.txt"</b>
    - Your code output in <b>"./wrong.txt"</b>
    
    <br>

    Finally, the programe will ask you if you want to make another test or not:
    - Y -> for yes
    - N or ENTER -> terminates the program 
    

### Future Updates:
If you have any better idea or any recommendation, feel free to contact me right away and I would be happy to have it.
I will also add any new features or enhancements that come in mind ISA.