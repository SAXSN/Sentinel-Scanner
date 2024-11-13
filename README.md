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
```

## Report Formats

Sentinel Scanner supports three report formats:

1. **JSON**: Provides a structured, machine-readable report.
2. **CSV**: Suitable for spreadsheet software or importing into databases.
3. **HTML**: Readable in a web browser with basic styling.

Reports are saved in the `reports` directory by default.

## Project Structure

Project structure of Sentinel Scanner:

- **`main.py`**: Main script to run the scanner and generate reports.
- **`sentinel_scanner/scanner.py`**: Contains the `SentinelScanner` class for scanning hosts.
- **`sentinel_scanner/vulnerability.py`**: Implements `VulnerabilityScanner`, which checks for known vulnerabilities.
- **`sentinel_scanner/reporting.py`**: Implements `ReportGenerator` to create JSON, CSV, and HTML reports.

## Contribution

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

Steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](License) file for details.

