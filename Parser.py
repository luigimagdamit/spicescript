from Scanner import Scanner
from Token import Token
from TokenType import TokenType
a = Scanner()
file = open("test.mood","r+").read()

class Variable():
    def __init__(self, name, value, type) -> None:
        self.name = name
        self.value = value
        self.type = type

    def __str__(self) -> str:
        return "VAR_NAME " + str(self.name) + " VAR_VALUE " + str(self.value) + " VAR_TYPE " + str(self.type)
    def toToken(self):
        return Token(self.name, self.value, self.type)

class Parser():
    def __init__(self, scanner: Scanner) -> None:
        self.scanner = scanner
        self.scanner.initiate(file.split())
        self.scanner.populate()

        self.stack = []
        self.memory = {}

    def add(self, n):
        self.stack.append(n)

    def getTop(self):
        return self.stack.pop()
    
    def parseTokens(self):
        token: Token
        for token in self.scanner.getTokens():
            if token.type == TokenType.STRING:
                if token.content not in self.memory:
                    self.add(token)
                elif token.content in self.memory:
                    retrievedVariable = self.memory[token.content].toToken()
                    self.add(retrievedVariable)
            elif token.type == TokenType.INT:
                self.add(token)
            elif token.type == TokenType.IN_HA_MOOD:
                self.add(token)
            elif token.type == TokenType.GRAH:
                top = self.getTop()
                print("GRAH!")
                
                print(top.content)
            elif token.type == TokenType.LIKE:
                top = self.getTop()
                value = top.content
                type = top.type
                name = self.getTop().content

                self.memory[name] =  Variable(name, value, type)
            elif token.type == TokenType.DAMN:
                num1 = self.getTop().type
                num2 = self.getTop().type
                
                if num1 == num2:
                    print("in ha mood")
                    self.add(Token("in ha mood", "in ha mood", TokenType.IN_HA_MOOD))
            elif token.type == TokenType.PLUS:
                num1 = self.getTop().content
                num2 = self.getTop().content

                res = int(num1) + int(num2)
                newPlusToken = Token(str(num1) + " + " + str(num2), res, TokenType.INT)
                self.stack.append(newPlusToken)
            elif token.type == TokenType.MINUS:
                num2 = self.getTop().content
                num1 = self.getTop().content
                
                res = int(num1) - int(num2)
                newMinusToken = Token(num1 + " - " + num2, res, TokenType.INT)
                self.stack.append(newMinusToken)

    def printStack(self):
        for token in self.stack:
            print(token)
    def printMemory(self):
        for variable in self.memory:
            print(self.memory[variable])
            
                


n = Parser(a)
# n.scanner.showTokens()
n.parseTokens()
# print(n.memory)
n.printMemory()
# n.printStack()