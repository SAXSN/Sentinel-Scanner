import nmap
import socket
import asyncio

class SentinelScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def scan_host(self, host: str):
        try:
            self.nm.scan(host)
            return self.nm[host]
        except Exception as e:
            print(f"Error scanning {host}: {e}")
            return None

    async def scan_hosts(self, hosts):
        tasks = [self.scan_host(host) for host in hosts]
        results = await asyncio.gather(*tasks)
        return results
