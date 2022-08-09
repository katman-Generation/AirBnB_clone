#!/usr/bin/python3
'''
The Cmd class provides a
framework for writing line-oriented command interpreters
'''
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

   def do_EOF(self, line):
       """
        Exit the program on keyboard shortcut Ctr-D
        :param line:
        :return:
        """
       print()
       return True

    def do_quit(self, line):
        """
        Exit the program when you type keyword quit
        :param line:
        :return:
        """
        return True

    def emptyline(self):
        """
        An requested, an empty line + ENTER shouldnt execute anything.
        So it will overwrite default behaviour to repeat the most recent command
        :return:
        """
        pass



if __name__ == "__main__":
    HBNBCommand().cmdloop()
