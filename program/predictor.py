# predictor.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.animation as animation
import pandas as pd
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings("ignore")

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

        self.df['Numeric_Percentage'] = self.df['Percentage'].apply(lambda x: float(x.strip('%').replace('+', '')))

        # Matplotlib figure
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        self.setCentralWidget(QWidget(self))
        layout = QVBoxLayout(self.centralWidget())
        layout.addWidget(self.canvas)
        self.prediction_label = QLabel(self)
        layout.addWidget(self.prediction_label)
        self.info_label = QLabel(self)
        layout.addWidget(self.info_label)

        self.prediction_interval = 3

        # Real-time prediction function
        self.ani = animation.FuncAnimation(self.fig, self.update_plot, blit=False, cache_frame_data=False)

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
        current_date = datetime.now()

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

        # Create new data
        new_data = pd.DataFrame({'Date': [current_date], 'Percentage': [new_percentage]})
        new_data['Price_Rise'] = new_data['Percentage'].apply(lambda x: float(x.strip('%').replace('+', '')))

        # Add new data to the existing data
        self.df = pd.concat([self.df, new_data], ignore_index=True)

        # Check if new_data is not empty and does not have all NA values
        if not new_data.empty and not new_data.isna().all().all():
            # Check if 'Numeric_Percentage' column exists, create it if not
            if 'Numeric_Percentage' not in self.df.columns:
                self.df['Numeric_Percentage'] = self.df['Percentage'].apply(lambda x: float(x.strip('%').replace('+', '')))

            # Build ARIMA model
            p, d, q = 3,1,3  # Replace with appropriate ARIMA parameters
            model = ARIMA(self.df['Numeric_Percentage'].dropna(), order=(p, d, q))
            fit_model = model.fit()

            # Perform prediction
            forecast = fit_model.forecast(steps=1)

            # Update the graph with actual Percentage values and predictions
            self.ax.clear()
            self.df['Numeric_Percentage'] = self.df['Percentage'].apply(lambda x: float(x.strip('%').replace('+', '')))
            self.ax.plot(self.df['Date'], self.df['Numeric_Percentage'], label='actual')

            # Plot the current date
            self.ax.axvline(current_date, color='blue', linestyle='--', label='current')

            # Plot the forecasted date (current date + prediction_interval)
            forecasted_date = current_date + timedelta(seconds=self.prediction_interval)
            self.ax.axvline(forecasted_date, color='green', linestyle='--', label='3s later')

            self.ax.scatter(forecasted_date, forecast, color='red', label='predict')

            self.ax.legend()
            self.ax.set_title('Crypto growth rate Predictor')
            self.info_label.setText(f'Current growth rate: {self.df["Numeric_Percentage"].iloc[-1]:.2f}')

            # Check if forecast value is greater or smaller than the current growth rate
            # Check if forecast value is greater or smaller than the current growth rate
            if forecast.iloc[0] > self.df["Numeric_Percentage"].iloc[-1]:
                # Display "Sell 3 sec later" if forecast is greater
                self.prediction_label.setText(f'<font color="red">3 sec later Prediction: {forecast.iloc[0]:.2f}</font>')
            else:
                # Remove "Sell 3 sec later" if forecast is smaller
                self.prediction_label.setText(f'3 sec later Prediction: {forecast.iloc[0]:.2f}')



def start_predictor():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Use Fusion style for a modern look

    # Apply global style sheet
    app.setStyleSheet("""
        QWidget {
            background-color: white;
        }
        """)

    predictor_app = CoinPredictorApp()
    predictor_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    start_predictor()
