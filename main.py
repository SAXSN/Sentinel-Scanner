import click
import asyncio
from sentinel_scanner.scanner import SentinelScanner
from sentinel_scanner.vulnerability import VulnerabilityScanner
from sentinel_scanner.reporting import ReportGenerator

@click.command()
@click.option('--targets', prompt='Target Hosts (comma separated)', help='Comma separated list of hosts to scan.')
@click.option('--report_type', default='html', type=click.Choice(['json', 'csv', 'html']), help='Report format.')
def scan(targets, report_type):
    hosts = targets.split(',')
    
    # Initialize Scanner, Vulnerability Checker, and Report Generator
    scanner = SentinelScanner()
    vulnerability_scanner = VulnerabilityScanner()
    report_generator = ReportGenerator()

    # Start scanning asynchronously
    loop = asyncio.get_event_loop()
    scan_results = loop.run_until_complete(scanner.scan_hosts(hosts))
    
    # Prepare the data for reporting
    data = []
    for host in scan_results:
        for service in host['services']:  # Each service contains details like port and service name
            version = service.get('version', '')
            vulnerability = vulnerability_scanner.check_cve(version)  # Check vulnerabilities if version info exists
            data.append({
                'host': host['host'],
                'port': service['port'],
                'service': service['service'],
                'vulnerability': vulnerability
            })

    # Generate the report based on the selected report type
    if report_type == 'json':
        report_generator.generate_json(data)
    elif report_type == 'csv':
        report_generator.generate_csv(data)
    elif report_type == 'html':
        report_generator.generate_html(data)

if __name__ == '__main__':
    scan()
