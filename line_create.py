from PyQt5.QtWidgets import QDialog,QLabel,QHBoxLayout
from qgis.gui import QgsMapTool,QgsRubberBand
from qgis.core import QgsVectorDataProvider,QgsFeature,QgsGeometry,QgsPointXY,QgsField,QgsWkbTypes
from qgis.utils import iface
from qgis.PyQt.QtCore import Qt,QVariant

class CoordTool(QgsMapTool):
    def __init__(self, iface):
        QgsMapTool.__init__(self, iface.mapCanvas())
        self.canvas = iface.mapCanvas()
        self.iface = iface
        self.status = 0
        self.rb = QgsRubberBand(self.canvas, QgsWkbTypes.LineGeometry)
        self.rb.setColor(QColor(255, 70, 0, 200))
        self.rb.setWidth(5)
        self.rb.setBrushStyle(Qt.NoBrush) 

    def canvasReleaseEvent(self, event):
        if event.button()==Qt.LeftButton:
            if self.status ==0:
                self.rb.reset(QgsWkbTypes.LineGeometry)
                self.status =1
            self.rb.addPoint(self.toMapcoorinates(event.pos()))
        else:
            if self.rb.numberOfVertices() > 1:
                self.status = 0
                current_layer = self.iface.mapCanvas().currentLayer()
                pr = current_layer.dataProvider()
                caps = current_layer.dataProvider().capabilities()
                if caps & QgsVectorDataProvider.AddFeatures:
                    feat = QgsFeature(current_layer.fields())
                    feat.setGeometry(self.rb.asGemoetry())
                    pr.addFeature(feat)
                    current_layer.updateExtents()
                    current_layer.commitChanges()
                    current_layer.triggerRepaint()

    def canvasMoveEvent(self,event):
        if self.rb.numberOfVertices() > 0 and self.status ==1:
            self.rb.removeLastPoint(0)
            self.rb.addPoint(self.toMapCoordinates(event.pos()))

        

canvas = iface.mapCanvas()
tool= CoordTool(canvas)
canvas.setMapTool(tool)