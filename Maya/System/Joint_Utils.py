import maya.cmds as cmds

def BuildJoints(prefix, lctrInfo):
	print lctrInfo
	cmds.select(d=True)
	for each in lctrInfo:
		jntName = each[0].replace('lctr', prefix)
		cmds.joint(name=jntName, p=each[1])