from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog,QLabel,QHBoxLayout
from qgis.core import *
from qgis.gui import *
from qgis.core import Qgis
import os
import tempfile
import platform

class Map_Tool(QgsMapTool):
    def __init__(self, iface):
        QgsMapTool.__init__(self, iface.mapCanvas())
        self.canvas = iface.mapCanvas()
        #self.emitPoint = QgsMapToolEmitPoint(self.canvas)
        self.iface = iface
    def activate(self):
        QgsMapTool.activate(self)
        
    def deactivate(self):
        QgsMapTool.deactivate(self)
            
    def canvasReleaseEvent(self, event):
        point = self.toMapCoordinates(event.pos())
        point_layer = self.iface.mapCanvas().currentLayer()
        pr = point_layer.dataProvider()
        caps = point_layer.dataProvider().capabilities()
        if caps & QgsVectorDataProvider.AddFeatures:
           feat = QgsFeature(point_layer.fields())
           feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(point.x(), point.y())))
           pr.addFeature(feat)
           point_layer.updateExtents()
           point_layer.commitChanges()
           point_layer.triggerRepaint()
        else:
           self.iface.messageBar().pushMessage("Edit Layer", "Layer Is ReadOnly", level=Qgis.Warning)
