from model.trlist import TrList
from model.kit import Kit
from model.notemap import NoteMap


class Model:
    def __init__(self):
        self.trList = TrList()
        self.kit = Kit(self.trList)
        self.noteMap = NoteMap(self.kit)
        self.timeline = []


if __name__ == "__main__":
    model = Model()
    print(model.kit)
    print(model.noteMap)
    print(model.trList)