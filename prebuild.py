import os
import sys

rootdir = "./sources"
for root, subFolders, files in os.walk(rootdir):
	for file in files:
		fileName, fileExtension = os.path.splitext(file)
		if fileExtension == ".ui" :
			os.system("python \"PortablePython\App\lib\site-packages\PyQt4\uic\pyuic.py\" \"" + root + "/" + fileName + fileExtension + "\" -o \"" + root + "/" + fileName + "_ui.py\"")
