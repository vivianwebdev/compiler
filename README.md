# Snake Language Compiler

This project is a compiler for **Snake**, a custom programming language designed for learning purposes. The compiler performs lexical, syntax, and semantic analysis with a graphical interface to facilitate the execution and debugging of programs written in Snake.

## Features
- **Lexical Analysis:** Tokenizes the input code and detects lexical errors.
- **Syntax Analysis:** Validates the structure of Snake programs based on predefined rules.
- **Semantic Analysis:** Ensures logical correctness, such as type consistency and variable declarations.
- **Custom Language:** Implements unique syntax and features of the Snake language.
- **User-Friendly GUI:** Provides an interface for inputting code, running analysis, and viewing results.

## Snake Language Syntax
### Basic Rules
1. **Program Structure:**
   - The program must start with `Snk_Begin $` and end with `Snk_End $`.

2. **Variable Declarations:**
   - **Integer:** `Snk_Int <var1>, <var2>, ... $`
   - **Real (float):** `Snk_Reel <var1>, <var2>, ... $`
   - **String:** `Snk_String "<value>" $`

3. **Assignments:**
   - Use `Set <variable> <value> $` to assign values to variables.

4. **Printing:**
   - Use `Snk_Print <message>` or `Snk_Print <variable>` to display text or variable values.

5. **Comments:**
   - Add inline comments using `$$`.

6. **Conditionals:**
   - Use `If [condition] $` and `End $` to define conditional blocks.

7. **Variable Copying:**
   - Use `Get <variable1> From <variable2> $` to assign the value of one variable to another.

8. **Blocks:**
   - Use `Begin $` and `End $` for nested operations or grouping commands.

## Example Program

Snk_Begin $

Snk_Int a, b $                  $$ Declare two integers
Snk_Reel pi $                   $$ Declare a real number
Set a 5 $
Set b 10 $
Set pi 3.14159 $

Snk_Print "The value of a is:" $
Snk_Print a $

If [a < b] $
    Snk_Print "a is less than b" $
End $

Snk_End $
------------------------------------------------------------------------------------------------------
How to Use :

1- Clone the Repository:
      git clone https://github.com/vivianwebdev/compiler.git
      
2- Navigate to the Directory:
cd compiler

3- Run the Compiler GUI:
  python ui.py
  
4- Write or Upload Snake Code:
Input your Snake code in the text area or upload a .snk file.

5- Analyze the Code:
Use the buttons to perform Lexical, Syntax, and Semantic analysis.
View Results:

6- Check the output section for errors or analysis results.

 File Structure
ui.py: Contains the graphical interface.
syntaxique.py: Performs syntax analysis.
sem.py: Handles semantic analysis.
Example File: example.snk demonstrates Snake language syntax.

Contributing
Contributions are welcome! Fork the project, make changes, and submit a pull request.muaaah
