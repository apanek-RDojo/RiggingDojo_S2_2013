import maya.cmds as cmds

def BuildJoints(prefix, lctrInfo):
	cmds.select(d=True)
	jntInfo = []
	for each in lctrInfo:
		jntName = each[0].replace('lctr', prefix)
		jnt = cmds.joint(name=jntName, p=each[1])
		jntInfo.append(jnt)

	return jntInfo

