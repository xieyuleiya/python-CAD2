#  ===================
#  @Time :2024/5/10
#  @by   :leilei
#  ===================

import comtypes.client

try:
    acad = comtypes.client.GetActiveObject('AutoCAD.Application', dynamic=True)
except WindowsError:
    acad = comtypes.client.CreateObject('AutoCAD.Application', dynamic=True)
    acad.Visible = True



import win32com.client as win32

wincad = win32.Dispatch("AutoCAD.Application")
doc = wincad.ActiveDocument
msp = doc.ModelSpace

doc.Utility.Prompt("Hello! Autocad from pywin32com.\n")

print(doc.Name)


