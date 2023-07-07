#!/usr/bin/python3
"""
consol model, entry point for the consol
"""
import cmd, sys
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """command line interpreter, entry point"""
    prompt = '(hbnb)'

    def do_create(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
