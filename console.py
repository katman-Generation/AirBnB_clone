#!/usr/bin/python3
"""
    contains the entry point of the command interpreter:
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
        command interprete
    """

    prompt = '(hbnb) '
    
    def do_EOF(self, args):
        """
            EOF command exits out of the command interpreter
        """
        print()
        return True

    def do_quit(self, args):
        """
            Quit command to exit the program
        """
        return True

        """
            EOF command exits out of the command interpreter
        """
        pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()
