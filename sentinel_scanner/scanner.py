import nmap
import asyncio

class SentinelScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def scan_host(self, host: str):
        """ Scan a single host and return the result """
        try:
            self.nm.scan(host)
            host_info = self.nm[host]  # Retrieve the host info from nmap
            # Extract necessary information (you can adjust this as needed)
            host_data = {
                'host': host,
                'hostname': host_info.get('hostnames', []),
                'ip': host_info.get('addresses', {}).get('ipv4', ''),
                'services': host_info.get('all_protocols', [])
            }
            return host_data
        except Exception as e:
            print(f"Error scanning {host}: {e}")
            return None

    async def scan_hosts(self, hosts):
        """ Scan multiple hosts asynchronously """
        tasks = [self.scan_host(host) for host in hosts]
        results = await asyncio.gather(*tasks)  # Gather the scan results
        # Filter out None results (in case of errors)
        return [result for result in results if result]
