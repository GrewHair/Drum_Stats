import re
import json
from itertools import product
import os


class Kit(dict):
    def __init__(self, trList):
        super().__init__()
        self.read_kit()
        self.guess_trks(trList)

    def read_kit(self):
        module_dir = os.path.dirname(__file__)
        cfg_dir = os.path.join(module_dir, 'cfg/kit.json')
        with open(cfg_dir) as f:
            self.update(json.load(f))

    def guess_trks(self, trList):
        for piece in self.keys():
            self[piece]['track'] = None
            self[piece]['enabled'] = False
            for trk_name, srch_key in product(trList, self[piece]['srch_keys']):
                if re.search(srch_key, trk_name[1], re.IGNORECASE):
                    self[piece]['track'] = trk_name
                    self[piece]['enabled'] = True
                    break
