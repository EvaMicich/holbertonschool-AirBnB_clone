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
            print(f"** instance id missing **")
        else:
            key = f"{args_list[0]}.{args_list[1]}"
            current_dict = storage.all()
            try:
                print(current_dict[key])
            except:
                print("** no instance found **")

    def do_destroy(self, *args):
        'Deletes an instance based on the class name and id: destroy\
BaseModel 1234-1234-1234'
        args_list = args[0].split()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print(f"** instance id missing **")
        else:
            key = f"{args_list[0]}.{args_list[1]}"
            current_dict = storage.all()
            try:
                del current_dict[key]
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, *args):
        'Prints all string representation of all instances\
based or not on the class name: all BaseModel or all'
        args_list = args[0].split()
        current_dict = storage.all()
        print_list = []
        if len(args_list) == 0:
            for obj_tuple in current_dict.items():
                print_list.append(obj_tuple[1].__str__())
            print(print_list)
            return
        class_name = args_list[0]
        if class_name not in self.class_dict.keys():
            print("** class doesn't exist **")
        else:
            for obj_tuple in current_dict.items():
                instance = obj_tuple[1]
                instance_class = str(instance.__class__.__name__)
                if instance_class == class_name:
                    print_list.append(instance.__str__())
            print(print_list)


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
