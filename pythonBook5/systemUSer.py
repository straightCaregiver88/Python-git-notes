
from random import seed
from random import randint
#seed(1)
user_name = ['luis','pedro','paulina','Admin']
user_message=[
    'Welcome : ',
    'Welcome back : ',
    'Crawling back : ',
    'Hello my cure admin : '
]
ran = randint(0,len(user_message))

logged_user = input('enter your name\n')


if(logged_user.lower() in (user.lower() for user in user_name)):
    if(logged_user == "admin"):
        print(user_message[3]+' '+logged_user)
    else:
        print(user_message[ran]+' '+logged_user)