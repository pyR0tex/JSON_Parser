'''
Logic for parsing JSON files
'''

from jsonParser import JSON_Parser, JSON_Exception
import argparse

def Main(args):
    print("--> main")
    
    flag = CheckJson(args)
    if flag:
        print(f"        JSON -> VALID")
    else:
        print(f"        JSON -> INVALID")

    return


def ReadJSON(fileName):
    '''
    Reads the JSON File
    '''
    file = fileName
    try:
        with open(file) as f:
            fileContent = f.read()
            print(f"{fileContent}")

    except FileNotFoundError as e:
        import sys
        print(f"        Program Failed while reading file: {file}")
        print(f"    [ERROR] -> {e}", file=sys.stderr) 
        sys.exit(1)
    
    return

def CheckJson(args) -> bool:
    '''
    Checks if user provided an arg file
    '''
    if args.JSON_File:
        print(f"        File Provided: {args.JSON_File}")
        ReadJSON(str(args.JSON_File))
        flag = True
    else:
        print(f"        No input JSON file provided")
        flag = False

    return flag


def SetupArgs():

    '''
    Initialize arparse to accept an input file
    '''
    argParser = argparse.ArgumentParser(
        prog="isJson",
        description="Tells the user if the input JSON file is formatted correctly"
    )
    argParser.add_argument(
        'JSON_File',
        nargs='?',
        help='Provide a JSON file to validate'
    )

    args = argParser.parse_args()
    return args


'''
TESTS / MAIN RUN
'''
if __name__ == '__main__':
    args = SetupArgs()
    Main(args)