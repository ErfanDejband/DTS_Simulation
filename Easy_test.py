import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTextEdit,QTabWidget,QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from simulator import simulate, plot_experimental

class DTS_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DTS Simulation GUI')
        self.setGeometry(100, 100, 1000, 600)
        # Tabs
        self.tabs = QTabWidget()
        # Tab 1
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "Tab 1")
        self.initTab1()
        # Tab 2
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "Tab 2")
        self.initTab2()

        # # Tab 3
        # self.tab3 = QWidget()
        # self.tabs.addTab(self.tab3, "Tab 3")
        # self.initTab3()

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)
#####################################################
########## set tab 1 ################################
#####################################################
    def initTab1(self):
        self.setWindowTitle('DTS Simulation GUI')
        self.setGeometry(100, 100, 1000, 600)

        # Input fields for hot spots
        self.lbl_start_points_tab1 = QLabel('Start Points (comma-separated):')
        self.le_start_points_tab1 = QLineEdit()

        self.lbl_stop_points_tab1 = QLabel('Stop Points (comma-separated):')
        self.le_stop_points_tab1 = QLineEdit()

        self.lbl_hot_temps_tab1 = QLabel('Hot Temperatures (comma-separated):')
        self.le_hot_temps_tab1 = QLineEdit()

        # Input field for environmental temperature
        self.lbl_env_temp_tab1 = QLabel('Environmental Temperature:')
        self.le_env_temp_tab1 = QLineEdit()

        # Button to trigger simulation
        self.btn_simulate_tab1 = QPushButton('Simulate_1')
        self.btn_simulate_tab1.clicked.connect(self.simulate_dts_tab1)

        # Input layout
        input_layout_tab1 = QVBoxLayout()
        input_layout_tab1.addWidget(self.lbl_start_points_tab1)
        input_layout_tab1.addWidget(self.le_start_points_tab1)
        input_layout_tab1.addWidget(self.lbl_stop_points_tab1)
        input_layout_tab1.addWidget(self.le_stop_points_tab1)
        input_layout_tab1.addWidget(self.lbl_hot_temps_tab1)
        input_layout_tab1.addWidget(self.le_hot_temps_tab1)
        input_layout_tab1.addWidget(self.lbl_env_temp_tab1) 
        input_layout_tab1.addWidget(self.le_env_temp_tab1) 
        input_layout_tab1.addWidget(self.btn_simulate_tab1)  

        # Message display area
        self.message_display_tab1 = QTextEdit()
        self.message_display_tab1.setReadOnly(True)

        # Main left panel layout
        left_panel_layout_tab1 = QVBoxLayout()
        left_panel_layout_tab1.addLayout(input_layout_tab1)
        left_panel_layout_tab1.addWidget(self.message_display_tab1)

        # Plot layout
        self.figure_tab1 = Figure()
        self.canvas_tab1 = FigureCanvas(self.figure_tab1)
        self.toolbar_tab1 = NavigationToolbar(self.canvas_tab1, self)
        plot_layout_tab1 = QVBoxLayout()
        plot_layout_tab1.addWidget(self.toolbar_tab1)
        plot_layout_tab1.addWidget(self.canvas_tab1)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_panel_layout_tab1)
        main_layout.addLayout(plot_layout_tab1)
        self.tab1.setLayout(main_layout)

#####################################################
########## set tab 2 ################################
#####################################################

    def initTab2(self):
        self.setWindowTitle('DTS Simulation GUI')
        self.setGeometry(100, 100, 1000, 600)

        # Input fields for hot spots
        self.lbl_start_points_tab2 = QLabel('Hotspot Start Points (comma-separated):')
        self.le_start_points_tab2 = QLineEdit()

        self.lbl_stop_points_tab2 = QLabel('Hotspot Stop Points (comma-separated):')
        self.le_stop_points_tab2 = QLineEdit()

        self.lbl_hot_temps_tab2 = QLabel('Hotspot Temperatures (comma-separated):')
        self.le_hot_temps_tab2 = QLineEdit()

        # Input field for environmental temperature
        self.lbl_env_temp_tab2 = QLabel('Environmental Temperature:')
        self.le_env_temp_tab2 = QLineEdit()

        # Input fields for 30m section
        self.lbl_start_30m_section = QLabel('Start of 30m Section:')
        self.le_start_30m_section = QLineEdit()

        self.lbl_stop_30m_section = QLabel('Stop of 30m Section:')
        self.le_stop_30m_section = QLineEdit()

        # Buttons
        self.btn_simulate_tab2 = QPushButton('Simulate DTS')
        self.btn_simulate_tab2.clicked.connect(self.simulate_dts_tab2)

        self.btn_plot_experiment = QPushButton('Plot Experiment')
        self.btn_plot_experiment.clicked.connect(self.plot_experiment_data)

        #CSV file
        self.lbl_csv_file = QLabel('CSV File:')
        self.btn_browse_csv = QPushButton('Browse')
        self.btn_browse_csv.clicked.connect(self.browse_csv_file)
        self.le_csv_file = QLineEdit()


        # Input layout
        input_layout_tab2 = QVBoxLayout()
        input_layout_tab2.addWidget(self.lbl_start_points_tab2)
        input_layout_tab2.addWidget(self.le_start_points_tab2)

        input_layout_tab2.addWidget(self.lbl_stop_points_tab2)
        input_layout_tab2.addWidget(self.le_stop_points_tab2)

        input_layout_tab2.addWidget(self.lbl_hot_temps_tab2)
        input_layout_tab2.addWidget(self.le_hot_temps_tab2)

        input_layout_tab2.addWidget(self.lbl_start_30m_section)
        input_layout_tab2.addWidget(self.le_start_30m_section)

        input_layout_tab2.addWidget(self.lbl_stop_30m_section)
        input_layout_tab2.addWidget(self.le_stop_30m_section)

        input_layout_tab2.addWidget(self.btn_simulate_tab2)
        input_layout_tab2.addWidget(self.btn_plot_experiment)

        input_layout_tab2.addWidget(self.lbl_env_temp_tab2)
        input_layout_tab2.addWidget(self.le_env_temp_tab2)

        input_layout_tab2.addWidget(self.lbl_csv_file)  # Add CSV file widgets
        input_layout_tab2.addWidget(self.le_csv_file)
        input_layout_tab2.addWidget(self.btn_browse_csv)


        # Message display area
        self.message_display_tab2 = QTextEdit()
        self.message_display_tab2.setReadOnly(True)

        # Main left panel layout
        left_panel_layout_tab2 = QVBoxLayout()
        left_panel_layout_tab2.addLayout(input_layout_tab2)
        left_panel_layout_tab2.addWidget(self.message_display_tab2)

        # Plot layout
        self.figure_tab2 = Figure()
        self.canvas_tab2 = FigureCanvas(self.figure_tab2)
        self.toolbar_tab2 = NavigationToolbar(self.canvas_tab2, self)
        plot_layout_tab2 = QVBoxLayout()
        plot_layout_tab2.addWidget(self.toolbar_tab2)
        plot_layout_tab2.addWidget(self.canvas_tab2)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_panel_layout_tab2)
        main_layout.addLayout(plot_layout_tab2)
        self.tab2.setLayout(main_layout)

#####################################################
########## set tab 3 ################################
#####################################################

    # def initTab3(self):
    #     self.setWindowTitle('DTS Simulation GUI')
    #     self.setGeometry(100, 100, 1000, 600)

    #     # Input fields for hot spots
    #     self.lbl_start_points = QLabel('3333:')
    #     self.le_start_points = QLineEdit()

    #     self.lbl_stop_points = QLabel('333 Points (comma-separated):')
    #     self.le_stop_points = QLineEdit()

    #     self.lbl_hot_temps = QLabel('Hot erwer (comma-separated):')
    #     self.le_hot_temps = QLineEdit()

    #     # Input field for environmental temperature
    #     self.lbl_env_temp = QLabel('33 Temperature:')
    #     self.le_env_temp = QLineEdit()

    #     # Button to trigger simulation
    #     self.btn_simulate = QPushButton('Simulate')
    #     self.btn_simulate.clicked.connect(self.simulate_dts)

    #     # Input layout
    #     input_layout = QVBoxLayout()
    #     input_layout.addWidget(self.lbl_start_points)
    #     input_layout.addWidget(self.le_start_points)
    #     input_layout.addWidget(self.lbl_stop_points)
    #     input_layout.addWidget(self.le_stop_points)
    #     input_layout.addWidget(self.lbl_hot_temps)
    #     input_layout.addWidget(self.le_hot_temps)
    #     input_layout.addWidget(self.lbl_env_temp) 
    #     input_layout.addWidget(self.le_env_temp) 
    #     input_layout.addWidget(self.btn_simulate)  

    #     # Message display area
    #     self.message_display = QTextEdit()
    #     self.message_display.setReadOnly(True)

    #     # Main left panel layout
    #     left_panel_layout = QVBoxLayout()
    #     left_panel_layout.addLayout(input_layout)
    #     left_panel_layout.addWidget(self.message_display)

    #     # Plot layout
    #     self.figure = Figure()
    #     self.canvas = FigureCanvas(self.figure)
    #     self.toolbar = NavigationToolbar(self.canvas, self)
    #     plot_layout = QVBoxLayout()
    #     plot_layout.addWidget(self.toolbar)
    #     plot_layout.addWidget(self.canvas)

    #     # Main layout
    #     main_layout = QHBoxLayout()
    #     main_layout.addLayout(left_panel_layout)
    #     main_layout.addLayout(plot_layout)
    #     self.tab3.setLayout(main_layout)

#####################################################
########## simulate_dts_tab1 ########################
#####################################################

    def simulate_dts_tab1(self):
        # Get user input for start points, stop points, and hot temperatures
        try:
            start_points = np.array([float(x.strip()) for x in self.le_start_points_tab1.text().split(',')])
            stop_points = np.array([float(x.strip()) for x in self.le_stop_points_tab1.text().split(',')])
            hot_temps = np.array([float(x.strip()) for x in self.le_hot_temps_tab1.text().split(',')])
            env_temp = float(self.le_env_temp_tab1.text())  # Retrieve environmental temperature
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter valid numeric values for start points, stop points, and hot temperatures.')
            return

        # Validate input lengths
        if len(start_points) != len(stop_points) or len(start_points) != len(hot_temps):
            QMessageBox.warning(self, 'Input Error', 'The number of start points, stop points, and hot temperatures must be the same.')
            return

        # Simulate DTS data
        distance_tab1, actual_T_tab1, DDTS_tab1 = simulate(start=0, stop=30, H_starts=start_points, H_stops=stop_points, H_temperatures=hot_temps, env_temp=env_temp)

        # Clear previous plot
        self.figure_tab1.clear()

        # Plot DTS simulation results
        ax_tab1 = self.figure_tab1.add_subplot(111)
        ax_tab1.plot(distance_tab1, actual_T_tab1, label='Actual Temperature', color='orange')
        ax_tab1.plot(distance_tab1, DDTS_tab1, label='DDT_Simulate', color='green')

        # Finalize plot
        ax_tab1.set_xlabel('Distance')
        ax_tab1.set_ylabel('Temperature')
        ax_tab1.set_title('Actual Temperature vs DDT_simulation vs DTS')
        ax_tab1.legend()
        ax_tab1.grid(True)
        self.canvas_tab1.draw()

        # Display success message
        self.message_display_tab1.clear()
        self.message_display_tab1.append(f'Simulation for {len(start_points)} Hotspot successful!')

    def simulate_dts_tab2(self):
        # Get user input for start points, stop points, and hot temperatures
        try:
            start_points = np.array([float(x.strip()) for x in self.le_start_points_tab2.text().split(',')])
            stop_points = np.array([float(x.strip()) for x in self.le_stop_points_tab2.text().split(',')])
            hot_temps = np.array([float(x.strip()) for x in self.le_hot_temps_tab2.text().split(',')])
            env_temp = float(self.le_env_temp_tab2.text())  # Retrieve environmental temperature
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter valid numeric values for start points, stop points, and hot temperatures.')
            return

        # Validate input lengths
        if len(start_points) != len(stop_points) or len(start_points) != len(hot_temps):
            QMessageBox.warning(self, 'Input Error', 'The number of start points, stop points, and hot temperatures must be the same.')
            return

        # Simulate DTS data
        distance_tab2, actual_T_tab2, DDTS_tab2 = simulate(start=0, stop=30, H_starts=start_points, H_stops=stop_points, H_temperatures=hot_temps, env_temp=env_temp)

        # Clear previous plot
        self.figure_tab2.clear()

        # Plot DTS simulation results
        ax = self.figure_tab2.add_subplot(111)
        ax.plot(distance_tab2, actual_T_tab2, label='Actual Temperature', color='orange')
        ax.plot(distance_tab2, DDTS_tab2, label='DDT_Simulate', color='green')

        # Finalize plot
        ax.set_xlabel('Distance')
        ax.set_ylabel('Temperature')
        ax.set_title('Actual Temperature vs DDT_simulation vs DTS')
        ax.legend()
        ax.grid(True)
        self.canvas_tab2.draw()

        # Display success message
        self.message_display_tab2.clear()
        self.message_display_tab2.append(f'Simulation for {len(start_points)} Hotspot successful!')
    
    def browse_csv_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)", options=options)
        if file_name:
            self.le_csv_file.setText(file_name)

    def plot_experiment_data(self):
                # Get user input for CSV file and 30m section parameters
        csv_file = self.le_csv_file.text()
        start_30m_section = float(self.le_start_30m_section.text())
        stop_30m_section = float(self.le_stop_30m_section.text())

        # Call compare_sim_with_experimental with user input
        num_data_points,distance_30m_section,temperature_30m_section = plot_experimental(csv_file, start_30m_section, stop_30m_section)

        # Plot experiment results
        # Clear previous plot
        self.figure_tab2.clear()
        ax_tab2 = self.figure_tab2.add_subplot(111)
        ax_tab2.plot(distance_30m_section, temperature_30m_section, label='Actual Temperature', color='orange')
        # ax_tab1.plot(distance_tab1, DDTS_tab1, label='DDT_Simulate', color='green')

        # Finalize plot
        ax_tab2.set_xlabel('Distance')
        ax_tab2.set_ylabel('Temperature')
        ax_tab2.set_title('Experimental data')
        ax_tab2.legend()
        ax_tab2.grid(True)
        self.canvas_tab2.draw()

        # Display success message
        self.message_display_tab2.clear()
        self.message_display_tab2.append(f'from {start_30m_section} to {stop_30m_section} section of experimental data ploted')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DTS_GUI()
    window.show()
    sys.exit(app.exec_())
