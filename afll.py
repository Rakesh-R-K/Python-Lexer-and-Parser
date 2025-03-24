import ply.lex as lex
import ply.yacc as yacc

# List of token names
tokens = (
    'LAMBDA', 'COLON', 'COMMA', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'LPAREN', 'RPAREN', 'FOR', 'IN', 'TRY', 'EXCEPT', 'DEF', 'YIELD',
    'PASS', 'IDENTIFIER', 'STRING', 'NUMBER', 'PLUS'
)

# Regular expression rules for simple tokens
t_LAMBDA = r'lambda'
t_COLON = r':'
t_COMMA = r','
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_FOR = r'for'
t_IN = r'in'
t_TRY = r'try'
t_EXCEPT = r'except'
t_DEF = r'def'
t_YIELD = r'yield'
t_PASS = r'pass'
t_PLUS = r'\+'
t_STRING = r'\"[a-zA-Z_][a-zA-Z0-9_]*\"'

# Reserved words
reserved = {
    'lambda': 'LAMBDA',
    'for': 'FOR',
    'in': 'IN',
    'try': 'TRY',
    'except': 'EXCEPT',
    'def': 'DEF',
    'yield': 'YIELD',
    'pass': 'PASS'
}

# IDENTIFIER rule, with reserved word check
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

t_NUMBER = r'[0-9]+'

# Ignored characters (whitespace)
t_ignore = " \t"

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules

def p_start(p):
    '''start : lambda_func
             | dict_decl
             | list_comprehension
             | try_except
             | generator_func'''
    pass

def p_lambda_func(p):
    '''lambda_func : LAMBDA params COLON expression'''
    print("Lambda function recognized")

def p_params(p):
    '''params : IDENTIFIER
              | IDENTIFIER COMMA params'''
    pass

def p_dict_decl(p):
    '''dict_decl : LBRACE pairs RBRACE'''
    print("Dictionary recognized")

def p_pairs(p):
    '''pairs : pair
             | pair COMMA pairs'''
    pass

def p_pair(p):
    '''pair : STRING COLON expression'''
    pass

def p_list_comprehension(p):
    '''list_comprehension : LBRACKET expression FOR IDENTIFIER IN expression RBRACKET'''
    print("List comprehension recognized")

def p_try_except(p):
    '''try_except : TRY COLON block EXCEPT COLON block'''
    print("Try-except block recognized")

def p_block(p):
    '''block : statement
             | statement block'''
    pass

def p_generator_func(p):
    '''generator_func : DEF IDENTIFIER LPAREN RPAREN COLON yield_block'''
    print("Generator function recognized")
def p_yield_block(p):
    '''yield_block : yield_statement
                   | yield_statement block'''
    pass
def p_yield_statement(p):
    '''yield_statement : YIELD expression'''
    pass
def p_statement(p):
    '''statement : YIELD expression
                 | PASS'''
    pass
# Define operator precedence
precedence = (
    ('left', 'PLUS'),
)

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | expression PLUS expression
                  | IDENTIFIER LPAREN expression RPAREN'''
    pass

# Error rule for syntax errors
def p_error(p):
    print(p)
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test cases for the constructs
test_cases = [
    'lambda x, y: x + y',                   # Lambda function
    '{"key": value, "name": John}',         # Dictionary declaration
    '[x for x in range(10)]',               # List comprehension
    'try: pass except: pass',               # Try-except block
    'def gen(): yield x'                    # Generator function with yield
]

# Parse each test case
for test in test_cases:
    print(f"\nTesting: {test}")
    # lexer.input(test)
    # print(f"Tokens for '{test}':")
    # for token in lexer:
    #     print(f"Token(type='{token.type}', value='{token.value}')")
    # print("-" * 40)
    result = parser.parse(test, lexer=lexer)
    if result is None:
        print("Parsed successfully")
    else:
        print("Parsing failed")
