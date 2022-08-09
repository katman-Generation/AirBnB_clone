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
    my_classes = ["BaseModel", "User", "Place", "State", "Amenity", "Review",
                                                                    "City"]

    def do_quit(self, args):
        """
            Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
            EOF command exits out of the command interpreter
        """
        print()
        return True
        """
            avoid any execution when enter is hit in empty line
        """
        pass 

if __name__ == '__main__':
        HBNBCommand().cmdloop()
