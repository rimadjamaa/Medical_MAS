from agno.memory.v2.memory import UserMemory

class DummyMemory(UserMemory):
    def __init__(self):
        self.history = []

    def set_model(self, model):
        self.model = model  # Pas de deepcopy ici

    def add(self, input=None, output=None, **kwargs):
        self.history.append((input, output))

    def get_memory(self):
        return self.history

    def clear(self):
        self.history = []
