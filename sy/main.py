from lexer import Lexer, Token


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


def main():
    expressions = ["2+3", "5+3+4", "5*3+4", "8/4/2"]

    for expression in expressions:
        try:
            lexer = Lexer(expression)
            tokens = lexer.tokenize()

            shunting_yard = ShuntingYard(tokens)
            rpn_expression = shunting_yard.get_rpn()
            print(f"{expression} = {rpn_expression}")
        except (ValueError, NotImplementedError) as e:
            print(e)
            exit(1)
