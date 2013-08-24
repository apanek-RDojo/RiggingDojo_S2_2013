"""
Script: Hinge_Lyt
Author: Ryan Griffin  ryangrif@gmail.com
Description: Creates a hinge layout.
"""
import maya.cmds as cmds

CLASS_NAME = 'Hinge_Lyt2'
TITLE = 'Hinge_LYT2'
DESCRIPTION = 'Builds a hinge layout'

class Hinge_Lyt2:
	def __init__(self):
		print "In Hinge Lyt"
		self.hinge_lyt()


	def hinge_lyt(self):
	    positions = ([0.0, 5.0, 0.0], [0.0, 4.0, 0.0], [0.0, 2.0, 1.0], [0.0, 0.0, 0.0])
	    # Change this line so we have a root locator
	    locator_names = ('lctr_l_Root', 'lctr_l_arm1', 'lctr_l_arm2', 'lctr_l_wrist')
	    for index in range(len(locator_names)):   
	        lctr = cmds.spaceLocator(n=locator_names[index])
	        # Center the pivot of the locator
	        cmds.xform(lctr, cp=True)
	        # Use the xform command to position the locators.  This will give us actual ws coordinates.  
	        lctr = cmds.xform(lctr, t=positions[index])

	        # Parent the locators to form a hierachy, 
	        #but only if it isn't the first item as the root has no parent
	        print locator_names[index]
	        print locator_names[index-1]
	        if index != 0:
	            # Notice the use of locator_names[index-1].  The -1 performs
	            # a math function on the list to find the previous item.
	            cmds.parent(locator_names[index], locator_names[index-1])
	
