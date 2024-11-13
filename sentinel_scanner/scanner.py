import nmap
import asyncio

class SentinelScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def scan_host(self, host: str):
        """ Scan a single host and return simplified information """
        try:
            self.nm.scan(host)
            host_info = self.nm[host]
            # Extract only the relevant data to make it hashable (IP, ports, service info)
            host_data = {
                'host': host,
                'hostname': host_info.get('hostnames', []),
                'ip': host_info.get('addresses', {}).get('ipv4', ''),
                'services': list(host_info.get('all_protocols', []))  # list of protocols (ports)
            }
            return host_data
        except Exception as e:
            print(f"Error scanning {host}: {e}")
            return None

    async def scan_hosts(self, hosts):
        """ Scan multiple hosts asynchronously using loop.run_in_executor """
        loop = asyncio.get_event_loop()  # Get the event loop
        tasks = []

        # Run each host scan in a separate thread
        for host in hosts:
            task = loop.run_in_executor(None, self.scan_host, host)  # Non-blocking way to run scan_host
            tasks.append(task)
        
        # Wait for all tasks to complete and return the results
        results = await asyncio.gather(*tasks)  # Gather the scan results
        return [result for result in results if result is not None]  # Filter out None results
