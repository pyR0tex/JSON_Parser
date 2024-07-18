'''
SET TO 0 if you don't want to debug
'''
import os
os.environ['PYTHONBREAKPOINT'] = '0'

# JSON Parser class

WHITESPACE = [" ", "\n", "\t", "\r"]
BOOL_OR_NULL = {'true': True, 'false': False, 'null': None}

class JSON_Exception(Exception):
    pass

class JSON_Parser:

    def __init__(self):
        self.index = 0
        self.jsonStr = ""
        self.depth = 0
    
    '''
        HELPERS --------------------------------------------------------------------------------------------
    '''
    def getIndex(self):
        '''
        Returns the index
        '''
        return self.index
    
    def skip_whitespace(self):
        while self.index < len(self.jsonStr) and self.jsonStr[self.index] in WHITESPACE:
            self.index += 1

    def process_colon(self):
        if self.index < len(self.jsonStr) and self.jsonStr[self.index] == ":":
            self.index += 1
        else:
            raise JSON_Exception(f"     Colon expected")
    
    def process_comma(self):
        if self.index < len(self.jsonStr) and self.jsonStr[self.index] == ",":
            self.index += 1
        else:
            raise JSON_Exception(f"     Comma expected")
    
    '''
       End HELPERS --------------------------------------------------------------------------------------------
    '''

    '''
    Initiates the parsing of the json file

    Input: File Content of input file
    '''
    def jsonParse(self, fileContent):

        self.index = 0
        self.jsonStr = fileContent
        self.depth = 0
        
        if len(self.jsonStr) == 0:
            raise JSON_Exception('  Empty File')
        
        if len(self.jsonStr) == 1:
            raise JSON_Exception('  File has only 1 character')
        
        self.skip_whitespace()

        if self.jsonStr[self.index] not in ["{"]:
           raise JSON_Exception('a valid JSON payload should be an object or array {}\n')
        
        breakpoint()

        result = self.parseValue()
        '''
        if not result:
            raise JSON_Exception(f'     Missing closing brace')
        '''
        try:
            self.skip_whitespace()
            char = self.jsonStr[self.index]
            raise JSON_Exception(f'     Extra character "{char}" after closing brace\n')
        except IndexError:
            pass

        return result
        
    # Parses the value accordingly
    def parseValue(self):

        breakpoint()

        result = self.parseString()
        if result == None:
            result = self.parseBoolAndNull()
        if result == None:
            result = self.parseObject()
        return result
    
    # Parses boolean values
    def parseBoolAndNull(self):

        try:
            # if bool or null
            if self.jsonStr[self.index] in ['f', 't', 'n']:
                boolStr = ""
                while self.jsonStr[self.index].isalpha():
                    boolStr += self.jsonStr[self.index]
                    self.index += 1
                if boolStr not in BOOL_OR_NULL.keys():
                    raise JSON_Exception(f"expecting boolean (true or false) or Null (null) values")
                return boolStr
        except IndexError:
            raise JSON_Exception(f"     index failure in parseBool")
        except Exception as e:
            raise JSON_Exception(f'{e}')
        return None

    # Parses string values
    def parseString(self):

        breakpoint()

        try:
            if self.jsonStr[self.index] == '"':
                result = ""
                self.index += 1
                self.skip_whitespace()
                while self.jsonStr[self.index] != '"':
                    result += self.jsonStr[self.index]
                    self.index += 1
                self.index += 1
                return result
        except IndexError:
            raise JSON_Exception(f"     Missing closing quote")
        except Exception as e:
            raise JSON_Exception(f'     failed while parsing string value: {e}')
        return None

    # Parses the JSON Object or inner objects
    def parseObject(self):
        try:
            if self.jsonStr[self.index] == "{":
                self.index += 1
                self.depth += 1
                self.skip_whitespace()
                result = {}
                openingBrace = True
                
                while self.jsonStr[self.index] != "}":
                    
                    if not openingBrace:
                        self.skip_whitespace()
                        self.process_comma()
                        self.skip_whitespace()

                    key = self.parseString()
                    if not key:
                        raise JSON_Exception(f"     Key expected")
                    
                    self.skip_whitespace()
                    self.process_colon()
                    self.skip_whitespace()

                    value = self.parseValue()
                    if not value:
                        raise JSON_Exception(f"     Value expected")
                    
                    if value in BOOL_OR_NULL.keys():
                        value = BOOL_OR_NULL[value]
                    
                    result[key] = value
                    self.skip_whitespace()
                    openingBrace = False

                self.index += 1
                self.depth -= 1
                return result
        except IndexError:
                raise JSON_Exception(f"     Missing closing brace")
        
        return None
if __name__ == '__main__':
    jsonParser = JSON_Parser()
    test = '{"key": "value"}'
    result = jsonParser.jsonParse(test)
    print(result)