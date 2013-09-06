# Rig_Utils

import maya.cmds as cmds


def setupControlObject(path, attrs):
	print path
	print attrs
	cmds.file(path, i=True)

	controlObject = ('control')

def createIk(sj, ej):
	print 'In Create IK'
	cmds.ikHandle( sj=sj, ee=ej, p=2, w=.5 )