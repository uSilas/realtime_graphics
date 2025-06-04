import subprocess
import sys
import time

flask_cmd = [sys.executable, 'app.py']

streamlit_cmd = ['streamlit', 'run', 'visualizer.py']

flask_process = subprocess.Popen(flask_cmd)
print("Flask app started.")

time.sleep(2)

streamlit_process = subprocess.Popen(streamlit_cmd)
print("Streamlit app started.")

try:
    flask_process.wait()
    streamlit_process.wait()
except KeyboardInterrupt:
    print("⏹️ Shutting down...")

    flask_process.terminate()
    streamlit_process.terminate()

    flask_process.wait()
    streamlit_process.wait()

    print("Both apps stopped.")
