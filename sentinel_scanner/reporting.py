import json
import csv
from jinja2 import Template
import os

class ReportGenerator:
    def __init__(self, output_dir="reports"):
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        self.output_dir = output_dir

    def generate_json(self, data, filename="scan_report.json"):
        path = os.path.join(self.output_dir, filename)
        try:
            with open(path, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"JSON report saved as {path}")
        except Exception as e:
            print(f"Error generating JSON report: {e}")

    def generate_csv(self, data, filename="scan_report.csv"):
        path = os.path.join(self.output_dir, filename)
        try:
            with open(path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Host", "Port", "Service", "Vulnerability"])
                for entry in data:
                    writer.writerow([entry['host'], entry['port'], entry['service'], entry['vulnerability']])
            print(f"CSV report saved as {path}")
        except Exception as e:
            print(f"Error generating CSV report: {e}")

    def generate_html(self, data, filename="scan_report.html"):
        path = os.path.join(self.output_dir, filename)
        try:
            template = """<html><head>
            <style>
                body { font-family: Arial, sans-serif; }
                h1 { color: #333; }
                table { width: 100%; border-collapse: collapse; }
                th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
                th { background-color: #f2f2f2; }
            </style>
            </head><body>
            <h1>Sentinel Scanner Report</h1>
            <table>
            <tr><th>Host</th><th>Port</th><th>Service</th><th>Vulnerability</th></tr>
            {% for entry in data %}
            <tr><td>{{ entry.host }}</td><td>{{ entry.port }}</td><td>{{ entry.service }}</td><td>{{ entry.vulnerability }}</td></tr>
            {% endfor %}
            </table>
            </body></html>"""
            tmpl = Template(template)
            with open(path, 'w') as f:
                f.write(tmpl.render(data=data))
            print(f"HTML report saved as {path}")
        except Exception as e:
            print(f"Error generating HTML report: {e}")
