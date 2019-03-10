from beyond.Reaper.Settings import *


class TrList(list):
    def __init__(self):
        super().__init__()
        self.read_trlist()

    def read_trlist(self):
        with Reaper as r:
            trkcount = r.RPR_CountTracks(0)
            for i in range(0, trkcount):
                trk_name = r.RPR_GetSetMediaTrackInfo_String(r.RPR_GetTrack(0, i), "P_NAME", "", False)[3]
                self.append((i, trk_name))
