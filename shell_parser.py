import ply.yacc as yacc
from shell_lexer import tokens

def p_main(p):
    'main : Statements'
    print("Syntax is Correct.")

def p_Statements(p):
    '''
    Statements : IF LSQR cond RSQR SEMICOLON Statements
               | UNTIL LSQR cond RSQR DO Statements DONE Statements
               | UNTIL LSQR cond RSQR SEMICOLON DO Statements DONE Statements
               | ID ASSIGN LSQR sep_id RSQR Statements
               | ID ASSIGN LSQR RSQR Statements
               | ID ASSIGN expression Statements
               | empty
               | FOR ID IN sep_id DO Statements DONE Statements
               | ECHO STRING Statements
               | IF LSQR cond RSQR SEMICOLON THEN Statements FI Statements
               | IF LSQR cond RSQR THEN Statements FI Statements
               | SELECT ID IN options DO CASE DOL ID IN cases ESAC DONE
               | LPAREN LPAREN ID rel RPAREN RPAREN
               | LPAREN LPAREN factor RPAREN RPAREN
    '''

def p_cases(p):
    '''cases : cases_body cases
             | cases_body
    '''

def p_cases_body(p):
    '''cases_body : options1 RPAREN options2 SEMICOLON SEMICOLON '''

def p_options(p):
    '''
    options : ID options
            | ID
    '''

def p_options1(p):
    '''
    options1 : ID BAR options1
            | ID
            | MULT
    '''

def p_options2(p):
    '''
    options2 : ECHO QUOTE primary QUOTE
            | ECHO primary
            | BREAK
    '''

def p_cond(p):
    '''
    cond : term rel term
        | empty
        | ID
        | QUOTE DOL cond QUOTE
    '''

def p_rel(p):
    '''
    rel : GT
        | LT
        | EQ
        | GE
        | LE
    '''

def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | expression MULT term
               | expression DIV term
               | expression PLUSPLUS
               | term
               | empty
    '''



def p_sep_id(p):
    '''
    sep_id : ID sep_id
           | ID
    '''

def p_term(p):
    '''
    term : factor
         | term MULT factor
         | term DIV factor
    '''

def p_factor(p):
    '''
    factor : primary
           | factor PLUSPLUS
    '''

def p_primary(p):
    '''
    primary : ID
            | NUMBER
            | STRING
            | LPAREN expression RPAREN
    '''


def p_empty(p):
    '''empty :'''



def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        print("Syntax error: Unexpected end of input")
    exit(1)


parser = yacc.yacc()
