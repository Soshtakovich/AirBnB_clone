### AirBnB Clone Project

This project aims to create an AirBnB clone, which includes building a command interpreter to manage AirBnB objects. The command interpreter allows users to create, retrieve, update, and delete objects, as well as perform operations like counting and computing statistics.

### Command Interpreter

#### How to Start:
To start the command interpreter, execute the `console.py` script using Python 3. You can do this by running the following command in your terminal:

```
$ ./console.py
```

#### How to Use:
Once the command interpreter is started, you will see a prompt `(hbnb)` waiting for your input. You can type various commands to perform operations on AirBnB objects. Some of the supported commands include:

- `create`: Create a new object (e.g., User, State, City, Place).
- `show`: Show details of a specific object.
- `update`: Update attributes of an object.
- `destroy`: Delete an object.
- `all`: Show all objects or objects of a specific class.
- `count`: Count the number of objects.
- `quit` or `EOF`: Exit the command interpreter.

#### Examples:
- To create a new User object:
```
(hbnb) create User
```

- To show details of a specific object (replace `<id>` with the actual object ID):
```
(hbnb) show User <id>
```

- To update attributes of an object (replace `<id>` and `<attribute>` with actual values):
```
(hbnb) update User <id> <attribute> <value>
```

- To delete an object:
```
(hbnb) destroy User <id>
```

- To count the number of objects of a specific class:
```
(hbnb) count User
```

- To exit the command interpreter:
```
(hbnb) quit
```

### Authors
- [Your Name](https://github.com/your_username)
- [Contributor 1](https://github.com/contributor1_username)
- [Contributor 2](https://github.com/contributor2_username)

Please refer to the `AUTHORS` file for a list of all individuals who have contributed to this project.