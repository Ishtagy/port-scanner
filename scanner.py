import socket
import sys

if len(sys.argv) != 2:
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

target = sys.argv[1]
print(f"Scanning {target}")

cnt = 0
try:
    for port in range(1, 1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        rslt = s.connect_ex((target, port))
        if rslt == 0:
            print(f"Port {port} is open")
            cnt += 1
        s.close()
    print(f"{cnt} out of 1000 ports is open")
except KeyboardInterrupt:
    sys.exit()
except socket.error:
    print(f"Couldn't connect to {target}")
    sys.exit()


