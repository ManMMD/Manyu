kilograms=eval(raw_input('Enter the amount of water in kilograms:'))
initialtemperature=eval(raw_input('Enter the initial temperature:'))
finaltemperature=eval(raw_input('Enter the final temperature:'))
Q=kilograms*(finaltemperature-initialtemperature)*4184
print('The energy needed is '+str(Q))
