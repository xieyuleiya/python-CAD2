"""
by leilei

"""

import win32com.client

# 连接到AutoCAD应用程序
cad = win32com.client.Dispatch("AutoCAD.Application")

doc = cad.ActiveDocument

doc.Utility.Prompt("hello")

print(doc.Name)


