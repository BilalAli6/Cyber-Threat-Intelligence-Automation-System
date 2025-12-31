<h1 align="center">🌐 Cyber Threat Intelligence Automation System</h1>


<div align="center">
<img width="855" height="267" alt="7" src="https://github.com/user-attachments/assets/8ae20b69-7ad8-46d4-90e5-6e0539d6b65e" />
  <p><em>Terminal highlights CVEs and threat advisories with color-coded severity</em></p>

  
<img width="854" height="389" alt="9" src="https://github.com/user-attachments/assets/572339dc-c91a-4bf6-8acd-a332b324e919" />
  <p><em>Structured JSON log of all detected events</em></p>
</div>

---

<p align="center">
  <strong>Built with ❤️ by Muhammad Bilal Ali Saif</strong> | 
  <a href="https://github.com/bilalali6">GitHub</a> | 
  <a href="https://inkedin.com/in/muhammad-bilal-ali-saif-a160a6284/">LinkedIn</a>
</p>

---

## 🚀 Features

<ul>
  <li>Fetch <strong>latest CVEs</strong> from <a href="https://nvd.nist.gov/">NVD</a></li>
  <li>Monitor <strong>security advisories</strong> and <strong>RSS feeds</strong></li>
  <li>Categorize events by severity: <strong>CRITICAL, HIGH, MEDIUM</strong></li>
  <li>Terminal alerts with <strong>color-coded boxes</strong> using <code>colorama</code></li>
  <li><strong>JSON logging</strong> for structured historical tracking</li>
  <li>Modular design for easy expansion</li>
</ul>

---

## 🛠 Technologies Used

<ul>
  <li>Python 3.x</li>
  <li><code>requests</code> / <code>aiohttp</code> for API calls</li>
  <li><code>feedparser</code> for RSS parsing</li>
  <li><code>colorama</code> for terminal formatting</li>
  <li>JSON for structured logging</li>
</ul>

---

## 💻 How to Run

```bash
# Clone the repository
git clone https://github.com/YourUsername/Cyber-Threat-Intel-Automation.git
cd Cyber-Threat-Intel-Automation

# Install dependencies
pip install requests feedparser colorama

# Run the monitoring system
python monitor.py
````

---

## 🔗 Example Output

<div style="background-color:#1e1e1e; color:#d4d4d4; padding:15px; border-radius:10px; font-family:monospace; overflow-x:auto;">
<b>Terminal</b><br>
[2025-12-31 17:30:32] CVE Feed -> Vulnerability -> CVE-2025-12345<br>
[2025-12-31 17:30:32] https://www.us-cert.gov/ncas/alerts.xml -> Threat Advisory -> Example Threat Title
</div>

<div style="background-color:#f5f5f5; color:#333; padding:15px; border-radius:10px; overflow-x:auto; margin-top:10px; font-family:monospace;">
<b>JSON Log</b><br>
[
  {
    "Source": "CVE Feed",
    "Event": "Vulnerability",
    "CVE_ID": "CVE-2025-12345",
    "Severity": "CRITICAL",
    "Description": "Example vulnerability affecting X...",
    "DetectedAt": "2025-12-31 17:30:32"
  },
  {
    "Source": "https://www.us-cert.gov/ncas/alerts.xml",
    "Event": "Threat Advisory",
    "Title": "Example Threat Title",
    "Link": "https://www.us-cert.gov/example",
    "Summary": "Short description of threat...",
    "DetectedAt": "2025-12-31 17:30:32"
  }
]
</div>

---

## 💡 Future Enhancements

<ul>
  <li>Email / Telegram alerts for <strong>critical events</strong></li>
  <li>Dark web paste monitoring</li>
  <li>Database storage for <strong>advanced analytics</strong> (SQLite / MongoDB)</li>
  <li>Web dashboard for <strong>real-time monitoring</strong></li>
</ul>

---

<p align="center">
  <em>Cyber Threat Intelligence Automation System — <strong>Made by Muhammad Bilal Ali Saif</strong></em>
</p>


