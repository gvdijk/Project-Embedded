import tkinter as tk

from Python.ui.menu.menu import Menu


class MenuStack:
    class __MenuStack:

        def __init__(self, root: tk.Frame):
            self.stack = [root]
            pass

    instance: __MenuStack = None
    root: Menu = None

    def __init__(self, root: tk.Frame):
        MenuStack.root = root
        if not MenuStack.instance:
            MenuStack.instance = MenuStack.__MenuStack(root)

    @staticmethod
    def next(menu: Menu):
        MenuStack.instance.stack.append(menu)
        menu.pack(expand=False)
        return menu

    @staticmethod
    def back():
        if len(MenuStack.instance.stack) > 1:
            menu = MenuStack.instance.stack.pop()
            print(menu)
            menu.destroy()

        return MenuStack.instance.stack[-1]

    @staticmethod
    def can_back() -> bool:
        return len(MenuStack.instance.stack) > 1
