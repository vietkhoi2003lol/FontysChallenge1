# Challenge1 (Team C)
This repo contains code used for Arduino Calibration and Python Application.
### Instuctions to Setup and Run the Arduino Code ###

#### **Overview**
This Arduino sketch uses the LSM9DS1 sensor on the Arduino Nano 33 BLE to measure tilt angles (X, Y axes) and identify which side of the OCTO-Tracker prototype is facing upward. Output is displayed on the Serial Monitor.

---

#### **Setup Instructions**
1. **Hardware**:
   - Arduino Nano 33 BLE
   - USB cable for connection.

2. **Software**:
   - Install **Arduino IDE** 
   - Install the **Arduino_LSM9DS1** library via the Library Manager.

3. **Upload Code**:
   - Open the code in Arduino IDE.
   - Select **Arduino Nano 33 BLE** in **Tools > Board**.
   - Select the correct **Port**.
   - Click **Upload**.

4. **Run**:
   - Open **Serial Monitor** (baud rate: 9600).
   - Now flip the sides of OCTO-Tracker Prototype to get the coordinates and start/stop the study session.

---

### Instuctions to Setup and Run the OCTO-Tracker Application Code ###

---

#### **Overview**  
OCTO-Tracker Application is a Python-based application designed to help the cleint manage study sessions, track moods, and organize assignment deadlines effectively. It integrates with Arduino for real-time data capture.

---

#### **Requirements**
- Python 3.x installed on your system.
- Arduino connected to your computer (default port: `COM5`).
- Libraries:
  - `tkinter`
  - `tkcalendar`
  - `PIL`
  - `pyserial`

---

#### **Installation**

1. **Clone or Download the Repository**  
   Save the code file in your desired directory.

2. **Install Dependencies**  
   Open a terminal or command prompt and run:
   ```bash
   pip install tkinter tkcalendar PIL pyserial
   ```
   or
   Install the above libraries in your desired IDE.

---

#### **Setup Arduino**
- Connect your Arduino to the computer via USB.
- Ensure the COM port matches the one in the script (`COM5` by default).
- Adjust the port in the code if required:
  ```python
  arduino = serial.Serial('COM_PORT', 9600, timeout=10)
  ```

---

#### **Running the Application**
1. Navigate to the folder containing the code file.
2. Run the program.
3. If you are using terminal or command prompt:
   ```bash
   python <file_name>.py
   ```

---

#### **How to use the Application**
1. **Home Screen**: Navigate between `Study`, `Dashboard`, or `Assignment Deadlines`.  
2. **Study Session**:
   - Ensure the Arduino is connected.
   - Flip the tracker as per the instructions in the application to start or stop a study session.
3. **Mood Tracking**:
   - Rate your satisfaction after each session (1–7 scale).
3. **Task Completion**:
   - Select YES/NO based on your task completion status.

---

#### **Exiting Fullscreen**
Press `EXIT` to exit application.

---

#### **Troubleshooting**
- **Arduino Connection Issue**: Ensure the Arduino is connected and the COM port is correct.
- **Dependencies Missing**: Reinstall libraries using the commands provided.

