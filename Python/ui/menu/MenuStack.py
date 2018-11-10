from Python.ui.menu.menu import Menu
import tkinter as tk


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
    def next(menu: Menu) -> Menu:
        MenuStack.instance.stack.append(menu)
        menu.grid(row=0, sticky="nsew")
        return menu

    @staticmethod
    def back() -> Menu:
        if len(MenuStack.instance.stack) > 1:
            menu = MenuStack.instance.stack.pop()
            menu.destroy()
        return MenuStack.instance.stack[-1]
