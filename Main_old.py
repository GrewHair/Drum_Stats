import json
from DrummingTable_old import *
from AssociateTable_old import *
from GUI import *


#Reaper.OnConnectExecute = "from sws_python import *"


with open('notemap.json') as f:
    allocate_list = list((json.load(f)).values())

with open('kit_old.json') as f:
    kit_dict = json.load(f)
    kit_list = list(kit_dict.keys())
    for k in kit_list:                                                # convert "dict of dicts" into "dict of lists"
        kit_dict[k] = list(kit_dict[k].values())

drTable = DrummingTable(kit_list, allocate_list)
drTable.fill_score()
print(drTable.table)

assTable = AssociateTable(kit_list, kit_dict)
print(assTable.pc_trk_assoc)
print(assTable.tracks_list)

# bpm = r.RPR_TimeMap2_GetDividedBpmAtTime(0, 0)

app = wx.App()
frame = GUI(parent=None, asstab=assTable)
app.MainLoop()

print('attention!!')
print(type(kit_dict['hihat']))


