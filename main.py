import requests

usernames_list = open('usernames.txt', 'r', encoding='utf-8')
invalid_usernames = open('Results/invalid.txt', 'a', encoding='utf-8')
valid_usernames = open('Results/valid.txt', 'a', encoding='utf-8')

usernames = usernames_list.readlines()
for username in usernames:
    username = username.replace('\n', '')
    link = 'https://snapchat.com/add/' + username
    r = requests.get(link)
    if r.status_code == 200:
        print(f'Valid username : {username}')
        valid_usernames.write(username + '\n')
    elif r.status_code == 404:
        print(f'Invalid username : {username}')
        invalid_usernames.write(username + '\n')
    else:
        print(f'Error ! {username}')
