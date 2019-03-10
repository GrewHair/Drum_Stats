from beyond.Reaper.Settings import *
import pandas as pd
import sys

class DrummingTable:

    def __init__(self, kit_list, allocate_list):

        self.allocate_list = allocate_list
        self.table = pd.DataFrame(columns=['time'] + kit_list[2:12])

    def fill_score(self):
        with Reaper as r:
            r.RPR_Main_OnCommand(40153, 0)                                                    # open MIDI editor
            take = r.RPR_MIDIEditor_GetTake(r.MIDIEditor_GetActive())
            notecnt = r.RPR_MIDI_CountEvts(take, 0, 0, 0)[2]
            for k in range(0, notecnt):
                ppq = r.RPR_MIDI_GetNote(take, k, 0, 0, 0, 0, 0, 0, 0)[5]
                note = r.RPR_MIDI_GetNote(take, k, 0, 0, 0, 0, 0, 0, 0)[8]
                if self.allocate_list[note] == 'forbid':
                    print('you have wrong notes!!')
                    sys.exit(0)
                if self.allocate_list[note] == 'ignore':
                    continue
                repeating = self.find_pos_of_rep(ppq)
                if repeating == None:
                    self.table = self.table.append({'time': ppq}, ignore_index=True)
                    self.table.at[len(self.table.index) - 1, self.allocate_list[note]] = 0
                else:
                    self.table.at[repeating, self.allocate_list[note]] = 0
            r.RPR_MIDIEditor_OnCommand(r.MIDIEditor_GetActive(), 2)                           # close MIDI editor

    def find_pos_of_rep(self, what):
        for i in self.table.loc[:, 'time'].index:
            if self.table.loc[i, 'time'] == what:
                return i
