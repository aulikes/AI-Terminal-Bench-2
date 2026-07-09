Read the access log at /app/access.log and write a JSON report to /app/report.json.

The report must be a JSON object with exactly these keys:
- total_requests: the total number of log entries in /app/access.log
- unique_ips: the number of distinct client IP addresses in /app/access.log
- top_path: the most frequently requested path in /app/access.log

Success criteria:
1. /app/report.json exists and contains a valid JSON object.
2. The JSON object contains exactly these keys: total_requests, unique_ips, and top_path.
3. The JSON object contains the correct values computed from /app/access.log.