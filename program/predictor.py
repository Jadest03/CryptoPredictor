# predictor.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta

class CoinPredictorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the initial data
        self.df = pd.read_csv('coin.csv')

        # Feature engineering
        self.df['Price_Rise'] = self.df['Percentage'].apply(lambda x: float(x.strip('%').replace('+', '')))

        # Feature and target data preparation
        self.X = self.df[['Price_Rise']]
        self.y = self.df['Price_Rise']

        # Matplotlib figure
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        self.setCentralWidget(QWidget(self))
        layout = QVBoxLayout(self.centralWidget())
        layout.addWidget(self.canvas)

        # Real-time prediction function
        self.ani = animation.FuncAnimation(self.fig, self.update_plot, blit=False)

        self.setWindowTitle("Coin Predictor")
        self.setGeometry(100, 100, 800, 600)

        # Apply style sheet for a more polished look
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                color: #333;
                font-size: 14px;
            }
        """)

    def update_plot(self, frame):
        df = pd.read_csv('coin.csv')

        # Current date and time plus 1 second
        current_date = datetime.now() + timedelta(seconds=1)

        # Get the new Percentage value from coin.csv
        new_percentage = df['Percentage'].iloc[-1]

        # Extract the numeric value without the percentage sign and handle potential errors
        try:
            new_percentage_numeric = float(new_percentage.strip('%').replace('+', ''))
        except ValueError:
            # If conversion to float fails, set it to NaN
            new_percentage_numeric = float('nan')

        # Feature Scaling (Normalization)
        scaler = MinMaxScaler()
        X_scaled = scaler.fit_transform(self.X)

        # Machine Learning model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_scaled, self.y)

        # Create new data
        new_data = pd.DataFrame({'Date': [current_date], 'Percentage': [new_percentage]})
        new_data['Price_Rise'] = new_data['Percentage'].apply(lambda x: float(x.strip('%').replace('+', '')))

        # Add new data to the existing data
        self.df = pd.concat([self.df, new_data], ignore_index=True)

        # Check if new_data is not empty and does not have all NA values
        if not new_data.empty and not new_data.isna().all().all():
            # Perform prediction
            X_new = new_data[['Price_Rise']]  # Use only the latest data point for prediction
            X_new_scaled = scaler.transform(X_new)
            prediction = model.predict(X_new_scaled)

            # Update the graph with actual Percentage values and predictions
            self.ax.clear()
            # Extract numeric values without percentage signs for plotting
            self.df['Numeric_Percentage'] = self.df['Percentage'].apply(lambda x: float(x.strip('%').replace('+', '')))
            self.ax.plot(self.df['Date'], self.df['Numeric_Percentage'], label='actual')  # Plot actual numeric values
            self.ax.scatter(current_date, prediction, color='red', label='predict')  # Mark the prediction
            self.ax.legend()
            self.ax.set_title('Crypto growth rate Predictor')

def start_predictor():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Use Fusion style for a modern look

    # Apply global style sheet
    app.setStyleSheet("""
        QWidget {
            background-color: #f0f0f0;
        }
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 8px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        """)

    predictor_app = CoinPredictorApp()
    predictor_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    start_predictor()










