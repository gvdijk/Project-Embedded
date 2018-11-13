import tkinter as tk

from Python.ui.menu.menu import Menu


class MenuStack:
    class __MenuStack:

        def __init__(self, root: tk.Frame):
            self.stack = []
            pass

    instance: __MenuStack = None
    root: Menu = None

    def __init__(self, root: tk.Frame):
        MenuStack.root = root
        if not MenuStack.instance:
            MenuStack.instance = MenuStack.__MenuStack(root)

    # Go to the passed in Menu, close the current Menu
    @staticmethod
    def next(menu: Menu):
        if len(MenuStack.instance.stack) > 0:
            prev: Menu = MenuStack.instance.stack[-1]
            prev.close()
            prev.pack_forget()

        MenuStack.instance.stack.append(menu)
        menu.pack(expand=False)
        menu.open()

    # Go to the previous Menu, close the current Menu
    @staticmethod
    def back():
        if len(MenuStack.instance.stack) > 1:
            prev = MenuStack.instance.stack.pop()
            prev.close()
            prev.on_delete()
            prev.pack_forget()
            prev.destroy()

        new = MenuStack.instance.stack[-1]
        new.open()

    # Return whether we are in the main menu
    @staticmethod
    def can_back() -> bool:
        return len(MenuStack.instance.stack) > 0
