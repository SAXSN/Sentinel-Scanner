import json
import csv
from jinja2 import Template

class ReportGenerator:
    def generate_json(self, data, filename="scan_report.json"):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def generate_csv(self, data, filename="scan_report.csv"):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Host", "Port", "Service", "Vulnerability"])
            for entry in data:
                writer.writerow([entry['host'], entry['port'], entry['service'], entry['vulnerability']])

    def generate_html(self, data, filename="scan_report.html"):
        template = """<html><body>
        <h1>Sentinel Scanner Report</h1>
        <table border="1">
        <tr><th>Host</th><th>Port</th><th>Service</th><th>Vulnerability</th></tr>
        {% for entry in data %}
        <tr><td>{{ entry.host }}</td><td>{{ entry.port }}</td><td>{{ entry.service }}</td><td>{{ entry.vulnerability }}</td></tr>
        {% endfor %}
        </table>
        </body></html>"""
        tmpl = Template(template)
        with open(filename, 'w') as f:
            f.write(tmpl.render(data=data))
