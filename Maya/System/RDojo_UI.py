import maya.cmds as cmds
import Maya.Modules.Layout.Hinge_Lyt as Hinge_Lyt
reload (Hinge_Lyt)
import Maya.Modules.Animation.Rig_Arm as Rig_Arm
reload (Hinge_Lyt)

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
        self.UI_Elements["hingeButton"] = cmds.button(label='Hinge_Lyt', width=buttonWidth, height=buttonHeight, p=self.UI_Elements['buttonLyt'], c=self.createHingeLyt)
        self.UI_Elements["rigArmButton"] = cmds.button(label='Rig_Arm', width=buttonWidth, height=buttonHeight, p=self.UI_Elements['buttonLyt'], c=self.rigArm)

        cmds.showWindow(self.UI_Elements["window"])
   
    def createHingeLyt(self, *args):
        Hinge_Lyt.Hinge_Lyt()
        print Hinge_Lyt.DESCRIPTION

    def rigArm(self, *args):
        Rig_Arm.Rig_Arm()
       