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
    
    scanner = SentinelScanner()
    vulnerability_scanner = VulnerabilityScanner()
    report_generator = ReportGenerator()

    # Start scanning asynchronously
    loop = asyncio.get_event_loop()
    scan_results = loop.run_until_complete(scanner.scan_hosts(hosts))
    
    data = []
    for host in scan_results:
        for port in host['services']:  # Iterate over open ports (services)
            service_info = scanner.scan_host(host['ip'])  # Get full service info for each port
            if service_info:
                # Check vulnerabilities for the service version
                version = service_info.get('version', '')
                vulnerability = vulnerability_scanner.check_cve(version)
                data.append({
                    'host': host['ip'],
                    'port': port,
                    'service': service_info['hostname'],  # or use service name if available
                    'vulnerability': vulnerability
                })

    # Generate the report based on the report type
    if report_type == 'json':
        report_generator.generate_json(data)
    elif report_type == 'csv':
        report_generator.generate_csv(data)
    elif report_type == 'html':
        report_generator.generate_html(data)

if __name__ == '__main__':
    scan()
