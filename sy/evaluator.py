from lexer import Token, TokenKind

def evaluate(expression: list[Token]) -> float:
    stack = []
    for token in expression:
        if token.kind is TokenKind.Number:
            number = float(token.lexeme)
            stack.append(number)

        elif token.is_operator():
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            rhs = stack.pop()
            lhs = stack.pop()

            match token.kind:
                case TokenKind.PlusOp: stack.append(lhs + rhs)
                case TokenKind.MinusOp: stack.append(lhs - rhs)
                case TokenKind.TimesOp: stack.append(lhs * rhs)
                case TokenKind.DividesOp: stack.append(lhs / rhs)

    return stack[0]
