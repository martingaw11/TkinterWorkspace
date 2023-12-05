import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui

class GradientBarGraph(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a PlotWidget
        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)

        # Create value
        self.x = 1
        self.y = 1

        # Create Brush
        gradient = QtGui.QLinearGradient(0, 0, 0, 100)
        gradient.setColorAt(0.1 , pg.mkColor(162, 215, 216))
        gradient.setColorAt(0.25, pg.mkColor(191, 225, 191))
        gradient.setColorAt(0.4, pg.mkColor(237, 237, 234))
        gradient.setColorAt(0.55, pg.mkColor(252, 208, 89))
        gradient.setColorAt(0.85, pg.mkColor(222, 88, 66))
        gradientBrush = QtGui.QBrush(gradient)

        # Create a BarWidget
        self.bar_widget = pg.BarGraphItem(x=self.x, height=self.y, width=0.2, brush=gradientBrush)

        # Add BarWidget to PlotWidget
        self.plot_widget.addItem(self.bar_widget)

        # Set axis labels
        self.plot_widget.setLabel('left', 'Y-axis')
        self.plot_widget.setLabel('bottom', 'X-axis')

        # Set the title of the plot
        self.plot_widget.setTitle('Basic PyQtGraph Example')

        self.plot_widget.setYRange(0, 100)
        self.plot_widget.setXRange(0, 2)
        self.plot_widget.setFixedSize(400, 800)

        # Create a timer to update the plot every 100 milliseconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_bar_height)
        self.timer.start(100)

    def update_bar_height(self):
        # Update the height of the BarGraphItem
        self.y *= 1.10

        self.bar_widget.setOpts(height=self.y)
        # Update the data of the BarGraphItem
        # self.bar_widget.setData(x=[self.x], height=[self.y])

def main():
    app = QApplication(sys.argv)
    window = GradientBarGraph()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
