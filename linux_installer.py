import PyInstaller.__main__ as installer
import os
import sys


filepath = "troll/app/topack/Slightly_obnoxious_revision_aid.py"
iconDebug = sys.platform

if iconDebug != "linux":
    icontype = '-i obnoxious.ico, \n -n Slightly Obnoxious Revision Aid'
else:
    icontype = '-n Slightly Obnoxious Revision Aid'


installer.run([
    filepath,
    "--windowed",
    f"{icontype}"

])