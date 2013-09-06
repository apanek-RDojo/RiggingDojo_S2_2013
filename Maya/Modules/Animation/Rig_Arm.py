"""
Script: Rig_Arm
Author: Ryan Griffin  ryangrif@gmail.com
Description: Creates an arm rig.
"""
import maya.cmds as cmds
import Maya.System.Joint_Utils as JointUtils
reload(JointUtils)

CLASS_NAME = 'Rig_Arm'
TITLE = 'Rig_Arm'
DESCRIPTION = 'Creates an arm rig'

class Rig_Arm:
	def __init__(self):
		lctrInfo = []
		rootLctr = cmds.ls(sl=True)
		tmpString = rootLctr[0].rpartition('_')[2]

		if tmpString == 'Root':
			print "Root Selected"
			rootChildren = cmds.listRelatives(rootLctr, ad=True, type='transform')
			
			for each in rootChildren:
			    pos = cmds.xform(each, q=True, ws=True, t=True)
			    lctrInfo.append([each, pos])
			lctrInfo.reverse()    
			
			rootPos = cmds.xform(rootLctr, q=True, ws=True, t=True)
			lctrInfo.insert(0, [rootLctr[0], rootPos])
			print lctrInfo
			self.rigArm(lctrInfo)

		else:
			return cmds.headsUpMessage('Please Select A Root')


	def rigArm(self, lctrInfo):
		print "In Rig Arm"	
		lctrInfo.remove(lctrInfo[0])		
		fkJoints = JointUtils.BuildJoints('fkJoint_', lctrInfo)
		ikJoints = JointUtils.BuildJoints('ikJoint_', lctrInfo)
		# Build Rig Joint_Utils
		# Create ik from arm1 to wrist
		# Build an ik control
		import Maya.System.Rig_Utils as Rig_Utils
		reload (Rig_Utils)
		path = 'R:/Maya/Modules/Animation/Controls/SphereControl.ma'
		attr = ('ik/fk')
		Rig_Utils.setupControlObject(path, attr)

		Rig_Utils.createIk(ikJoints[0], ikJoints[2])
		# Parent ikHandle to ik arm control
		# PV control
		# Connect rig joints to fk and ik joints
		# Create fk controls.