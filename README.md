# JSON_Parser

### A JSON Parser Command Line Tool - built in Python
#### - Given an input .json file, the program will output if the file content is a syntactically valid JSON object; else it will raise an exception


## Prerequisites:
  - clone the repo to your machine
  - create a virtual environment (venv)
  - install the argparse module: 'pip install argparse'
    
## To Run:
  - run the program in the command line: 'python isJson.py [.json file]'
  - the program also takes optional argruments:
      'python isJson [-h], [--help] for [HELP]'
      'python isJson [-test] for [TEST]'
  - if no flags nor input file are given:
      'python isJson.py' -- provide the input file name through standard input

## Testing:
  - Type: 'python isJson -test' and follow the instructions
  ![test screenshot] (Testing_Screenshot.png)


