
# 🎮 Player Performance Visualization App

This project is a simple system that allows collecting and visualizing player performance data, such as **points** and **time without dying**. It uses **Flask** for data ingestion and **Streamlit** for interactive visualization.

---

## ✅ Features

- **Flask API** to receive player performance data via POST requests.
- **Streamlit dashboard** to visualize data with:
  - Line charts
  - Bar charts
  - Raw data table
- **CSV storage** for simple persistence.
- **Automatic graph updates** in near real-time.

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Streamlit
- Pandas
- Altair (for charts)

---

## 📂 Project Structure

```
├── app.py               # Flask backend to receive data
├── visualizer.py       # Streamlit frontend to visualize data
├── run_apps.py         # Script to launch Flask and Streamlit simultaneously
├── data.csv            # CSV file for data storage (auto-generated)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/player-visualization.git
cd player-visualization
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

**Example `requirements.txt`:**

```
flask
streamlit
pandas
altair
```

---

## 🏃 Running the Application

### ✅ Option 1: Run Flask and Streamlit separately

**Start Flask backend:**

```bash
python app.py
```

**In a new terminal, start Streamlit:**

```bash
streamlit run visualizer.py
```

---

### ✅ Option 2: Run both automatically

```bash
python run_apps.py
```

This will launch both Flask and Streamlit simultaneously.

---

## 📝 Sending Data

You can send data to the Flask endpoint using tools like **Postman**, **curl**, or via a Python script.

**Example with Python:**

```python
import requests

url = 'http://127.0.0.1:5000/submit'
data = {
    'points': 150,
    'time_without_dying': 45
}

response = requests.post(url, json=data)
print(response.json())
```

---

## 📊 Viewing Data

After sending data, visit the **Streamlit app** in your browser:

```
http://localhost:8501
```

You will see:

- Raw data table
- Line chart of `Points vs Time Without Dying`
- Bar charts for distributions

The dashboard automatically refreshes every 5 seconds to show the latest data.

---

## ⚙️ Configuration

- Data stored in `data.csv` in the project root.
- Flask listens on `http://127.0.0.1:5000`.
- Streamlit runs on `http://localhost:8501`.

You can change ports in the `app.py` and `streamlit run` command if needed.

---

## 🧹 Cleaning Up

To stop both Flask and Streamlit:

- If using `run_apps.py`: press `Ctrl + C`.
- If running separately: stop each terminal session with `Ctrl + C`.

---

## 🏆 Future Improvements

- Switch from CSV to a database (e.g., SQLite, PostgreSQL).
- Add authentication to the API.
- Use WebSockets for true real-time updates.
- Deploy using Docker.

---

## 📄 License

MIT License.

---

## 🙌 Acknowledgements

Thanks to the developers of Flask, Streamlit, Pandas, and Altair for these amazing tools!

---

## 💡 Contact

For questions or contributions, please open an issue or submit a pull request.
