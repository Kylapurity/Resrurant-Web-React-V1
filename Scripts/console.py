#!/usr/bin/python3

import cmd
from imaplib import _CommandResults

class MyConsole(cmd.Cmd):
    "Am making a command line"
    prompt = '>'
    intro = "Welcome to my command line"
    def do_hello(self, arg):
        print("Hello World")

    def do_quit(self, line):
        return True
    
    def do_EOF(self, arg):
        """ close the program"""
        print("")
    
    def do_greet(self, arg):
        print("Hello", arg)

    def emptyline(self):
        print("These is a new line")

    def do_add(self, arg):
        print("Adding", arg)

    def do_sub(self, arg):
        print("Subtracting", arg)

    def do_mul(self, arg):
        print("Multiplying", arg)

    if __name__ == '__main__':
     _CommandResults().cmdloop()

