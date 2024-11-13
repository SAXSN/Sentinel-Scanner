import nmap
import asyncio

class SentinelScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def scan_host(self, host: str):
        try:
            self.nm.scan(host, arguments='-sS -sV')
            if host not in self.nm.all_hosts():
                return None
            
            host_info = self.nm[host]
            services = []
            for proto in host_info.all_protocols():
                for port in host_info[proto].keys():
                    service_data = {
                        'port': port,
                        'service': host_info[proto][port]['name'],
                        'version': host_info[proto][port].get('version', 'Unknown')
                    }
                    services.append(service_data)

            return {'host': host, 'services': services}
        
        except Exception as e:
            print(f"Error scanning {host}: {e}")
            return None

    async def scan_hosts(self, hosts):
        loop = asyncio.get_event_loop()
        tasks = [loop.run_in_executor(None, self.scan_host, host) for host in hosts]
        results = await asyncio.gather(*tasks)
        
        # Filter out None results and return a list of host data
        return [result for result in results if result is not None]
