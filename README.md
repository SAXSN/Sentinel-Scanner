# Sentinel Scanner

**Sentinel Scanner** is an open-source vulnerability scanner that scans specified hosts for open ports, services, and known vulnerabilities. This tool aims to be more advanced than a simple network scanner, providing both vulnerability insights and customizable report generation.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Report Formats](#report-formats)
- [Project Structure](#project-structure)
- [Contribution](#contribution)
- [License](#license)

## Features

- **Asynchronous Scanning**: Scans multiple hosts in parallel to improve efficiency.
- **Service Detection**: Identifies open ports, services, and service versions.
- **Vulnerability Detection**: Checks for known vulnerabilities based on service version information.
- **Customizable Reporting**: Generates JSON, CSV, and HTML reports for easy analysis and sharing.
  
## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/sentinel-scanner.git
    cd sentinel-scanner
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Nmap**: Ensure Nmap is installed on your system, as it is required by the scanner.
    - For **Ubuntu/Debian**:
      ```bash
      sudo apt-get install nmap
      ```
    - For **MacOS**:
      ```bash
      brew install nmap
      ```
    - For **Windows**: Download and install Nmap from [nmap.org](https://nmap.org/download.html).

## Usage

Use the command-line interface to scan hosts and generate reports.

```bash
python main.py --targets <host1,host2,...> --report_type <json|csv|html>
