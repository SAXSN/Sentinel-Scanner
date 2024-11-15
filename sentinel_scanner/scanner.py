import nmap
import asyncio

class SentinelScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def scan_host(self, host: str):
        """
        Scans a single host and retrieves services, including their versions.
        """
        try:
            print(f"Scanning host: {host}")
            # Perform a SYN scan with service version detection
            self.nm.scan(host, arguments='-sS -sV')

            # Check if the host was scanned
            if host not in self.nm.all_hosts():
                print(f"No data found for host: {host}")
                return None

            host_info = self.nm[host]
            services = []

            # Iterate over all protocols and retrieve port and service details
            for proto in host_info.all_protocols():
                ports = host_info[proto].keys()
                for port in ports:
                    service_data = {
                        'port': port,
                        'protocol': proto,
                        'service': host_info[proto][port].get('name', 'Unknown'),
                        'version': host_info[proto][port].get('version', 'Unknown')
                    }
                    services.append(service_data)

            print(f"Services for host {host}: {services}")
            return {
                'host': host,
                'ip': host_info.get('addresses', {}).get('ipv4', 'Unknown'),
                'services': services
            }

        except Exception as e:
            print(f"Error scanning {host}: {e}")
            return None

    async def scan_hosts(self, hosts):
        """
        Scans multiple hosts asynchronously and retrieves their services.
        """
        loop = asyncio.get_event_loop()
        tasks = [loop.run_in_executor(None, self.scan_host, host) for host in hosts]
        results = await asyncio.gather(*tasks)

        # Filter out None results and return only successful scans
        return [result for result in results if result is not None]
