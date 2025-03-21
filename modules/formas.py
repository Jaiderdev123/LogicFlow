from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem
from PySide6.QtGui import QBrush, QPen, QColor
from PySide6.QtCore import Qt, QRectF
import sys

# Clase personalizada para una forma de nodo (rectángulo)
class FlowchartNode(QGraphicsItem):
    def __init__(self, x, y, width=100, height=50, color=QColor("lightblue")):
        super().__init__()
        self.rect = QRectF(0, 0, width, height)  # Definir tamaño del nodo
        self.color = color
        self.setPos(x, y)  # Posición en la escena
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)  # Permitir mover y seleccionar

    def boundingRect(self):
        return self.rect  # Definir límites del objeto

    def paint(self, painter, option, widget=None):
        painter.setBrush(QBrush(self.color))  # Relleno
        painter.setPen(QPen(Qt.black, 2))  # Borde
        painter.drawRect(self.rect)  # Dibujar el rectángulo

# Clase principal con `QGraphicsView` y `QGraphicsScene`
class FlowchartApp(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setRenderHint(self.renderHints())

        # Agregar formas a la escena
        self.scene.addItem(FlowchartNode(50, 50))   # Nodo 1
        self.scene.addItem(FlowchartNode(200, 50))  # Nodo 2

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlowchartApp()
    window.show()
    sys.exit(app.exec())
