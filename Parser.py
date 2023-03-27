from Scanner import Scanner
from Token import Token
from TokenType import TokenType
import os
a = Scanner()
file = open("test.ispice","r+").read()

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
        if self.scanner.getTokens()[0].type != TokenType.YOU_THOUGHT_I_WAS_FEELIN_YOU:
            quit()
        token: Token
        for token in self.scanner.getTokens():
            if token.type == TokenType.STRING:
                if token.content not in self.memory:
                    self.add(token)
                elif token.content in self.memory:
                    retrievedVariable = self.memory[token.content].toToken()
                    retrievedVariable.lexeme = token.content
                    self.add(retrievedVariable)
            elif token.type == TokenType.INT:
                self.add(token)
            elif token.type == TokenType.IN_HA_MOOD:
                self.add(token)
            elif token.type == TokenType.BOYS_A_LIAR:
                self.add(token)
            elif token.type == TokenType.ARRAY:
                self.add(token)
            elif token.type == TokenType.EAT_IT_FOR_LUNCH:
                top = self.getTop()
                arr = self.getTop()
                name = arr.lexeme
                newVar = Variable(top.content, top.content, top.type)
                print("NAME" + name)
                arrAccess = self.memory[name].value
                arrAccess.append(newVar)
            elif token.type == TokenType.MUNCH:
                top = self.getTop()
                arr = self.getTop()
                name = arr.lexeme
                print("NAME" + name)
                arrAccess = self.memory[name].value
                arrAccess.remove(top.content)
            elif token.type == TokenType.GRAB:
                index = self.getTop()
                arr = self.getTop()
                arrAccess = self.memory[name].value
                grabbed = (arrAccess[int(index.content)])

                self.add(grabbed.toToken())
                # we need a type conversion for grabbed
            elif token.type == TokenType.THEN:
                eval = self.getTop()
                if eval.type != TokenType.BOYS_A_LIAR:
                    continue
                if eval.type == TokenType.BOYS_A_LIAR:
                    curr_index = (self.scanner.getTokens().index(token))
                    next_index = curr_index + 1
                    flag = 0
                    while flag == 0:
                        next_token = self.scanner.getTokens()[next_index]
                        if next_token.type == TokenType.DUHDUHDUH:
                            flag = 1
                        else:
                            del self.scanner.getTokens()[next_index]
                    # del self.scanner.getTokens()[next_index]

            # elif token.type == TokenType.DUHDUHDUH:
            #     print(self.stack)
            #     node1 = self.getTop()
            #     eval = self.getTop()

            #     if eval.content == "in_ha_mood":
            #         self.add(node1)
            #     else:
            #         continue
            elif token.type == TokenType.HOLD_ON:
                s2 = self.getTop()
                s1 = self.getTop()

                concatToken = Token(s1.content + " " + s2.content, s1.content + " " + s2.content, TokenType.STRING)
                self.add(concatToken)
            elif token.type == TokenType.GRAH:
                top = self.getTop()
                print("GRAH!")
                
                print(top.content)
            elif token.type == TokenType.LIKE:
                top = self.getTop()
                value = top.content
                type = top.type
                name = self.getTop().lexeme

                self.memory[name] =  Variable(name, value, type)
            elif token.type == TokenType.DAMN:
                num1 = self.getTop()
                num2 = self.getTop()
                if num1.content == num2.content:
                    print("in ha mood")
                    self.add(Token("in ha mood", "in ha mood", TokenType.IN_HA_MOOD))
                else:
                    print("boys a liar")
                    self.add(Token("boys a liar", "boys a liar", TokenType.BOYS_A_LIAR))
            elif token.type == TokenType.YOU_THOUGHT_I_WAS_FEELIN_YOU:
                print("SPICESCRIPT v0.1 -- " + os.getcwd())
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
n.printStack()