from typing import List
from Token import Token
from TokenType import TokenType

class Scanner:
    def __init__(self) -> None:
        self.initialStrList: List[str] = []
        self.tokenList: List[Token] = []
    def initiate(self, stringArray: List[str]):
        self.initialStrList = stringArray
    def add(self, token):
        self.tokenList.append(token)
    def getTokens(self):
        return self.tokenList
    def showTokens(self):
        for token in self.tokenList:
            print(token)
    def populate(self):
        lexeme: str
        for lexeme in self.initialStrList:
            if lexeme == "+":
                newToken = Token("+", "+", TokenType.PLUS)
                self.add(newToken)
            elif lexeme == "-":
                newToken = Token("-", "-", TokenType.MINUS)
                self.add(newToken)
            elif lexeme == "*":
                newToken = Token("*", "*", TokenType.MULTIPLY)
                self.add(newToken)
            elif lexeme == "/":
                newToken = Token("/", "/", TokenType.DIVIDE)
                self.add(newToken)
            elif lexeme == "like":
                newToken = Token("like", "", TokenType.LIKE)
                self.add(newToken)
            elif lexeme == "grah":
                newToken = Token("grah", "", TokenType.GRAH)
                self.add(newToken)
            elif lexeme == "in_ha_mood":
                newToken = Token("in_ha_mood", "in_ha_mood", TokenType.IN_HA_MOOD)
                self.add(newToken)
            elif lexeme == "boys_a_liar":
                newToken = Token("boys_a_liar", "boys_a_liar", TokenType.BOYS_A_LIAR)
                self.add(newToken)
            elif lexeme == "damn":
                newToken = Token("damn", "", TokenType.DAMN)
                self.add(newToken)
            elif lexeme == "[]":
                newToken = Token("[]", [], TokenType.ARRAY)
                self.add(newToken)
            elif lexeme == "eat_it_for_lunch":
                newToken = Token("eat_it_for_lunch", "eat_it_for_lunch", TokenType.EAT_IT_FOR_LUNCH)
                self.add(newToken)
            elif lexeme == "munch":
                newToken = Token("munch", "munch", TokenType.MUNCH)
                self.add(newToken)
            elif lexeme == "grab":
                newToken = Token("grab", "grab", TokenType.GRAB)
                self.add(newToken)
            elif lexeme == "then":
                newToken = Token("then", "then", TokenType.THEN)
                self.add(newToken)
            elif lexeme == "duhduhduh":
                newToken = Token("duhduhduh", "duhduhduh", TokenType.DUHDUHDUH)
                self.add(newToken)
            elif lexeme == "hold_on":
                newToken = Token("hold_on", "hold_on", TokenType.HOLD_ON)
                self.add(newToken)
            elif lexeme == "you_thought_i_was_feelin_u?":
                newToken = Token(lexeme, lexeme, TokenType.YOU_THOUGHT_I_WAS_FEELIN_YOU)
                self.add(newToken)
            elif lexeme == "hit_wonder":
                newToken = Token(lexeme, lexeme, TokenType.HIT_WONDER)
                self.add(newToken)
            elif lexeme in ["(", ")", "[", "]", "{", "}", "a", "that", "he"]:
                continue
            elif lexeme.isdigit():
                newToken = Token(lexeme, lexeme, TokenType.INT)
                self.add(newToken)
            elif not lexeme.isdigit() and type(lexeme) is str:
                newToken = Token(lexeme, lexeme, TokenType.STRING)
                self.add(newToken)
            else:
                print("flag")

