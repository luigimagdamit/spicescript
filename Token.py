from TokenType import TokenType
class Token:
    def __init__(self, lexeme, content: any, type: TokenType):
        self.lexeme = lexeme
        self.content = content
        self.type = type
    def __str__(self):
        return f'Lexeme: {self.lexeme} \nContent: {self.content} \nToken: {self.type}'
    
