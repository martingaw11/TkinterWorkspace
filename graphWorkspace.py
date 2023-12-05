import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg

class BasicGraphApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a PlotWidget
        self.plot_widget = pg.PlotWidget()
        self.setCentralWidget(self.plot_widget)

        # Generate some example data
        x = list(range(-100, 100))
        y = [val ** 2 for val in x]

        # Plot the data
        self.plot_widget.plot(x, y, pen='b', name='Quadratic')

        # Set axis labels
        self.plot_widget.setLabel('left', 'Y-axis')
        self.plot_widget.setLabel('bottom', 'X-axis')

        # Set the title of the plot
        self.plot_widget.setTitle('Basic PyQtGraph Example')

def main():
    app = QApplication(sys.argv)
    window = BasicGraphApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
