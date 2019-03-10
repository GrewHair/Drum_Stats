import sys
import json
import os


class NoteMap(tuple):
    def __new__(cls, kit):
        return super().__new__(cls, cls.read_file())

    def __init__(self, kit):
        super().__init__()                 # not sure if it should be there
        self.validate(kit)

    def read_file():
        module_dir = os.path.dirname(__file__)
        cfg_dir = os.path.join(module_dir, 'cfg/notemap.json')
        with open(cfg_dir) as f:
            return (json.load(f)).values()

    def validate(self, kit):
        for piece in self:
            if not piece in (list(kit.keys()) + ['forbid', 'ignore']):
                print('youve got a wrong map!')
                sys.exit(0)
