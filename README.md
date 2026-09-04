# smart-weather-monitoring-app
Real-time weather analytics application integrating REST APIs with error handling, latency optimization, and network resilience

# Smart Weather Monitoring & Resilience Pipeline

A weather monitoring service built to demonstrate API consumption, network request-response lifecycle handling, and cloud architecture deployment.

## Key Features & Network Handling
- **Secure Endpoints:** Connects to external meteorological REST APIs strictly over HTTPS (Port 443).
- **Latency & Timeout Guard:** Configured 5-second socket timeouts to handle network degradation and packet drop.
- **Error Status Mapping:** Dedicated exception handling for `404 Not Found`, `401 Unauthorized`, DNS timeouts, and socket connection drops.
- **JSON Payload Parsing:** Efficient client-side extraction reducing in-memory overhead.

## Architecture Flow
`Client / CLI` ──(HTTPS GET)──> `External REST API` ──(JSON Payload)──> `Parser & Logging`

## Cloud Deployment Note
*Previously deployed on AWS leveraging serverless API routing. Cloud infrastructure was decommissioned post-testing to adhere to cloud cost-optimization and resource lifecycle management best practices.*

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/YashNagode123/smart-weather-monitoring-app.git](https://github.com/DevRushi-engg/smart-weather-monitoring-app.git)
   cd smart-weather-monitoring-app
2. Install dependencies:
   Bash
   pip install requests
   
3. Execute script:
   Bash
   python app.py
