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
        
        if len(self.jsonStr) == 0:
            raise JSON_Exception('Empty File')
        
        self.skip_whitespace()

        if self.jsonStr[self.index] not in ["{", "["]:
            raise JSON_Exception('a valid JSON payload should be an object or array\n')
        
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

    def parseValue(self):
        result = self.parseObject()
        
        return result
    

    def parseObject(self):
        if self.jsonStr[self.index] == "{":
            self.index += 1
            self.depth += 1
            self.skip_whitespace()
            result = {}
            openingBrace = True
            
            try:
                while self.jsonStr[self.index] != "}":
                    break
            except EOFError:
                print(f"End of JSON object not found")

            self.index += 1
            self.depth += 1
            return result


if __name__ == '__main__':
    jsonParser = JSON_Parser()
        