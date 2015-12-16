import commands as cmd

class MenuItem:
    def __init__(self, id, text, action = None, extra_arg = None):
        self.id = id
        self.text = text
        self.action = action
        self.extra_arg = extra_arg

    def __repr__(self):
        return '{} {}'.format(self.id, self.text)

class Menu:
    def __init__(self, items):
        self.items = items

    def display(self):
        print(self.get_menu())

    def get_menu(self):
        return "\n".join(str(item) for item in self.items)

    def select_item(self, choice, store):
        for item in self.items:
            if item.id == choice:
                if item.extra_arg == None:
                    return item.action(store)
                return item.action(store, item.extra_arg)
        return cmd.Result(success = False, text = '{} is wrong input'.format(choice))

    def ask_player(self):
        return input('Choose an option: ')
