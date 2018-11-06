from Python.ui.menu.menu import Menu
import tkinter as tk


class MenuStack:
    class __MenuStack:

        def __init__(self, root_menu: tk.Frame):
            self.stack = [root_menu]
            pass

    instance: __MenuStack = None

    def __init__(self, root_menu: tk.Frame):
        if not MenuStack.instance:
            MenuStack.instance = MenuStack.__MenuStack(root_menu)

    def __getattr__(self, item):
        return getattr(self.instance, item)

    @staticmethod
    def next(menu: Menu) -> Menu:
        MenuStack.instance.stack.append(menu)
        menu.pack(side="top", fill="both", expand=True)
        return menu

    @staticmethod
    def back() -> Menu:
        if len(MenuStack.instance.stack) > 1:
            menu = MenuStack.instance.stack.pop()
            menu.destroy()
        return MenuStack.instance.stack[-1]
