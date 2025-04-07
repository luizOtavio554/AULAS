item = []
while True:
    print('Insira algo ou fim: ')
    x = input()
    if x == 'fim':
        item.append(item)   
        break                                                                                                                                                                                            
    else:
      item.append(item)
      print(f'item:')
      print(len(item))