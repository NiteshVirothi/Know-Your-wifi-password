import subprocess

#stores all the profiles
a = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
#stores profile in list form
a1 = [i.split(":")[1][1:-1] for i in a if "All user profile" in i]

#check and print wifi and password if available
for i in a1:
    #This checks for password make sure key=clear to get password in clear txt
    results=subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split('\n')
    #store obtained password in list form
    results=[b.split(":")[1][1:-1] for b in results if "key content" in b]
    #print wifi names and passwords
    try:
        print("{:<30)| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30)| {:<}".format(i, ""))
