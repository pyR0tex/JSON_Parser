'''
Logic for parsing JSON files
'''

from jsonParser import JSON_Parser, JSON_Exception
import argparse

def Main(args):
    print(f"        --> JSON PARSER <--", end="\n\n")
    
    flag = CheckJson(args)
    if flag:
        print(f"    result: JSON -> VALID")
    else:
        print(f"    result: JSON -> INVALID")

    return

'''
Reads the JSON File
'''
def ReadJSON(fileName):
    file = fileName
    jsonParser = JSON_Parser()
    try:
        with open(file) as f:
            fileContent = f.read()
            print(f"{fileContent}")
            print(f"{jsonParser.jsonParse(fileContent)}")

    except FileNotFoundError as FNF:
        import sys
        print(f"        Program Failed while reading file: {file}")
        print(f"    [ERROR] -> {FNF}", file=sys.stderr) 
        sys.exit(1)
    except JSON_Exception as e:
        import sys
        print(f"        Program Failed while reading file: {file}")
        print(f"    [ERROR] -> {e}", file=sys.stderr) 
        sys.exit(1)
    
    return 

'''
Checks if user provided an arg file
'''
def CheckJson(args) -> bool:
    if args.test:
        RunTests()
        flag = False
    else:
        if args.JSON_File:
            print(f"        File Provided: {args.JSON_File}")
            ReadJSON(str(args.JSON_File))
            flag = True
        else:
            print(f"        No input JSON file provided")
            print(f"        --> standard input IN PORGRESS\n")
            flag = False

    return flag


'''
Initialize arparse to accept an input file
'''
def SetupArgs():
    argParser = argparse.ArgumentParser(
        prog="isJson",
        description="-- Tells the user if the input JSON file is formatted correctly"
    )
    argParser.add_argument(
        'JSON_File',
        nargs='?',
        help='-- Provide a JSON file to validate'
    )
    argParser.add_argument(
        '--test',
        '-t',
        nargs='?',
        help='-- Run the pre-written tests'
    )

    args = argParser.parse_args()
    return args

def RunTests():
    print(f"        --- Running Test Scripts ---")
    print(f"        --> IN PROGRESS \n")

'''
TESTS / MAIN RUN
'''
if __name__ == '__main__':
    args = SetupArgs()
    Main(args)

    pass