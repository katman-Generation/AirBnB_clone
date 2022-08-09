#!/usr/bin/python3
'''
The Cmd class provides a
framework for writing line-oriented command interpreters
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
beginning of interpreter
    '''
    prompt = "(hbnb) "
    classes = {"BaseModel", "State", "City","Amenity", "Place", "Review", "User"}

    def do_EOF(self, inp):
        '''
    Exit program with ctr-D
        '''
        print()
        return True

    def do_quit(self, inp):
        '''
    Exit program with quit
        '''
        return True

    def emptyline(self):
        '''
    Emptyline + enter should execute nothing
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
