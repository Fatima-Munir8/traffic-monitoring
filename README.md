
# Traffic Monitoring System
A Python-based project that automates traffic violation detection by monitoring vehicle speeds, applying speed-limit rules, and generating violation summaries.
## Features
- Checks vehicle speeds according to vehicle type (car, bike, truck).
- Automatically ignores emergency vehicles.
- Classifies violations into warnings, fines, and heavy fines.
- Tracks violations separately for each vehicle type.
- Generates a summary of total violations.
- Identifies the vehicle ID with the highest number of recorded violations.
- Determines which vehicle type has the most violations.
## Speed Limits & Violation Rules

| Vehicle Type | Speed Limit | Warning | Fine | Heavy Fine |
|---|---:|---:|---:|---:|
| Car | 60 km/h | 61–70 | 71–80 | Above 80 |
| Bike | 50 km/h | 51–60 | 61–70 | Above 70 |
| Truck | 40 km/h | 41–50 | 51–60 | Above 60 |

## Technologies & Concepts
- **Language:** Python
- **Data Structures:** Lists, Dictionaries, Tuples
- **Concepts:** Functions, Loops, Conditional Statements, Data Processing
## Project Structure

```text
Traffic-Monitoring-System/
├── traffic.py
└── README.md
```
## How to Run
```bash
git clone <repository-url>
cd Traffic-Monitoring-System
python traffic.py
```
No external libraries are required.
