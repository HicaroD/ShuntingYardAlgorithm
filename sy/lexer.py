from enum import Enum
from dataclasses import dataclass


class Associativity(Enum):
    Left = 1
    Right = 2
    Undefined = 3


class TokenKind(Enum):
    # Operators
    PlusOp = 1
    MinusOp = 2
    DividesOp = 3
    TimesOp = 4

    # Special characters
    LeftPar = 5
    RightPar = 6

    Number = 7

    EOF = 8


@dataclass
class Token:
    kind: TokenKind
    lexeme: str

    def __repr__(self):
        return f"{self.kind}({self.lexeme})"

    def is_operator(self) -> bool:
        return self.kind in {
            TokenKind.PlusOp,
            TokenKind.MinusOp,
            TokenKind.DividesOp,
            TokenKind.TimesOp,
        }

    def get_associativity(self) -> Associativity:
        match self.kind:
            case TokenKind.PlusOp | TokenKind.MinusOp | TokenKind.TimesOp | TokenKind.DividesOp:
                return Associativity.Left
            case _:
                return Associativity.Undefined


class Lexer:
    def __init__(self, expression: str) -> None:
        self.expression = expression
        self.position = 0
        self.current_char = expression[self.position]

    def is_end_of_expression(self) -> bool:
        return self.position >= len(self.expression)

    def skip_whitespace(self):
        if self.current_char == " ":
            self.advance()

    def advance(self) -> None:
        self.position += 1
        if not self.is_end_of_expression():
            self.current_char = self.expression[self.position]

    def get_number(self) -> Token:
        number = ""
        while self.current_char.isdigit() and not self.is_end_of_expression():
            number += self.current_char
            self.advance()
        return Token(TokenKind.Number, number)

    def consume_and_advance(self, token: Token) -> Token:
        self.advance()
        return token

    def get_token(self) -> Token:
        match self.current_char:
            case "(":
                return self.consume_and_advance(Token(TokenKind.LeftPar, "("))

            case ")":
                return self.consume_and_advance(Token(TokenKind.RightPar, ")"))

            case "+":
                return self.consume_and_advance(Token(TokenKind.PlusOp, "+"))

            case "-":
                return self.consume_and_advance(Token(TokenKind.MinusOp, "-"))

            case "*":
                return self.consume_and_advance(Token(TokenKind.TimesOp, "*"))

            case "/":
                return self.consume_and_advance(Token(TokenKind.DividesOp, "/"))

            case _:
                if self.current_char.isdigit():
                    number = self.get_number()
                    return number
                else:
                    raise ValueError(f"Invalid token: {self.current_char}")

    def tokenize(self) -> list[Token]:
        tokens = []

        while not self.is_end_of_expression():
            try:
                self.skip_whitespace()
                token = self.get_token()
                tokens.append(token)
            except ValueError as e:
                print(f"{e}")
                exit(1)

        return tokens
