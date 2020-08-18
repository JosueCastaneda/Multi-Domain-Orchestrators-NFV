import pickle

time_spent = pickle.load(open('time_spent.p', 'rb'))
print('Time spent: ', time_spent)
