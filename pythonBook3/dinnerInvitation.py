#print 3 accepted invitations
friends = ['Rafa','Diego','Javier','Rodrigo','Samuel']
aux = 0
accept = 0
while aux < len(friends) and accept < 3:
    response = input('Hello '+ friends[aux] + ' would you like to have dinner today?')
    if(response not in ['yes','Yes']):
        print('lets meet other time, thanks for the heads up')
    else:
        print('see you at 3 at dominos')
        accept+=1
    aux+=1    
