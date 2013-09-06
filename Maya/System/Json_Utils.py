import maya.cmds as cmds
import json
import tempfile

def writeJson(fileName, data):

	with open(fileName, 'w') as outfile:
		json.dump(data, outfile)

	file.close(outfile)

def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data
	
	
	
jointInfo = ['hi', int(0)]	
sel = cmds.ls(sl=True, type='joint')
pos = cmds.xform(sel[0], q=True, ws=True, t=True)
jointInfo.append([sel[0], pos])
fileName = 'R:/Maya/Data/CharacterA_JointInfo.json'
writeJson(fileName, jointInfo)


data = readJson(fileName = 'R:/Maya/Data/CharacterA_JointInfo.json')
print data

print type(data[0])