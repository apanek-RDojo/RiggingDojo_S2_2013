import maya.cmds as cmds
import Maya.Modules.Layout.Hinge_Lyt as Hinge_Lyt
reload (Hinge_Lyt)
import Maya.Modules.Animation.Rig_Arm as Rig_Arm
reload (Hinge_Lyt)
from functools import partial

class Rdojo_UI:

    def __init__(self):
        print "In Rdojo_UI"

        self.UI_Elements = {}

        self.windowName = "RdojoUI_Window"
        if cmds.window(self.windowName, exists=True):
            cmds.deleteUI(self.windowName)


        windowWidth = 80
        windowHeight = 40

        buttonWidth = 70
        buttonHeight = 33

        self.UI_Elements["window"] = cmds.window(self.windowName, width=windowWidth, height=windowHeight, title="RDojo_UI", sizeable=True)

        self.UI_Elements["buttonLyt"] = cmds.flowLayout(v=True, width=windowWidth, height=windowHeight)
        
        fileDirectory = 'R:/Maya/Modules/Layout/'
        for widget in self.returnWidgets(fileDirectory):
            print widget
            # http://docs.python.org/2/library/functions.html#__import__
            mod = __import__("Maya.Modules.Layout."+widget, {}, {}, [widget])  
            reload(mod) 
            title = mod.TITLE
            description = mod.DESCRIPTION
            classname = mod.CLASS_NAME 

            cmds.separator(p=self.UI_Elements["buttonLyt"])
            # http://stackoverflow.com/questions/15331726/how-does-the-functools-partial-work-in-python
            self.UI_Elements["module_button_" + widget] = cmds.button(label=title, width=buttonWidth, height=buttonHeight, p=self.UI_Elements['buttonLyt'], c=partial(self.installWidget, widget))
        

        self.UI_Elements["rigArmButton"] = cmds.button(label='Rig_Arm', width=buttonWidth, height=buttonHeight, p=self.UI_Elements['buttonLyt'], c=self.rigArm)

        cmds.showWindow(self.UI_Elements["window"])
   
    def installWidget(self, widget, *args):
        mod = __import__("Maya.Modules.Layout."+widget, {}, {}, [widget])
        reload(mod)
        widgetClass = getattr(mod, mod.CLASS_NAME)
        widgetInstance = widgetClass()

    def rigArm(self, *args):
        Rig_Arm.Rig_Arm()

    def returnWidgets(self, path, *args):
        import File_Utils as fileUtils
        reload(fileUtils)
        allPyFiles = fileUtils.findAllFiles(path, '.py')
        return allPyFiles
       