# Network Scanning

## Useful nmap options:
- `-n`: Disable name and port resolution
- `-PR`: ARP host discovery
- `-Pn`: Disable host discovery
- `-sn`: Disable port scan (host discovery only)
- `-sS`/`-sT`/`-sU`: SYN/TCP connect/UDP scan
- `--top-ports 50`: Scan 50 top ports
- `-iL file`: Host input file
- `-oA file`: Write output files (3 file formats)
- `-sC`: Script scan (default scripts)
- `--script <file/category>`: Specific scripts
- `-sV`: Version detection
- `-6`: IPv6 scan
- `--open`: Do not wait for RST (improves speed)
- `-v`/`-d`: Verbose / debugging output

## Specify target via
- CIDR `10.5.23.0/24`, ranges `10.13-37.5.1-23` or input file `-iL scope.txt`.

## Reverse DNS lookup of IP address range:
