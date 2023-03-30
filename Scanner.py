from typing import List
from Token import Token
from TokenType import TokenType

class Scanner:
    def __init__(self) -> None:
        self.initialStrList: List[str] = []
        self.tokenList: List[Token] = []
    def initiate(self, stringArray: List[str]):
        self.initialStrList = stringArray
    def populate(self):
        lexeme: str
        for lexeme in self.initialStrList:
            if lexeme == "+":
                newToken = Token("+", "+", TokenType.PLUS)
                self.tokenList.append(newToken)
            elif lexeme == "-":
                newToken = Token("-", "-", TokenType.MINUS)
                self.tokenList.append(newToken)
            elif lexeme == "*":
                newToken = Token("*", "*", TokenType.MULTIPLY)
                self.tokenList.append(newToken)
            elif lexeme == "/":
                newToken = Token("/", "/", TokenType.DIVIDE)
                self.tokenList.append(newToken)
            elif lexeme == "like":
                newToken = Token("like", "", TokenType.LIKE)
                self.tokenList.append(newToken)
            elif lexeme == "grah":
                newToken = Token("grah", "", TokenType.GRAH)
                self.tokenList.append(newToken)
            elif lexeme == "in_ha_mood":
                newToken = Token("in_ha_mood", "in_ha_mood", TokenType.IN_HA_MOOD)
                self.tokenList.append(newToken)
            elif lexeme == "boys_a_liar":
                newToken = Token("boys_a_liar", "boys_a_liar", TokenType.BOYS_A_LIAR)
                self.tokenList.append(newToken)
            elif lexeme == "damn":
                newToken = Token("damn", "", TokenType.DAMN)
                self.tokenList.append(newToken)
            elif lexeme == "[]":
                newToken = Token("[]", [], TokenType.ARRAY)
                self.tokenList.append(newToken)
            elif lexeme == "eat_it_for_lunch":
                newToken = Token("eat_it_for_lunch", "eat_it_for_lunch", TokenType.EAT_IT_FOR_LUNCH)
                self.tokenList.append(newToken)
            elif lexeme == "munch":
                newToken = Token("munch", "munch", TokenType.MUNCH)
                self.tokenList.append(newToken)
            elif lexeme == "grab":
                newToken = Token("grab", "grab", TokenType.GRAB)
                self.tokenList.append(newToken)
            elif lexeme == "then":
                newToken = Token("then", "then", TokenType.THEN)
                self.tokenList.append(newToken)
            elif lexeme == "duhduhduh":
                newToken = Token("duhduhduh", "duhduhduh", TokenType.DUHDUHDUH)
                self.tokenList.append(newToken)
            elif lexeme == "hold_on":
                newToken = Token("hold_on", "hold_on", TokenType.HOLD_ON)
                self.tokenList.append(newToken)
            elif lexeme == "you_thought_i_was_feelin_u?":
                newToken = Token(lexeme, lexeme, TokenType.YOU_THOUGHT_I_WAS_FEELIN_YOU)
                self.tokenList.append(newToken)
            elif lexeme in ["(", ")", "[", "]", "{", "}", "a", "that"]:
                continue
            elif lexeme.isdigit():
                newToken = Token(lexeme, lexeme, TokenType.INT)
                self.tokenList.append(newToken)
            elif not lexeme.isdigit() and type(lexeme) is str:
                newToken = Token(lexeme, lexeme, TokenType.STRING)
                self.tokenList.append(newToken)
            else:
                print("flag")
    def getTokens(self):
        return self.tokenList
    def showTokens(self):
        for token in self.tokenList:
            print(token)

