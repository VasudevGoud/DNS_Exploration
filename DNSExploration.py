import socket
import dns.resolver

def get_ip(domain):
    """Get the IP address of a domain."""
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return "Could not resolve domain"

def get_dns_records(domain, record_type):
    """Fetch specified DNS records for a domain."""
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [answer.to_text() for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        return f"No {record_type} records found"

def scan_subdomains(domain, subdomains):
    """Check for active subdomains from a given list."""
    found_subdomains = {}
    for sub in subdomains:
        subdomain = f"{sub}.{domain}"
        ip = get_ip(subdomain)
        if "Could not resolve" not in ip:
            found_subdomains[subdomain] = ip
    return found_subdomains

if __name__ == "__main__":
    domain = input("Enter the domain: ")
    print(f"IP Address: {get_ip(domain)}")
    
    record_types = ["A", "MX", "NS", "TXT", "CNAME"]
    for record in record_types:
        print(f"{record} Records: {get_dns_records(domain, record)}")
    
    subdomain_list = ["www", "mail", "ftp", "api", "blog"]
    active_subdomains = scan_subdomains(domain, subdomain_list)
    print("Active Subdomains:", active_subdomains)
