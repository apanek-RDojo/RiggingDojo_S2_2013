"""
Script: Rig_Arm
Author: Ryan Griffin  ryangrif@gmail.com
Description: Creates an arm rig.
"""
import maya.cmds as cmds
#import System.Joint_Utils as JointUtils

CLASS_NAME = 'Rig_Arm'
TITLE = 'Rig_Arm'
DESCRIPTION = 'Creates an arm rig'

class Rig_Arm:
	def __init__(self):
		lctrInfo =[]
		lctrs = cmds.ls(sl=True)
		for each in lctrs:
		    pos = cmds.xform(each, q=True, t=True)
		    lctrInfo.append([each, pos])
		    
		print lctrInfo

		print "In Rig Arm"
		fkJoints = JointUtils.BuildJoints('fkJoint_', lctrInfo)
		ikJoints = JointUtils.BuildJoints('ikJoint_', lctrInfo)