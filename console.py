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
        class = args_list[0]
        current_dict_dict = storage.all()
        print_list = []
        if len(args_list) == 0:
            for dict in current_dict_dict.items():
                for key, value in dict.items():
                    print_list.append(value)
                    print(print_list)
#        if class not in class_dict.keys():
 #           print("** class doesn't exist **")
  #      else:
   #         for dict in current_dict_dict.items():
    #            for key, value in dict.items():
     #               if value[__class__] == class:
      #                  print_list.append(value)

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
