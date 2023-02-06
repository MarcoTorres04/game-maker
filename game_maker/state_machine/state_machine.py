class StateMachine:
    def __init__(self):
        self.__states = []

    def push(self, state: str):
        self.__states.append(state)

    def pop(self) -> str:
        return self.__states.pop(len(self.__states) - 1)

    def view(self) -> str:
        if len(self.__states) == 0:
            return None
        return self.__states[-1]
