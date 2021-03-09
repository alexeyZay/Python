def greet_user(name,isEnemy):
    if isEnemy:
        return f'Hey {name}! Where are you? I will find you'
    else:
        return f'Hello {name}! How are you?'
    
def cooking_burgers(number,isHungry):
    if isHungry:
        return f'Need more? I will bring them to you'
    else:
        return f'You eat more then {number} burgers! Why you still hungry?'