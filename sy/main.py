class ShuntingYard:
    def __init__(self, expression: str):
        self.expression = expression
        self.cursor = 0
        self.current_token = None

        if not self.is_expression_empty():
            self.current_token = self.expression[0]

    def is_expression_empty(self):
        return not self.expression or self.expression.isspace()

    def is_end_of_expression(self):
        return self.cursor >= len(self.expression)

    def advance(self):
        if not self.is_end_of_expression():
            self.cursor += 1

    def rank_precedence(self, token) -> int:
        match token:
            case "+":
                return 0
            case "-":
                return 0
            case "*":
                return 2
            case "/":
                return 2
            case _:
                return -1

    def is_operator(self, token):
        return token in {"+", "-", "/", "*"}

    def get_rpn(self):
        output = []
        stack = []

        if self.current_token != None:
            while not self.is_end_of_expression():
                # TODO: Add support to multiple digits numbers
                if self.current_token.isdigit():
                    output.append(self.current_token)
                    self.advance()

                elif self.is_operator(self.current_token):
                    self.advance()

                elif self.current_token == '(':
                    stack.append(self.current_token)
                    self.advance()

                elif self.current_token == ')':
                    self.advance()

                else:
                    raise NotImplementedError(f"Invalid token: {self.current_token}")
        else:
            raise ValueError("Empty expression")

        return self.expression


def main():
    expressions = ["2+3", "5+3+4", "5*3+4", "8/4/2^"]

    for expression in expressions:
        try:
            shunting_yard = ShuntingYard(expression)
            rpn_expression = shunting_yard.get_rpn()
            print(f"{expression} = {rpn_expression}")
        except ValueError as e:
            print(e)
            exit(1)
