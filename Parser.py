from Scanner import Scanner
from Token import Token
from TokenType import TokenType
import os
import contextlib
a = Scanner()
file = open("test.mood","r+").read()

if file.split()[0] != "you_thought_i_was_feelin_u?":
    quit()

class Variable():
    def __init__(self, name, value, type) -> None:
        self.name = name
        self.value = value
        self.type = type

    def __str__(self) -> str:
        return (
                    "VAR_NAME " 
                    + str(self.name) 
                    + " VAR_VALUE " 
                    + str(self.value) 
                    + " VAR_TYPE " 
                    + str(self.type)
        )
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
    def printStack(self):
        for token in self.stack:
            print(token)
    def printMemory(self):
        for variable in self.memory:
            print(self.memory[variable])
    def parseTokens(self):
        # if self.scanner.getTokens()[0].type != TokenType.YOU_THOUGHT_I_WAS_FEELIN_YOU:
        #     continue
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
                top, arr = self.getTop(), self.getTop()
                name = arr.lexeme
                newVar = Variable(
                    top.content, 
                    top.content, 
                    top.type
                )
                arrAccess = self.memory[name].value
                arrAccess.append(newVar)
            elif token.type == TokenType.MUNCH:
                top, arr = self.getTop(), self.getTop()
                name = arr.lexeme
                arrAccess = self.memory[name].value
                del arrAccess[int(top.content)]
            elif token.type == TokenType.GRAB:
                index, arr = self.getTop(), self.getTop()
                name = arr.lexeme
                arrAccess = self.memory[name].value
                grabbed = (arrAccess[int(index.content)])

                self.add(grabbed.toToken())

                # we need a type conversion for grabbed
            elif token.type == TokenType.THEN:
                eval = self.getTop()
                if eval.type == TokenType.BOYS_A_LIAR:
                    curr_index = (self.scanner
                                    .getTokens()
                                    .index(token)
                    )
                    next_index = curr_index + 1
                    flag = 0
                    while flag == 0:
                        next_token = self.scanner.getTokens()[next_index]
                        if next_token.type == TokenType.DUHDUHDUH:
                            flag = 1
                        else:
                            del self.scanner.getTokens()[next_index]
                    # del self.scanner.getTokens()[next_index]

            elif token.type == TokenType.HOLD_ON:
                s2, s1 = self.getTop(), self.getTop()

                concatToken = Token(s1.content 
                                        + " " 
                                        + s2.content, 
                                    s1.content 
                                        + " " 
                                        + s2.content,
                                     TokenType.STRING
                )
                self.add(concatToken)
            elif token.type == TokenType.GRAH:
                top = self.getTop()
                
                if top.content.__class__ == list:
                    print("[", end=" ")
                    for element in top.content:
                        print(str(element.value), end = " ")
                    print("]", end=" ")
                else:
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
                    self.add(
                        Token(
                            "in ha mood", 
                            "in ha mood", 
                            TokenType.IN_HA_MOOD
                        )
                )
                else:
                    self.add(
                        Token(
                            "boys a liar", 
                            "boys a liar", 
                            TokenType.BOYS_A_LIAR
                        )
                )
            elif token.type == TokenType.HIT_WONDER:
                end = int(self.getTop().content)
                start = int(self.getTop().content)

                local_tokens = []
                curr_index = (self.scanner
                                .getTokens()
                                .index(token)
                )
                next_index = curr_index + 1

                flag = 0
                while flag == 0:
                    next_token = self.scanner.getTokens().pop(next_index)
                    if next_token.type == TokenType.DUHDUHDUH:
                        flag = 1
                    else:
                        local_tokens.append(next_token)
                for i in range(start, end):
                    b = Scanner()
                    localParser = Parser(b)
                    localParser.memory = self.memory
                    localParser.scanner.tokenList = local_tokens
                    localParser.parseTokens()

                
            elif token.type == TokenType.YOU_THOUGHT_I_WAS_FEELIN_YOU:
                print("\n" + "SPICESCRIPT v0.1 -- " + os.getcwd() + "\n\n")
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
                newMinusToken = Token(str(num1) + " - " + str(num2), res, TokenType.INT)
                self.stack.append(newMinusToken)
            elif token.type == TokenType.MULTIPLY:
                num2 = self.getTop().content
                num1 = self.getTop().content
                
                res = int(num1) - int(num2)
                newMultiplyToken = Token(num1 
                                            + " * " 
                                            + num2, 
                                        res, 
                                        TokenType.INT
                )
                self.stack.append(newMultiplyToken)
            elif token.type == TokenType.MULTIPLY:
                num2 = self.getTop().content
                num1 = self.getTop().content
                
                res = int(num1) - int(num2)
                newMultiplyToken = Token(num1 + " / " + num2, res, TokenType.INT)
                self.stack.append(newMultiplyToken)
            
                


n = Parser(a)
# n.scanner.showTokens()
# path = './file.txt'
# with open(path, 'w') as f:
#     with contextlib.redirect_stdout(f):
#         n.parseTokens()
n.parseTokens()
# print(n.memory)
# n.printMemory()
# n.printStack()
