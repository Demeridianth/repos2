def hungover():
    answer = input('Would u like to start? y/n')

    if answer == 'y':
        print()
        start = True
        inventory = []

    else:
        print('Some other time')



    if start == True:
        print('You have a headache')
        print('Terrible dream again? Was it all a dream')
        print('Time to get up?')
        choice = input('Get up? (y/n)\n')
    #GET UP?

    #if you decided to get up
    if choice == 'y':
        choiceY1 = True
        print('You get up')
        print('You are in a shed, distant smell of smoke')
        print('###---You pick up your sword---###\n')
        inventory.append('Iron Sword')

    #if you decided to keep lying down
    else:
        choiceY1 = False
        print('you keep lying on hey in a shed, distant smell of smoke')
        print('loud voice: "hey big guy! want a drink"?')

    if choiceY1 == False:
        print('you see a man, covered in blood, smiling, drinking wine')
        print('you get up, fast')
        decision = input('come up slowly and accept the drink or ask him who is he is? (drink/ask)?')

    
    #if you decided to get up (have sword)
    elif choiceY1 == True:
        print('you walk out of the shed')
        print('a man walks up to you, nervous looking, bootle in this hand')
        approach = input('aproach the man? (y/n)?')


    #kept lying down, got up fast, (no sword)
    if decision == 'drink':
        print('the man starts to mumble about the gore and horror of the battle that just went down across the river')
        print('you notice something weird about him')
        print('you drink the wine, it warms up your belly, you relax')
    
    elif decision == 'ask':
        print('the man starts to mumble, he is nervous')
        print('his close doesnt fit him')
        


    

hungover()

        

    







    