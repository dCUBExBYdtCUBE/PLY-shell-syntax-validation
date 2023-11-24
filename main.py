from shell_lexer import lexer
from shell_parser import parser

file_path = r"D:/Suhas/1Data transfer/3rd Sem/afll/if_eg.txt"

try:
    with open(file_path, 'r') as file:
        input_string = file.read()

    # Give the lexer the input string
    lexer.input(input_string)

    # Tokenize and print the tokens
    for token in lexer:
        print(token)

    # Parse the input string
    try:
        result = parser.parse(input_string)
        print("Parsing successful.")
        # You can do something with the parsed result here if needed.
    except Exception as parse_error:
        print(f"Parsing failed: {parse_error}")

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
