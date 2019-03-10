import wx


class GUI(wx.Frame):


    def __init__(self, parent, asstab):
        wx.Frame.__init__(self, parent, wx.ID_ANY, 'Confirm kit')  #calling parent's constructor

        self.chk, self.lbl, self.cmb, self.uninit = [], [], [], []

        self.InitUI(asstab)
        self.Centre()
        self.Show()


    def InitUI(self, asstab):

        panel = wx.Panel(self)
        sizer = wx.FlexGridSizer(len(asstab.pc_trk_assoc.loc[:, 'piece']) + 1, 3, 5, 5)

        for i in asstab.pc_trk_assoc.loc[:, 'piece'].index:

            self.chk.append(wx.CheckBox(parent=panel, id=i))
            self.lbl.append(wx.StaticText(parent=panel, id=wx.ID_ANY, label=asstab.pc_trk_assoc.loc[i, 'piece']))
            self.cmb.append(wx.ComboBox(parent=panel, id=i, choices=asstab.tracks_list, style=wx.CB_READONLY))
            self.uninit.append(False)

            self.chk[i].Bind(wx.EVT_CHECKBOX, self.Check)
            self.cmb[i].Bind(wx.EVT_COMBOBOX, self.ComboChoose)

            sizer.Add(self.chk[i], 0, wx.EXPAND)
            sizer.Add(self.lbl[i], 0, wx.EXPAND)
            sizer.Add(self.cmb[i], 0, wx.EXPAND)

            try:
                self.cmb[i].SetSelection(int(asstab.pc_trk_assoc.loc[i, 'trk_index']))
                self.chk[i].SetValue(True)
            except ValueError:                            # NaN from Pandas means no track was found for this kit peace
                self.chk[i].SetValue(False)
                self.lbl[i].Enable(False)
                self.cmb[i].Enable(False)
                self.uninit[i] = True

        confirm_assoc = wx.Button(parent=panel, id=wx.ID_ANY, label='Confirm association!')
        sizer.Add(confirm_assoc, 0, wx.EXPAND)
        panel.SetSizer(sizer)


    def Check(self, event):
        if self.uninit[event.GetId()]:
            self.chk[event.GetId()].SetValue(False)
            self.cmb[event.GetId()].Popup()
            return

        if event.GetEventObject().GetValue():
            self.lbl[event.GetId()].Enable(True)
            self.cmb[event.GetId()].Enable(True)
        else:
            self.lbl[event.GetId()].Enable(False)
            self.cmb[event.GetId()].Enable(False)
        return


    def ComboChoose(self, event):
        self.chk[event.GetId()].SetValue(True)
        self.lbl[event.GetId()].Enable(True)
        self.cmb[event.GetId()].Enable(True)
        self.uninit[event.GetId()] = False
