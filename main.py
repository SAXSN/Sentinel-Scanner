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
    async def perform_scan():
        return await scanner.scan_hosts(hosts)

    loop = asyncio.get_event_loop()
    scan_results = loop.run_until_complete(perform_scan())
    
    # Prepare the data for reporting
    data = []
    for host in scan_results:
        for service in host['services']:
            vulnerability = vulnerability_scanner.check_cve(service['version'])  # Check for vulnerabilities
            data.append({
                'host': host['host'],  # Updated to match `SentinelScanner` output
                'port': service['port'],
                'protocol': service['protocol'],
                'service': service['service'],
                'version': service['version'],
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
