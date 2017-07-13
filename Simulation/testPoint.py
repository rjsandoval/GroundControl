from kivy.uix.gridlayout                     import GridLayout
from kivy.properties                         import NumericProperty, ObjectProperty
from kinematics                              import Kinematics
from kivy.graphics                           import Color, Ellipse, Line

import math

class TestPoint(GridLayout):
    
    def initialize(self, targetCanvas, correctKinematics, distortedKinematics): 
        print "test point initialized"
        self.targetCanvas        = targetCanvas
        self.correctKinematics   = correctKinematics
        self.distortedKinematics = distortedKinematics
        
        
        self.plotPoint()
    
    def plotPoint(self):
        print "plotting point"
        radius = 5
        correctPosX   = 0
        correctPosY   = 0
        
        #take the position, translate it to chain lengths
        chainALength, chainBLength = self.correctKinematics.inverse(correctPosX, correctPosY)
        print chainALength
        print chainBLength
        
        #then back into XY coordinates using the correct kinematics
        correctPosX, correctPosY = self.correctKinematics.forward(chainALength, chainBLength)
        print "pos:"
        print correctPosX
        print correctPosY
        
        #then back into XY coordinateness using the distorted kinematics
        distortedPosX, distortedPosY = self.distortedKinematics.forward(chainALength, chainBLength)
        print "distorted Pos"
        print distortedPosX
        print distortedPosY
        
        with self.targetCanvas:
            Color(1, 1, 1)
            Line(circle=(correctPosX, correctPosY, radius))
            Color(1, 0, 0)
            Line(circle=(distortedPosX, distortedPosY, radius))