'''
Logic for parsing JSON files
'''

import jsonParser

def Main():
    JP = jsonParser.JSON_Parser()
    JE = jsonParser.JsonException()
    JP.jsonPrint()


if __name__ == '__main__':
    Main()