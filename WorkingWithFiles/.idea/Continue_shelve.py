import shelvewith shelve.open('new_shelve_file') as nfs:    nfs['opel'] = 'germany'    nfs['mazda'] = 'japan'    nfs['ford'] = 'usa'    nfs['ferrari'] = 'Italia'    # print(nsf['ford'])    # for key in nfs:    #     print(key + ' : ' + nfs[key])    # if you will try to get acsess to not existing element you will se an error    # to avoid this you can use method get()    # print(nfs['ford'])    # print(nfs.get('honda')) # none return because there is no such key    # while True:    #     key = input('please enter the name of the car: ')    #     if key=='quit':    #         break    #     country = nfs.get(key,"We don't have a" + key)    #     print(country)    #     if key=='ford':    #         print(nfs[key])    # while True:    #     key = input('please enter the name of the car: ')  # .lower()    #     if key == 'quit':    #         print(key)    #         break    #     if key in nfs:    #         country = nfs[key]    #         print(country)    #     else:    #         print(" We don't have " + key)    #    #     print(key + ' : ' + nfs[key])    # to get values from the file    for values in nfs.values():        print(values)# you can use shelve without 'with' but you should manually close file at the end# somefile=shelve.open('newshelvefile')## somefile['test1']='one'# somefile['test2']='two'## somefile.close()