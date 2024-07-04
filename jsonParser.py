# JSON Parser class

WHITESPACE = [" ", "\n", "\t", "\r"]

class JSON_Exception(Exception):
    pass

class JSON_Parser:

    def __init__(self):
        self.index = 0
        self.jsonStr = ""
        self.depth = 0
    
    def jsonPrint(self):
        print("JSON Parser")
    
    def jsonParse(self, fileContent):
        self.index = 0
        self.jsonStr = fileContent
        self.depth = 0
        
        '''
        Add code to skip whitespace 

        Here
        '''

        if fileContent[self.index] not in ["{", "["]:
            raise JSON_Exception('a valid JSON payload should be an object or array')
        result = self.parseValue()
        return result

    def parseValue(self):
        result = "      parseValue() -> in progress"

        return result