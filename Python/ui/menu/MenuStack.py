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

    @staticmethod
    def next(menu: Menu):
        if len(MenuStack.instance.stack) > 0:
            MenuStack.instance.stack[-1].pack_forget()

        MenuStack.instance.stack.append(menu)
        menu.pack(expand=False)
        return menu

    @staticmethod
    def back():
        if len(MenuStack.instance.stack) > 0:
            menu = MenuStack.instance.stack.pop()
            menu.destroy()

        return MenuStack.instance.stack[-1]

    @staticmethod
    def can_back() -> bool:
        return len(MenuStack.instance.stack) > 0
