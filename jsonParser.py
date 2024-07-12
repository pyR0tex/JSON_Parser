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
    
    # Entry from isJSON.py
    def jsonParse(self, fileContent):
        self.index = 0
        self.jsonStr = fileContent
        self.depth = 0
        
        if len(self.jsonStr) == 0:
            raise JSON_Exception('Empty File')
        
        if len(self.jsonStr) == 1:
            raise JSON_Exception('File has only 1 character')
        
        self.skip_whitespace()

        if self.jsonStr[self.index] not in ["{", "["]:
            raise JSON_Exception('a valid JSON payload should be an object or array {{}}, []\n')
        
        result = self.parseValue()

        try:
            self.skip_whitespace()
            char = self.jsonStr[self.index]
            raise JSON_Exception(f'Invalid JSON: Extra character "{char}" after closing brace\n')
        except IndexError:
            pass

        return result

    def skip_whitespace(self):
        while self.index < len(self.jsonStr) and self.jsonStr[self.index] in WHITESPACE:
            self.index += 1

    def process_colon(self):
        if self.index < len(self.jsonStr) and self.jsonStr[self.index] == ":":
            self.index += 1
        else:
            raise JSON_Exception(f"Colon expected after Key")

    # Parses the value accordingly
    def parseValue(self):
        result = self.parseString()
        if result == None:
            result = self.parseObject()
        
        return result
    
    def parseString(self):
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
        except Exception as e:
            raise JSON_Exception(f'Failed while Parsing String: {e}')


    def parseObject(self):
        if self.jsonStr[self.index] == "{":
            self.index += 1
            self.depth += 1
            self.skip_whitespace()
            result = {}
            openingBrace = True
            
            try:
                while self.jsonStr[self.index] != "}":
                    '''
                    Add code for:
                    if not opening brace:
                        skip white
                        colon
                        skip white
                    '''
                    if not openingBrace:
                        self.skip_whitespace()
                        self.process_colon()
                        self.skip_whitespace()

                    key = self.parseString()
                    # at or before colon
                    self.skip_whitespace()
                    self.process_colon()
                    self.skip_whitespace()
                    value = self.parseValue()
                    result[key] = value
                    self.index += 1
                    openingBrace = False

            except Exception as e:
                print(f"{e}")

            self.index += 1
            self.depth -= 1
            return result


if __name__ == '__main__':
    jsonParser = JSON_Parser()
    test = '{"Key" :}'
    result = jsonParser.jsonParse(test)