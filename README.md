Smart Waste Management System

The Smart Waste Management System is an IoT-enabled project designed to address inefficiencies in traditional waste collection. It uses live-time sensor data, automated dry and wet waste segregation, and web-based monitoring to ensure effective waste disposal. This system helps reduce pollution, and promote a cleaner and more sustainable environment.
Features
•	Smart Detection: Uses ultrasonic sensors to detect object presence and bin fill levels.
•	Automatic Lid Operation: Servo motor opens/closes lid when user approaches.
•	Moisture-Based Waste Classification: Soil moisture sensor differentiates wet and dry waste.
•	Automated Sorting: Waste is directed into dry/wet compartments accordingly.
•	Web Dashboard: View bin fill levels and system status.
Installation Requirements
Software:
•	Arduino IDE – for programming the microcontroller
•	Web Development Stack: HTML, CSS, Flask (Python)
Hardware:
•	Arduino Uno – Microcontroller unit
•	Ultrasonic Sensors (HC-SR04) – Detects waste levels and object proximity
•	Soil Moisture Sensor – Identifies type of waste
•	Servo Motors – Controls lid and waste direction
•	Breadboard & Jumper Wires
 
Project Setup 
Arduino Setup:
•	Connect pins using jumper wires to ultrasonic sensors, servo motors, soil-moisture sensor, and Arduino uno as per the circuit below.

   
         
•	Upload the Arduino code via Arduino IDE.
•	Power the system by using a USB cable.
Web Dashboard Setup:
•	Set up the Flask backend to fetch and display sensor data from the serial reader, which is real-time live data.
•	Launch the HTML dashboard locally or on a hosted server.
Steps to run the project
1)	Take a dustbin, and make the connections as per the setup - connecting servo motors, ultrasonic sensors, soil moisture sensor using the jumper wires to the breadboard and Arduino.
2)	After the lid is opened by sensing an object/person in front it, place the waste on the soil moisture sensor, which will automatically detect if it’s wet/dry and segregate in it into the respective compartment.
3)	Parallelly, the web application dashboard keeps reading the real-time live data by using serial monitor and will display:
-	Object detection (green for detected, red for not detected)
-	Real-time Moisture levels
-	Waste type (dry or wet waste)
-	Level of fullness (both dry and wet wastes)
Usage
•	Place the bin in a public area.
•	When a user approaches, the lid opens automatically.
•	Waste is deposited and classified as dry/wet using a moisture sensor.
•	Sorted into the correct compartment.
•	Data is updated to the web dashboard which reflects the current status.  
Project Structure
SmartWasteManagement/
├── Arduino_Code/
│   └── " Arduino IDE"├
── WebApp/
│   ├── static/
│   │   └── styles.css
│   ├── templates/
│   │   └── dashboard.html
│   └── app.py (Flask server)
│   └── serial_read.py (Real-time data reader)
│   └── data.json (Last live data)
└── Documentation/
    └── SWMS_documentation.docx
Outputs
•	Bin Dashboard: Displays bin fill levels, type of waste - dry or wet waste, moisture levels, and detects object presence.
•	Live-Time Data Feed
•	System Interaction: Auto-classification and lid movement based on sensor inputs.

Authors
Amogha Sri Kommera - 23251A0568
Sirimalla Vyshnavi - 23251A0594
Sri Harshita Kemburu - 23251A0595

