import picklehonda = (    'civic',    'grey',    '2009',    (        (1, 'James Brown'),        (2, 'John Dow')    ))models = ['honda','Vaz','BMW']owners = ['Peter','Martin','John']number = 100# with open('honda.pickle', 'bw') as readFromBinaryHonda:#     pickle.dump(honda, readFromBinaryHonda)## with open('honda.pickle', 'br') as readFromBinaryHonda:#     honda_from_file = pickle.load(readFromBinaryHonda)#     print(honda_from_file)#     model, color, year, ownerlist = honda_from_file#     print(model)#     print(color)#     print(year)#     print(ownerlist)#     for owner in ownerlist:#         ownerId, ownerName = owner#         print(ownerId)#         print(ownerName)with open('newBinaryFile.pickle','bw') as new_file:    pickle.dump(models,new_file)    pickle.dump(owners,new_file)    pickle.dump(number,new_file)with open('newBinaryFile.pickle','br') as read_new_file:    print(read_new_file)    models_from_file = pickle.load(read_new_file)    owners_from_file = pickle.load(read_new_file)    number_from_file = pickle.load(read_new_file)print(models_from_file)print(owners_from_file)print(number)# important that the order of writing should be the same when reading# all the file stores in PC memory