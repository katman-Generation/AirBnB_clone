#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def do_EOF(self, inp):
        '''
        exiting the program at an unexpected end of file
        '''
        print()
        return True

    def do_quit(self, inp):
        '''
        Quit command to exit the program

        '''
        return True

    def emptyline(self):
        '''
         an empty line and enter should not execute anything
        '''
        pass



if __name__ == "__main__":
    HBNBCommand().cmdloop()
