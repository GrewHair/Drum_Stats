from beyond.Reaper.Settings import *
import pandas as pd
import re
from itertools import product             #it might be corrupted

class AssociateTable:

    def __init__(self, kit_list, kit_dict):
        self.pc_trk_assoc = pd.DataFrame(columns=['piece', 'trk_index', 'trk_name'])
        self.tracks_list = list()

        self.fill_tracks_list()
        self.associate_trks(kit_list, kit_dict)


    def fill_tracks_list(self):
        with Reaper as r:
            trkcount = r.RPR_CountTracks(0)
            for i in range(0, trkcount):
                trk_name = r.RPR_GetSetMediaTrackInfo_String(r.RPR_GetTrack(0, i), "P_NAME", "", False)[3]
                self.tracks_list.append(trk_name)


    def associate_trks(self, kit_list, kit_dict):
        for piece in kit_list[2:12]:
            self.pc_trk_assoc = self.pc_trk_assoc.append({'piece': piece}, ignore_index=True)
            for trk_name, keyword in product(self.tracks_list, kit_dict[piece]):
                if re.search(keyword, trk_name, re.IGNORECASE):
                    self.pc_trk_assoc.at[len(self.pc_trk_assoc.index) - 1, 'trk_index'] = self.tracks_list.index(trk_name)
                    self.pc_trk_assoc.at[len(self.pc_trk_assoc.index) - 1, 'trk_name'] = trk_name
                    break


    def confirm_association(self):
        pass