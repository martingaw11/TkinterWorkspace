import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui

class LiveUpdateGraphApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a PlotWidget
        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)

        # Initialize example data
        self.x = list(range(100))
        self.y = [val ** 2 for val in self.x]

        # Make gradient brush
        gradient = QtGui.QLinearGradient(0, 0, 0, 10000)
        gradient.setColorAt(0.3, pg.mkColor(20, 70, 159))
        gradient.setColorAt(0.9, pg.mkColor(218, 48, 104))
        gradientBrush = QtGui.QBrush(gradient)

        # Plot the initial data
        self.plot = self.plot_widget.plot(self.x, self.y, pen='b', name='Quadratic', fillLevel=0, fillBrush=gradientBrush)
        self.plot.setFillBrush(gradientBrush)

        # Set axis labels
        self.plot_widget.setLabel('left', 'Y-axis')
        self.plot_widget.setLabel('bottom', 'X-axis')

        # Set the title of the plot
        self.plot_widget.setTitle('Live Update PyQtGraph Example')

        # Create a timer to update the plot every 100 milliseconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(100)

    def update_data(self):
        # Update the data (in this example, a simple quadratic function)
        self.x = list(range(len(self.x) + 1))
        self.y.append(self.x[-1] ** 2)

        # Trim data to keep a fixed number of points (optional)
        max_points = 100
        if len(self.x) > max_points:
            self.x = self.x[-max_points:]
            self.y = self.y[-max_points:]

        # Update the plot with the new data
        self.plot.setData(self.x, self.y)

def main():
    app = QApplication(sys.argv)
    window = LiveUpdateGraphApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
