class Task:
    def __init__(self, description, completed = False):
        self.description = description
        self.completed = completed

    def __repr__(self):
        status = "[ ]"
        if self.completed:
            status = "[x]"
        return '{} {}'.format(status, self.description)

    def set_completed(self, status):
        self.completed = status
