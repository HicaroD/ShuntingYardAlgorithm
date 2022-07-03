from sy import ShuntingYard
from lexer import Lexer


def main():
    expressions = ["2+3", "5+3+4", "5*3+4", "8/4/2"]

    # REPL
    while 1:
        try:
            expression = input("> ")

            lexer = Lexer(expression)
            tokens = lexer.tokenize()

            shunting_yard = ShuntingYard(tokens)
            rpn_expression = shunting_yard.get_rpn()
            print(f"{expression} = {rpn_expression}")

        except (ValueError, NotImplementedError) as e:
            print(e)
            exit(1)

        except EOFError:
            exit(1)
