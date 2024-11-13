# Sentinel Scanner
Sentinel Scanner is an open-source vulnerability scanner that scans specified hosts for open ports, services, and known vulnerabilities. This tool aims to be more advanced than a simple network scanner, providing both vulnerability insights and customizable report generation.

# Table of Contents
Features
Installation
Usage
Report Formats
Project Structure
Contribution
License

# Features
Asynchronous Scanning: Scans multiple hosts in parallel to improve efficiency.
Service Detection: Identifies open ports, services, and service versions.
Vulnerability Detection: Checks for known vulnerabilities based on service version information.
Customizable Reporting: Generates JSON, CSV, and HTML reports for easy analysis and sharing.
Installation
Clone the Repository:
bash
Copy code
git clone https://github.com/yourusername/sentinel-scanner.git
cd sentinel-scanner
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Install Nmap: Ensure Nmap is installed on your system, as it is required by the scanner.

For Ubuntu/Debian:
bash
sudo apt-get install nmap
For MacOS:
bash
brew install nmap
For Windows: Download and install Nmap from nmap.org.
Usage
Use the command-line interface to scan hosts and generate reports.

bash
python main.py --targets <host1,host2,...> --report_type <json|csv|html>
Command Options
--targets: Comma-separated list of IPs or hostnames to scan.
--report_type: Format of the report (json, csv, or html). Default is html.
Example Usage
bash
python main.py --targets 192.168.1.1,192.168.1.2 --report_type json
This will scan the specified hosts and save the results in a JSON report format.

# Report Formats
Sentinel Scanner supports three report formats:
JSON: Provides a structured, machine-readable report.
CSV: Suitable for spreadsheet software or importing into databases.
HTML: Readable in a web browser with basic styling.
Reports are saved in the reports directory by default.

# Project Structure
main.py: Main script to run the scanner and generate reports.
sentinel_scanner/scanner.py: Contains the SentinelScanner class for scanning hosts.
sentinel_scanner/vulnerability.py: Implements VulnerabilityScanner, which checks for known vulnerabilities.
sentinel_scanner/reporting.py: Implements ReportGenerator to create JSON, CSV, and HTML reports.
Contribution
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
