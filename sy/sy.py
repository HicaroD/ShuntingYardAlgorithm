from lexer import Token


class ShuntingYard:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens

    def get_precedence(self, token) -> int:
        match token:
            case "+":
                return 0
            case "-":
                return 0
            case "*":
                return 2
            case "/":
                return 2

    def has_higher_precedence(self, top, current):
        return self.get_precedence(top) > self.get_precedence(current)

    def get_rpn(self):
        output = []
        stack = []

        for token in self.tokens:
            # TODO: Implement shunting yard algorithm
            print(token)

        return output
