# Competitive-Programming-Solution-Validator
This is a simple python script that genarates random testcases to stress-test your solution and figure out side case that would break your code.

### Overview of how it works
This program is simply taking "gen.cpp" and compile it and then run it. Then, it takes generated testcase and push it into "./test.exe". After that, it compiles the other two (correct.cpp, wrong.cpp) and runs their exe files. Then it passes testcase which we got from "gen.cpp" and pass to both files and pass their outputs into ["correct.txt", "wrong.txt"] and compare the output results. If they are the same then PASSED, otherwise it's FAILED and the program terminates. Obviously, when the program terminates it will leave all text files with their last contents which is testcase that broke your code.
- <b>"wrong.txt"</b> will contain the output of your code which has the problem.
- <b>"correct.txt"</b> will contain the correct output/
- <b>"test.txt"</b> will contain the test that broke your code.

### Requirements:
- your-solution.cpp file
- brute-force/correct-solution.cpp file
- generator.cpp file to generate test cases
- g++ compiler installed on your machine


### How To Use:
1. First, you open "tester.exe" file

2. You should have 4 prompts like these:

    ![prompts](https://github.com/SayedReda1/Competitive-Programming-Solution-Validator/assets/71211593/1d2842b6-8fd6-4a5e-8bdb-03df8d2117e1)
    
    - <b>Correct cpp file path [./correct.cpp]:</b><br>
    You can type the brute-force/correct cpp file path here or click ENTER and default path is <b>"./correct.cpp"</b>.

    - <b>Wrong cpp file path [./wrong.cpp]:</b><br>
    You can type the cpp file path that you need to test here or click ENTER and default path is <b>"./wrong.cpp"</b>.

    - <b>Generator cpp file path [./gen.cpp]:</b>
    You can type generator.cpp file path here or click ENTER and default path is <b>"./gen.cpp"</b>.

    - <b># of tests: </b><br>
   You need to type the number of random test cases to test your code.<br>
   <b>Warning:</b> no default values for this one.

3. After passing the files, you need to wait for couple of seconds and your result for all test cases will appear like this if all passed:<br>
    
    ![passed](https://github.com/SayedReda1/Competitive-Programming-Solution-Validator/assets/71211593/94def73e-f33d-4030-8b7e-5b961b6af50a)


    When a testcase breaks your code, stress-tester will immediately terminate and show like this:

   
    ![failed](https://github.com/SayedReda1/Competitive-Programming-Solution-Validator/assets/71211593/0eee1fc8-189b-43aa-bb1d-077811953305)

    

    leaving 3 text files:
    - The line number of ouput difference
    - This test case that broke your solution in <b>"./test.txt"</b>
    - Brute-force/correct output in <b>"./correct.txt"</b>
    - Your code output in <b>"./wrong.txt"</b>
    
    <br>

    Finally, the programe will ask you if you want to make another test or not:
    - Y -> for yes
    - N or ENTER -> terminates the program 
    

### Issues:
- This idea works only with one-expected-output computational problems not the ones that may have different correct outputs because it only validates solutions through comparing outputs.
- It obviously doesn't work with interactive problems (which may be included in future updates)

I would be happy to receive any improvement ideas. If you have one, feel free to contact me right away ^_^.
