import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTextEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from simulator import simulate

class DTS_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DTS Simulation GUI')
        self.setGeometry(100, 100, 1000, 600)

        # Input fields
        self.lbl_H_start = QLabel('H Start:')
        self.le_H_start = QLineEdit()

        self.lbl_H_stop = QLabel('H Stop:')
        self.le_H_stop = QLineEdit()

        self.lbl_H_temperature = QLabel('H Temperature:')
        self.le_H_temperature = QLineEdit()

        self.lbl_env_temp = QLabel('Environment Temperature:')
        self.le_env_temp = QLineEdit()

        self.btn_simulate = QPushButton('Simulate')
        self.btn_simulate.clicked.connect(self.simulate_dts)

        # Input layout
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.lbl_H_start)
        input_layout.addWidget(self.le_H_start)
        input_layout.addWidget(self.lbl_H_stop)
        input_layout.addWidget(self.le_H_stop)
        input_layout.addWidget(self.lbl_H_temperature)
        input_layout.addWidget(self.le_H_temperature)
        input_layout.addWidget(self.lbl_env_temp)
        input_layout.addWidget(self.le_env_temp)
        input_layout.addWidget(self.btn_simulate)

        # Message display area
        self.message_display = QTextEdit()
        self.message_display.setReadOnly(True)

        # Main left panel layout
        left_panel_layout = QVBoxLayout()
        left_panel_layout.addLayout(input_layout)
        left_panel_layout.addWidget(self.message_display)

        # Plot layout
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        plot_layout = QVBoxLayout()
        plot_layout.addWidget(self.toolbar)
        plot_layout.addWidget(self.canvas)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_panel_layout)
        main_layout.addLayout(plot_layout)

        self.setLayout(main_layout)

    def simulate_dts(self):
        # Get user inputs
        try:
            H_start = float(self.le_H_start.text())
            H_stop = float(self.le_H_stop.text())
            H_temperature = float(self.le_H_temperature.text())
            env_temp = float(self.le_env_temp.text())
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter valid numeric values for all parameters.')
            return

        # Perform DTS simulation
        distance, actual_T, DDTS = simulate(H_start=H_start, H_stop=H_stop, H_temperature=H_temperature, env_temp=env_temp)

        # Update message display
        self.message_display.setText('Simulation successful!')

        # Clear previous plot
        self.figure.clear()

        # Create a new plot
        ax = self.figure.add_subplot(111)
        ax.plot(distance, actual_T, label='Actual Temperature')
        ax.plot(distance, DDTS, label='DDTS')
        ax.set_xlabel('Distance')
        ax.set_ylabel('Temperature')
        ax.set_title('Actual Temperature vs DDT_simulation')
        ax.legend()
        ax.grid(True)

        # Refresh canvas
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DTS_GUI()
    window.show()
    sys.exit(app.exec_())
