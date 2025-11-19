---
title: Week 9- Linux intro and IO
---

- # Bash fundamentals
	- Bash is a shell- prints the prompt and interprets
		- ![image_1761346122054_0.png](../assets/image_1761346122054_0_1762457946230_0.png){:height 288, :width 364}
	- Bash is the root of scripting
	- Shell scripts are common on Unix and Linux systems
	- Shells scripts evolved from a workflow
		- Sequence of commands placed in a file

		- Command line options enable different options to be passed to commands

		- Introduce variables, if tests, loops enables more complex programming flow

	- Can also be an intermediary between other languages
- # Bash Terminal and Commands
- ## Using the shell
	- ![image_1761346948850_0.png](../assets/image_1761346948850_0_1762457936237_0.png){:height 183, :width 348}
	- ~ is a shorthand for home directory in this case
- ### Example commands
	-
	  ```bash
	  [username@scc1 ~]$ command --option argument
	  ```
	- Command- does one thing
	- Options- change the way command does the thing
	- Argument-provides input/output that the command interacts with
	- Can use man or info to get info
	- History command to see shell history
	- ![image_1761347500811_0.png](../assets/image_1761347500811_0_1762457960459_0.png)
- ### Variables
	-
	  ```bash
	  USER=test
	  echo $test
	  export $test
	  ```
	- Too see environment variables use the printenv command
- # Input Output in Bash
	- I/O is important to interact with users, data processing, automation and scripting tasks, interaction with other programs, error handling
	- Bash input-received data from user
	- Bash output-refers to info or data that the program generates or writes
	- ![image_1761349308902_0.png](../assets/image_1761349308902_0_1762457976102_0.png)
- ## File Descriptors
	- Standard input - stdin
		- Interactively read input from user from another command using standard input
	- Standard output - stdout
		- Allows you to display output using standard output
	- Standard error- stderr
		- Handles error messages
- ## File Redirection
	- ![image_1761349419418_0.png](../assets/image_1761349419418_0_1762458063075_0.png){:height 409, :width 689}
	- Basic I/O manipulation
	-
	  ```bash
	  echo "This is example code" > story
	  cat story
	  cat < story
	  ```
- ## Pipelines
	- Redirect output of command into standard input
	-
	  ```bash
	  ls -l | more
	  ```
- # Bash Conditionals

	- Allow scripts to make decisions

	- Execute different commands based on conditions

	- Control flow

- ## Types of conditional statements

	- if

	- if else

	- elif (else if)

- ### If statement

  ```bash
  if [ condition ]; then
  	commands
  fi
  ```
- ### If-else statement

  ```bash
  if [ condition ]; then
  	commands
  else
  	commands2
  fi
  ```
- ### elif statement

  ```bash
  if [ condition1 ]; then
  	commands1
  elif [ condition2 ]; then
  	commands2
  else
  	commands3
  fi
  ```
- ## Comparison operators

-
	- • -eq (equal)

	  • -ne (not equal)  
	  • -lt (less than)  
	  • -le (less than or equal)  
	  • -gt (greater than)  
	  • -ge (greater than or equal)  
	- • = (equal)

	  • != (not equal)  
	  • -z (empty string)  
	  • -n (non-empty string)  

  ```bash
  num=10
  if [ $num -gt 5 ]; then
  	echo "The number is greater than 5"
  fi
  ```
- ## Logical operators

	- && (AND)

	- || (OR)

	- ! (NOT)

- ## File Test operators

	- • -f (is a file)

	  • -d (is a directory)  
	  • -e (exists)  
	  • -r (is readable)  
	  • -w (is writable)  
	  • -x (is executable)  

  ```bash
  # Example of checking a file
  if [ -f "file.txt" ]; then
  	echo "The file exists"
  else
  	echo "The file does not exist"
  fi
  ```


<style>
  h1 { font-size: 1.5em; }
  h2 { font-size: 1.3em; }
  h3 { font-size: 1.1em; }
  
  /* SMART FIX: Makes list items (bullets) respect your Logseq line breaks */
  li { white-space: pre-wrap; }
  
  /* Keep headings inside lists normal size */
  li h1, li h2, li h3, li h4 { 
      font-size: 1em !important; 
      margin: 0 !important; 
      display: inline;
  }
</style>
