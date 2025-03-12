# DNS Exploration

## Overview
DNS (Domain Name System) Exploration involves querying DNS servers to retrieve information about domain names, such as their IP addresses, mail servers, and other DNS records. This can help in network diagnostics, cybersecurity investigations, and domain management.

This Python script enables users to:
- Resolve a domain name to its IP address.
- Retrieve specific DNS records such as A, MX, NS, TXT, and CNAME.

## Prerequisites
Ensure you have Python installed (preferably Python 3.x). You also need to install the required dependencies:

```sh
pip install dnspython
```

## How to Run the Script
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script with the desired domain and DNS record type:

```sh
python DNSExploration.py example.com A
```

Replace `example.com` with the domain you want to explore and `A` with the desired record type (e.g., MX, NS, TXT, CNAME).

## Example Output
```
IP Address: 93.184.216.34
MX Records: ['10 mail.example.com.']
NS Records: ['ns1.example.com.', 'ns2.example.com.']
```

## Notes
- If the domain cannot be resolved, the script will display an error message.
- Ensure you have a stable internet connection to query DNS records successfully.




