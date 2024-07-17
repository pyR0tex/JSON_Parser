'''
Logic for parsing JSON files
'''

from jsonParser import JSON_Parser, JSON_Exception
import argparse
import sys, os

def Main(args):
    print()
    print(f"        --> JSON PARSER <--", end="\n\n")
    
    flag = CheckJson(args)
    if flag:
        print(f"\n        result:   JSON file --> VALID\n")
    else:
        print(f"\n        result:   JSON file --> INVALID\n")
    sys.exit(0)

'''
Reads the JSON File
'''
def ReadJSON(fileName) -> bool:
    file = fileName
    jsonParser = JSON_Parser()

    try:
        with open(file) as f:
            fileContent = f.read()
            print(f"        Parsed Content:\n \
                            --> {jsonParser.jsonParse(fileContent)} <--")
            return True

    except FileNotFoundError as FNF:
        print(f"        Program Failed while reading file: {file}")
        print(f"        [ERROR] -> {FNF}\n", file=sys.stderr)
        return False 
    
    except JSON_Exception as e:
        print(f"        Program Failed while parsing file: {file}")
        print(f"        [ERROR] -> {e}\n") 
        return False
        

'''
Checks if user provided an arg file
'''
def CheckJson(args) -> bool:
    if args.test:
        RunTests()
    else:
        if args.JSON_File:
            print(f"        File Provided: {args.JSON_File}")
            flag = ReadJSON(str(args.JSON_File))
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
        '-t',
        '--test',
        nargs='?',
        help='-- Run the pre-written tests'
    )

    args = argParser.parse_args()
    return args

def RunTests():
    print(f"        --- Running Test Scripts ---\n")
    test_directory = 'tests'
    test_input = input("        Type the test option (left), then press ENTER\n \
                       \n \
            ss -- ALL TESTS \n \
            s1 -- STEP 1 Tests\n \
            s2 -- STEP 2 Tests\n \
            s3 -- STEP 3 Tests\n \
            s4 -- STEP 4 Tests\n\n")
    try:

        ## STEP 1
        if test_input == "s1":
            step = 'step1'
            json_test_files = os.listdir(str(f"{test_directory}/{step}"))
            filtered_json_files = [j for j in json_test_files if j.endswith('.json')]
            i = 0
            for json in filtered_json_files:
                print(f"    Test {i}:  {test_directory}/{step}/{json}\n")
                flag = ReadJSON(str(f"{test_directory}/{step}/{json}"))
                i += 1
                if flag:
                    print(f"\n        result:   JSON file --> VALID\n")
                else:
                    print(f"\n        result:   JSON file --> INVALID\n")
        
        ## STEP 2
        elif test_input == "s2":
            step = 'step2'
            json_test_files = os.listdir(str(f"{test_directory}/{step}"))
            filtered_json_files = [j for j in json_test_files if j.endswith('.json')]
            i = 0
            for json in filtered_json_files:
                print(f"    Test {i}:  {test_directory}/{step}/{json}\n")
                flag = ReadJSON(str(f"{test_directory}/{step}/{json}"))
                i += 1
                if flag:
                    print(f"\n        result:   JSON file --> VALID\n")
                else:
                    print(f"\n        result:   JSON file --> INVALID\n")
        ## STEP 3
        elif test_input == "s3":
            step = 'step3'
            json_test_files = os.listdir(str(f"{test_directory}/{step}"))
            filtered_json_files = [j for j in json_test_files if j.endswith('.json')]
            i = 0
            for json in filtered_json_files:
                print(f"    Test {i}:  {test_directory}/{step}/{json}\n")
                flag = ReadJSON(str(f"{test_directory}/{step}/{json}"))
                i += 1
                if flag:
                    print(f"\n        result:   JSON file --> VALID\n")
                else:
                    print(f"\n        result:   JSON file --> INVALID\n")
        ## STEP 4
        elif test_input == "s4":
            step = 'step4'
            json_test_files = os.listdir(str(f"{test_directory}/{step}"))
            filtered_json_files = [j for j in json_test_files if j.endswith('.json')]
            i = 0
            for json in filtered_json_files:
                print(f"    Test {i}:  {test_directory}/{step}/{json}\n")
                flag = ReadJSON(str(f"{test_directory}/{step}/{json}"))
                i += 1
                if flag:
                    print(f"\n        result:   JSON file --> VALID\n")
                else:
                    print(f"\n        result:   JSON file --> INVALID\n")
        ## ALL TESTS
        elif test_input == "ss":
            tests_list = os.listdir(test_directory)
            filtered_tests_list = [t for t in tests_list if t.startswith('step')]
            filtered_tests_list.reverse()
            i = 0
            for f in filtered_tests_list:
                json_test_files = os.listdir(str(f"{test_directory}/{f}"))
                filtered_json_files = [j for j in json_test_files if j.endswith('.json')]
                for json in filtered_json_files:
                    print(f"    Test: {i}\n")
                    flag = ReadJSON(str(f"{test_directory}/{f}/{json}"))
                    i += 1
                    if flag:
                        print(f"\n        result:   JSON file --> VALID\n")
                    else:
                        print(f"\n        result:   JSON file --> INVALID\n")
        else:
            print(f"        ERROR: Bad Input, running again\n")
            RunTests()

        sys.exit(0)

    except JSON_Exception as json_e:
        print(f"        [ERROR] -> {json_e}\n")
        print(f"\n        result:   JSON file --> INVALID\n")
        sys.exit(1)
        return 
    except Exception as e:
        print(f"        [ERROR] -> {e}\n")
        print(f"\n        result:   JSON file --> INVALID\n")
        sys.exit(1)
        return 
    
    
'''
TESTS / MAIN RUN
'''
if __name__ == '__main__':
    args = SetupArgs()
    Main(args)

    pass