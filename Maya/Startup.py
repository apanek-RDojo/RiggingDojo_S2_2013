import maya.cmds as cmds


# Changing default preferences
cmds.currentUnit( time='ntsc' )

def createMenu():
	# Query the names of all "MayaWindows"
	mi = mc.window('MayaWindow', ma=True, q=True)
	 
	for m in mi:
		print m
		# If a name matches 'UserScripts', delete it
		if m == 'DojoTools':
			mc.deleteUI('DojoTools', m=True)
		# Create the 'UserScripts' menu. 
	mc.menu('DojoTools', label='DojoTools', to=True, p="MayaWindow")

	# Create a menu item for the RDojo UI
	mc.menuItem('DojoTools', label='RD_UI', c=createLytItem)


def createLytItem(*args):
	import Maya.System.RDojo_UI as RDojo_UI
	reload(RDojo_UI)
	RDojo_UI.Rdojo_UI()

	 
createMenu()