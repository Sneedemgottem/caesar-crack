# Usage:
The command only has two flags (-c and -m).

**-m** <String> This is a required field because it is the main string input you are giving the program.

**-c** <Integer> This is an optional field. If you do not use it then it will simply output every single alphabet shift sequence of the string given with the -m flag. If you do choose to use this flag, it takes an integer as an input and will only output the original message with an alphabet shift of whatever integer you input. Can be used to create cipher text from an original message.

**-h** This outputs a help message to remind you of the flags.

Example:
```
python caesar.py -m "Hello" -> This will output every alphabet shift sequence.
```
Example 2: 
```
python caesar.py -m czggj -c 5 -> Outputs 'hello' because it shifts the alphabet over by 5
```

Example 3 (with file):
On linux you can use the following command to take text from a file and pipe it to the python script.
```
cat hello.txt | xargs python caesar.py -c5 -m
```
