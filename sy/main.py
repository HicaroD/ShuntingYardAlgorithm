from sy import ShuntingYard
from lexer import Lexer
from evaluator import evaluate


def main():
    # REPL
    while 1:
        try:
            expression = input("> ")

            lexer = Lexer(expression)
            tokens = lexer.tokenize()

            shunting_yard = ShuntingYard(tokens)
            rpn_expression = shunting_yard.get_rpn_expression()
            result = evaluate(rpn_expression)
            print(result)

        except (ValueError, NotImplementedError) as e:
            print(e)
            exit(1)

        except EOFError:
            exit(1)

        except ZeroDivisionError:
            print("Error: Can't divide by zero!")
