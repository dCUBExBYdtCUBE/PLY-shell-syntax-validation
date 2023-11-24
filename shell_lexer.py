import ply.lex as lex

tokens = ('EQUALS','WHILE','ASSIGN','NUMBER','PLUS','MINUS','MULT','DIV','LSQR','RSQR','LT','GT','EQ','ID', 'UNTIL', 'DO',
          'DONE', 'IN', 'FOR', 'ECHO', 'STRING', 'IF','THEN', 'FI','PLUSPLUS','SEMICOLON','LPAREN','RPAREN',
          'SELECT', 'CASE', 'ESAC','BREAK','BAR','DOL','GE','LE','QUOTE')  #,'SENTENCE'
reserved = {'while': 'WHILE', 'if': 'IF', 'do': 'DO', 'done': 'DONE', 'until': 'UNTIL', 'for': 'FOR', 'in': 'IN', 'echo':'ECHO', 'then':'THEN', 'fi':'FI',
            'select':'SELECT','case':'CASE','esac':'ESAC','break':'BREAK','else':'ELSE'}


t_ignore = ' \t\n' #ignoring space and tabs
t_DOL = r'\$'
t_SEMICOLON = r';'
t_EQUALS = r'\=\='
t_ASSIGN=r'\='
t_PLUS=r'\+'
t_MINUS=r'-'
t_MULT=r'\*'
t_DIV=r'/'
t_LSQR=r'\['
t_QUOTE = r'\"|\''
t_RSQR=r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LT=r'<'
t_GT=r'>'
t_GE=r'>\='
t_LE=r'<\='
t_PLUSPLUS = r'\+\+'
t_NUMBER=r'\d+'
t_BAR = r'\|'

# def t_SENTENCE(t):
#     r'".*?"'
#     return t

# def t_SENTENCE(t):
#     r'"[^"]*"'
#     return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID') #checks for reserved words
    return t

def t_EQ(t):
    r'=='
    return t

def t_WHILE(t):
    r'while'
    return t

def t_DONE(t):
    r'done'
    return t

# def t_STRING(t):
#     r'\"[^\"]*\"'
#     return t

# def t_STRING(t):
#     r'\"(?!\\\$)[^"]*\"'
#     return t

def t_STRING(t):
    r'\"(\\.|[^"\\])*\"'
    return t

def t_error(t): 
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

