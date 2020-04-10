

### Programming Assignment 1 - The ARITH language:

In Haskell, or the language of your choice, write an interpreter for the ARITH language. Your program should consist of:

* A data structure for the abstract syntax tree (AST) of ARITH.
* A parser for ARITH.  You may use external libraries when writing the parser. Remember to cite any code that you take from elsewhere.
* Do NOT use regular expressions to parse the string. The ARITH language is simple enough that this would work, but you will still have to worry about precedence. It may be helpful to parse the String into an AST and think about how the AST should be interpreted. You will be asked to write more complicated parsers later in the quarter. Please take the time to learn how to use a real parsing library.
In HW1, you may assume that there will be exactly one space between numbers and operands, as in the provided test cases. (This assumption will not be true in future homework.)
An interpreter for this AST.  The interpreter should be in the form of a function called eval, which takes in an AST and returns the result.
Test cases which show that your AST, parser, and interpreter work.  These test cases should show good code coverage (i.e. test all cases).
Finally, add a feature to your language, like subtraction or exponentiation.  This addition will involve modifying the AST, parser, and interpreter to support this new feature. You should also write new tests for this feature.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

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
    

```
Give examples
```

### Testing
* After you met are done with the **prerequisites**
* Test the code in terminal with **test.sh**, make sure that you are in the same directory as **test.sh**

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* https://www.youtube.com/watch?v=TastAWp8eIE

