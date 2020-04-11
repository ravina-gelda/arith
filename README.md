

### Programming Assignment 1 - The ARITH language: A Simple Langauge of
### Arithmetic Expressions ###
 ## Problem statement ##
In Haskell, or the language of your choice, write an interpreter for the ARITH language. Your program should consist of:

* A data structure for the abstract syntax tree (AST) of ARITH.
* A parser for ARITH.  You may use external libraries when writing the parser. Remember to cite any code that you take from elsewhere.
* Do NOT use regular expressions to parse the string. The ARITH language is simple enough that this would work, but you will still have to worry about precedence. It may be helpful to parse the String into an AST and think about how the AST should be interpreted. You will be asked to write more complicated parsers later in the quarter. Please take the time to learn how to use a real parsing library.
In HW1, you may assume that there will be exactly one space between numbers and operands, as in the provided test cases. (This assumption will not be true in future homework.)
An interpreter for this AST.  The interpreter should be in the form of a function called eval, which takes in an AST and returns the result.
Test cases which show that your AST, parser, and interpreter work.  These test cases should show good code coverage (i.e. test all cases).
Finally, add a feature to your language, like subtraction or exponentiation.  This addition will involve modifying the AST, parser, and interpreter to support this new feature. You should also write new tests for this feature.

## My implemenattion

I have implemnted ARITH interpretor in Python3. I have Added substraction feature to ARITH. In order to implement the interpretor, I have used precedence of the operators as " Multiplication > Addition > Substraction". Also, with the assumtions taht the input string will have operators separted by **whiletspace**, the parsing of the string becomes easy. Though it should not be difficult to change the code, if we don't want to assume this and parse the input string correctly. While creating AST I followed the below rules:
- if current token is an number
        * if the currect node is not + / - / * then put the number in the node
        * else if current node is * then put the new node with the number to the right of the current node and the current node is changed to the parent of the * node
        * else if current is + / - then put the new node with the integer on the right of the current node
- If current token is + / -
         * create a newnode with this token , and attach the current node to the left of this new node. And change the current node to this new node
- If current token is *
          * create a new node with this token:
          then new_node.left=curr_node.right
                    curr_node.right=new_node
                    curr_node=new_node
 - Then to evalute the AST , I used postorder traversal.
### Prerequisites


Need Python3 installed
* There were some erros taht I faced using make file:
   - pip needs to be installed
   - Setting permission by **'chmod 777'** for all the files :
       - bin/bats
       - libexec/bats-core/bats
       - libexec/bats-core/bats-exec-suite
       - libexec/bats-core/bats-exec-test
       - libexec/bats-core/bats-format-tap-stream
       - libexec/bats-core/bats-preprocess
    

### Testing
* After you met are done with the **prerequisites**
* Test the code in terminal with **test.sh**, make sure that you are in the same directory as **test.sh**


## Acknowledgments

* https://www.youtube.com/watch?v=TastAWp8eIE

