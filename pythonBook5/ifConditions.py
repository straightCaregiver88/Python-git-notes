alien_color = ['green','red','purple','gold']
points = 0
lider_color = 'gold'
target = input('Select the color of the alien that you whant to kill : ')

if(target in alien_color):
    print('you killed the alien +5 point')
    points += 5
    if(target == lider_color):
        print('Bonus for lider color +10')
        points += 10

else:   
    print('you missed')

print('Total point : '+str(points))