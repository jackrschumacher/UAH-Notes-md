- # Bash fundamentals
	- Bash is a shell- prints the prompt and interprets
		- ![image_1761346122054_0.png](../assets/image_1761346122054_0_1762457946230_0.png){:height 288, :width 364}
	- Bash is the root of scripting
	- Shell scripts are common on Unix and Linux systems
	- Shells scripts evolved from a workflow
		- Sequence of commands placed in a file
		  logseq.order-list-type:: number
		- Command line options enable different options to be passed to commands
		  logseq.order-list-type:: number
		- Introduce variables, if tests, loops enables more complex programming flow
		  logseq.order-list-type:: number
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
  id:: 68fc172a-5e29-4a62-a15b-7fac33851683
	- Allow scripts to make decisions
	  id:: 68fc18b9-c2b1-4bf1-8523-a3d48d8b158d
	- Execute different commands based on conditions
	  id:: 68fc18c3-5205-461d-9187-edcfaeeae5cb
	- Control flow
	  id:: 68fc18cd-f39f-4f17-9602-b41342d79ab7
- ## Types of conditional statements
  id:: 68fc18d0-f1db-459a-b60e-35f91b8d3374
	- if
	  id:: 68fc18fc-1d9c-47f9-986a-08611a1e069b
	- if else
	  id:: 68fc18fe-ff7f-4310-9f02-27c3c5e526c7
	- elif (else if)
	  id:: 68fc1900-d3cd-48e3-9648-e575c98d6c5e
- ### If statement
  id:: 68fc1904-b26f-4c36-9f19-380f1d540b32
-
  id:: 68fc190d-b29a-45ec-956e-2926a058aca5
  ```bash
  if [ condition ]; then
  	commands
  fi
  ```
- ### If-else statement
  id:: 68fc1928-23e0-4169-b58f-f432b6e100ad
-
  id:: 68fc1931-cb34-46a2-9262-6ceffe1b65e4
  ```bash
  if [ condition ]; then
  	commands
  else
  	commands2
  fi
  ```
- ### elif statement
  id:: 68fc1997-210c-40b0-b814-6a8e87c5dd10
-
  id:: 68fc19a5-079e-47ec-bd7e-08df3c025f12
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
  id:: 68fc19dc-16f0-43f2-bffb-166c9ae2e552
-
	- • -eq (equal)
	  id:: 68fc19f6-ad75-45de-af33-565316eca321
	  • -ne (not equal)  
	  • -lt (less than)  
	  • -le (less than or equal)  
	  • -gt (greater than)  
	  • -ge (greater than or equal)  
	- • = (equal)
	  id:: 68fc1a26-2225-492d-b223-e8caabf76d0e
	  • != (not equal)  
	  • -z (empty string)  
	  • -n (non-empty string)  
-
  id:: 68fc1ac6-ab00-4288-80f6-c30a4a5f6056
  ```bash
  num=10
  if [ $num -gt 5 ]; then
  	echo "The number is greater than 5"
  fi
  ```
- ## Logical operators
  id:: 68fc1a53-6bb9-4e77-91d5-f96d4dfb5efa
	- && (AND)
	  id:: 68fc1a5c-b8b8-44ff-9153-73025b51e04c
	- || (OR)
	  id:: 68fc1a64-72f1-45ba-a881-132d2991d230
	- ! (NOT)
	  id:: 68fc1a67-d1c7-42a9-803e-06bc6f25e100
- ## File Test operators
  id:: 68fc1a73-4845-466e-a270-c11a61d65592
	- • -f (is a file)
	  id:: 68fc1a7c-aa5b-444f-8f28-eab438a2e6e0
	  • -d (is a directory)  
	  • -e (exists)  
	  • -r (is readable)  
	  • -w (is writable)  
	  • -x (is executable)  
-
  id:: 68fc1a88-43d4-4845-a386-5ba8f60f7d4c
  ```bash
  # Example of checking a file
  if [ -f "file.txt" ]; then
  	echo "The file exists"
  else
  	echo "The file does not exist"
  fi
  ```
-
  id:: 68fc1c75-aa4e-4179-ba4d-3c2e6c14c135
