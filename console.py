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

    class_dict = {
        "BaseModel": BaseModel
    }

    def do_create(self, *args):
        'Creates instance of class: create BaseModel'
        args_list = args[0].split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
        else:
            my_model = self.class_dict[args_list[0]]()
            my_model.save()
            print(my_model.id)

    def do_show(self, *args):
        'Prints the string representation of an instance based\
 on the class name and id: show BaseModel 1234-1234-1234'
        args_list = args[0].split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print(f"len arg list {len(args_list)}** instance id missing **")
        else:
            key = f"{args_list[0]}.{args_list[1]}"
            current_dict = storage.all()
            try:
                print(current_dict[key])
            except:
                print("** no instance found **")

    def do_test(self, *args):
        args_list = args[0].split()
        print(args_list)
        print(len(args_list))

        if len(*args) == 0:
            print("** class name missing **")
        elif args[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
#        else:
#            try:
#                my_dummy = self.class_dict[args[0]]()
#                FileStorage.reload()
#            my_model = self.class_dict[args[0]]()
#            my_model.save()
#            print(my_model.id)

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
