#!/usr/bin/env python3

program = "write(\"Hello World\")"

stack = []

def KWWrite():
    if op == 'write':
        return Identifier('write')
    # StringLit()

def OpenParen():
    contents = {
        "Token": op,
        "Next Token": op
    }
    # print(contents)
    print("I saw an open parentheses")
def CloseParen():
    print("I saw a close parenteses")
def StringLit():
    if op == '"':
        print("Start of String")
        stack.append(op)
        a = stack.pop()
        print(a)
        # print(f"{Identifier('write')}: {a}")
        if op == '"':
            print("done string")
    if len(op) < 0 or op != '"':
        print("Continously Looping the String")
    if op == ')':
        print("It used to be end of string but found out in close parentheses")
def Identifier(identname: str):
    if identname == 'write':
        print("I saw a write keyword")
for op in program:
    # print(op)
    if op == 'write':
        KWWrite()
    if op == '(':
        OpenParen()
    elif op == '"':
        Identifier('write')
    elif op == ')':
        CloseParen()
    else:
        pass
        # print(f"Unknown Token {op}")

    #print(op)
