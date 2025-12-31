#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cyber Threat Intelligence Monitor
Author: Muhammad Bilal Ali Saif
Gmail: bilalalisaif6@gmail.com

Collects live vulnerability data from NVD
and security advisories from trusted RSS feeds.
Displays results in a rich terminal dashboard
and stores all findings locally in JSON format.
"""
import datetime
import json
import logging
import requests
import feedparser
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

# --- CONFIGURATION ---
# Note: NVD API v2.0 is the current standard
CVE_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
THREAT_FEEDS = [
    "https://www.us-cert.gov/ncas/alerts.xml",
    "https://www.cert.europa.eu/rss/alerts.xml"
]
ALERT_JSON_FILE = "cyber_threat_alerts.json"

console = Console()
logging.basicConfig(filename='cti_monitor.log', level=logging.INFO)

class ThreatIntelTool:
    def __init__(self):
        self.all_events = []

    def fetch_cves(self):
        """Fetches latest vulnerabilities from NVD"""
        try:
            # Fetching last 10 CVEs
            response = requests.get(CVE_API_URL, params={"resultsPerPage": 10}, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # NVD API v2 structure
            for vulnerability in data.get("vulnerabilities", []):
                cve = vulnerability.get("cve", {})
                metrics = cve.get("metrics", {}).get("cvssMetricV31", [{}])[0]
                severity = metrics.get("cvssData", {}).get("baseSeverity", "UNKNOWN")
                
                self.all_events.append({
                    "time": datetime.datetime.now().strftime("%H:%M:%S"),
                    "source": "NVD (CVE)",
                    "id": cve.get("id"),
                    "severity": severity,
                    "info": cve.get("descriptions", [{}])[0].get("value")[:75] + "..."
                })
        except Exception as e:
            logging.error(f"Error fetching CVEs: {e}")

    def fetch_rss_feeds(self):
        """Fetches security advisories from RSS feeds"""
        for url in THREAT_FEEDS:
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries[:3]:
                    self.all_events.append({
                        "time": datetime.datetime.now().strftime("%H:%M:%S"),
                        "source": "Advisory",
                        "id": entry.title[:30] + "...",
                        "severity": "INFO",
                        "info": entry.link
                    })
            except Exception as e:
                logging.error(f"Error fetching RSS {url}: {e}")

    def display_results(self):
        """Renders the data into a professional terminal table"""
        if not self.all_events:
            console.print("[bold red]No data retrieved. Check your connection.[/bold red]")
            return

        table = Table(title="Live Threat Intelligence Feed", title_style="bold magenta", expand=True)
        table.add_column("Time", style="cyan", no_wrap=True)
        table.add_column("Source", style="blue")
        table.add_column("Identifier/Title", style="white")
        table.add_column("Severity", justify="center")
        table.add_column("Description/Link", ratio=1)

        for e in self.all_events:
            sev = e['severity'].upper()
            sev_color = "red" if "CRIT" in sev or "HIGH" in sev else "yellow" if "MEDIUM" in sev else "green"
            
            table.add_row(
                e['time'],
                e['source'],
                e['id'],
                f"[{sev_color}]{sev}[/{sev_color}]",
                e['info']
            )

        console.print(table)

    def save_to_file(self):
        """Appends findings to the local JSON database"""
        try:
            try:
                with open(ALERT_JSON_FILE, "r") as f:
                    data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                data = []

            data.extend(self.all_events)
            with open(ALERT_JSON_FILE, "w") as f:
                json.dump(data, f, indent=4)
            console.print(f"\n[bold green]✔[/bold green] Logged {len(self.all_events)} events to {ALERT_JSON_FILE}")
        except Exception as e:
            console.print(f"[red]Failed to save logs: {e}[/red]")

def main():
    console.print(Panel.fit("🛡️  CYBER THREAT INTELLIGENCE AUTOMATION  🛡️", style="bold blue"))
    
    cti = ThreatIntelTool()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Polling NVD Database...", total=None)
        cti.fetch_cves()
        
        progress.add_task(description="Scanning Threat Feeds...", total=None)
        cti.fetch_rss_feeds()

    cti.display_results()
    cti.save_to_file()

if __name__ == "__main__":
    main()
