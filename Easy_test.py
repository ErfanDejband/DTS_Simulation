import sys
import numpy as np
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

        # Input fields for hot spots
        self.lbl_start_points = QLabel('Start Points (comma-separated):')
        self.le_start_points = QLineEdit()

        self.lbl_stop_points = QLabel('Stop Points (comma-separated):')
        self.le_stop_points = QLineEdit()

        self.lbl_hot_temps = QLabel('Hot Temperatures (comma-separated):')
        self.le_hot_temps = QLineEdit()

        # Input field for environmental temperature
        self.lbl_env_temp = QLabel('Environmental Temperature:')
        self.le_env_temp = QLineEdit()

        # Button to trigger simulation
        self.btn_simulate = QPushButton('Simulate')
        self.btn_simulate.clicked.connect(self.simulate_dts)

        # Input layout
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.lbl_start_points)
        input_layout.addWidget(self.le_start_points)
        input_layout.addWidget(self.lbl_stop_points)
        input_layout.addWidget(self.le_stop_points)
        input_layout.addWidget(self.lbl_hot_temps)
        input_layout.addWidget(self.le_hot_temps)
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
        # Get user input for start points, stop points, and hot temperatures
        try:
            start_points = np.array([float(x.strip()) for x in self.le_start_points.text().split(',')])
            stop_points = np.array([float(x.strip()) for x in self.le_stop_points.text().split(',')])
            hot_temps = np.array([float(x.strip()) for x in self.le_hot_temps.text().split(',')])
            env_temp = float(self.le_env_temp.text())  # Retrieve environmental temperature
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter valid numeric values for start points, stop points, and hot temperatures.')
            return

        # Validate input lengths
        if len(start_points) != len(stop_points) or len(start_points) != len(hot_temps):
            QMessageBox.warning(self, 'Input Error', 'The number of start points, stop points, and hot temperatures must be the same.')
            return

        # Simulate DTS data
        distance, actual_T, DDTS = simulate(start=0, stop=30, H_starts=start_points, H_stops=stop_points, H_temperatures=hot_temps, env_temp=env_temp)

        # Clear previous plot
        self.figure.clear()

        # Plot DTS simulation results
        ax = self.figure.add_subplot(111)
        ax.plot(distance, actual_T, label='Actual Temperature', color='orange')
        ax.plot(distance, DDTS, label='DDT_Simulate', color='green')

        # Finalize plot
        ax.set_xlabel('Distance')
        ax.set_ylabel('Temperature')
        ax.set_title('Actual Temperature vs DDT_simulation vs DTS')
        ax.legend()
        ax.grid(True)
        self.canvas.draw()

        # Display success message
        self.message_display.clear()
        self.message_display.append(f'Simulation for {len(start_points)} Hotspot successful!')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DTS_GUI()
    window.show()
    sys.exit(app.exec_())
