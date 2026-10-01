#!/usr/bin/env python3
# Created by: Mignonne Gihozo
# Created on: Sept 2026
# This program shows how local and global variables work

# global variable
variable_x = 25


def local_variable() -> None:
    """The local_variable() function creates local variables, returns None."""
    variable_x = 10
    variable_y = 30
    variable_z = variable_x + variable_y
    print(f"Local variable: {variable_x} + {variable_y} = {variable_z}")


def global_variable() -> None:
    """The global_variable() function uses a global variable, returns None."""
    global variable_x
    variable_y = 30
    variable_x = variable_x + 1
    variable_z = variable_x + variable_y
    print(f"Global variable: {variable_x} + {variable_y} = {variable_z}")


# These are the function calls at the bottom of your file
local_variable()
global_variable()

print("\nDone.")
