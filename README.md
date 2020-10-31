#DEVELOPER
	Gaurav Batra

# Undo Logging and Recovery

## Introduction
This assignment has been done as a part of Database Systems Course in Monsoon 2019.
It contains 2 parts:
- **Undo Logging**:
	- Given a set of transactions, print out the Undo Logs into a file.
	- The transactions take place in a round-robin fashion, so a parameter **x** is also provided.
	- Basically given **n** transactions, carry out first **x** instructions for the first transaction, then the first **x** for the next transaction and so on...
- **Undo Recovery**:
	- Given an input file containing UNDO logs till a crash point, and the current set of database element values, perform a recovery - output the set of database elements and their recovered values.

## :file_folder: File Structure
```bash
.
├── 20171114.sh
├── 20171114_1.py
├── 20171114_2.py
├── ProblemStatement.pdf
├── README.md
├── Sample Test Cases
└── input.txt

1 directory, 6 files
```
- **Sample Test Cases** - Contains sample test input.

## :running: Running the program

* To run Undo Logging:
```bash
./20171114.sh [input_file] [x]
```

* To run Undo Recovery:
```bash
./20171114.sh [input_file]
```

[![asciicast](https://asciinema.org/a/CPXSMD0OhpSosbn6ZypPKGjXl.svg)](https://asciinema.org/a/CPXSMD0OhpSosbn6ZypPKGjXl)

## :open_file_folder: Input File Format

* **Undo Logging**:
	- The first line of the file will be a list of database element names and their initial values, space separated, on a single line.
	- Each transaction will begin on a new line, with the transaction name and number of actions in the first line, followed by actions of form READ(), WRITE(), OUTPUT(), or an operation in successive lines. Successive transactions are separated by a newline character.
	- The set of operations you’ll have to handle are {+, −, ∗, /} and the second operand is always an integer.
* **Undo Recovery**:
	- The first line of the file will be a list of database element names and their current disk values, space separated, on a single line.
	- This is followed by a number of log statements which are either STARTs, update logs, COMMITs, Nonquiescent START CKPTs or END CKPTs in successive lines.
	- The last log entry in the file is the entry just before the crash happened.
___________________________________________

Feel free to Contribute :heart:




