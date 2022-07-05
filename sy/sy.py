from lexer import Token, TokenKind, Associativity


class ShuntingYard:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens

    def get_precedence(self, token: Token) -> int:
        match token:
            case TokenKind.PlusOp | TokenKind.MinusOp: return 0
            case TokenKind.TimesOp | TokenKind.DividesOp: return 2

    def has_higher_precedence(self, top: Token, current: Token) -> bool:
        return self.get_precedence(top.kind) > self.get_precedence(current.kind)

    def has_same_precedence(self, top, current) -> bool:
        return self.get_precedence(top.kind) == self.get_precedence(current.kind)

    def get_rpn_expression(self) -> list[Token]:
        operators = []
        operands = []

        for token in self.tokens:
            match token.kind:
                case TokenKind.Number:
                    operands.append(token)

                case TokenKind.LeftPar:
                    operators.append(token)

                case TokenKind.RightPar:
                    left_parenthesis_found = False
                    while operators:
                        if operators[-1].kind is TokenKind.LeftPar:
                            left_parenthesis_found = True
                            break
                        else:
                            operands.append(operators.pop())

                    if not operators and not left_parenthesis_found:
                        raise ValueError("Invalid expression")
                    else:
                        # Discard left parenthesis
                        operators.pop()

                case _:
                    if token.is_operator():
                        while operators:
                            top = operators[-1]

                            if (
                                top.kind is not TokenKind.LeftPar
                                and self.has_higher_precedence(top, token)
                                or self.has_same_precedence(top, token)
                                and token.get_associativity() is Associativity.Left
                            ):
                                operands.append(operators.pop())
                            else:
                                break
                        operators.append(token)

                    else:
                        raise ValueError(f"Invalid token: {token}")

        while operators:
            top = operators[-1]
            if top.kind == TokenKind.LeftPar:
                raise ValueError("Error: Mismatched parenthesis")
            operands.append(operators.pop())

        return operands
