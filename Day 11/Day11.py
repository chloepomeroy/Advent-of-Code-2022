#!/usr/bin/env python
# coding: utf-8

# In[104]:


text_file = open("input.txt", "r")
data = text_file.read()
monkeys = [monkey.split('\n') for monkey in data.split('\n\n')]


# In[426]:


def monkey_business(monkeys):
    
    monkeys_dict = {}
    for i in range(len(monkeys)):
        monkeys_dict[i]={'Operation': {'op': monkeys[i][2][23:24], 'num':  monkeys[i][2][25:]}, 'Items': [int(worry_level) for worry_level in monkeys[i][1][18:].split(',')],'Test': int(monkeys[i][3][20:]), 'If True': int(monkeys[i][4][29:]), 'If False': int(monkeys[i][5][30:])}
    
    inspected = [0]*len(monkeys)

    for i in range(20):
            
        for monkey_num in range(len(monkeys)):
            monkey = monkeys_dict.get(monkey_num)
            true = []
            false = []
            for item in monkey.get('Items'):
                if monkey_num==2:
                    new = item*item
                    inspected[monkey_num] += 1
                elif '*' in monkey.get('Operation').get('op'):
                    new = item*int(monkey.get('Operation').get('num'))
                    inspected[monkey_num] += 1
                else:
                    new = item+int(monkey.get('Operation').get('num'))
                    inspected[monkey_num] += 1
                new = int(new/3)       
                
                
                if new%monkey.get('Test')==0:
                    true.append((new, item))

                else:
                    false.append((new, item))
            
            for i in true:
                monkeys_dict.get(monkey.get('If True')).get('Items').append(i[0])
                monkey.get('Items').remove(i[1])
            for i in false:
                monkeys_dict.get(monkey.get('If False')).get('Items').append(i[0])
                monkey.get('Items').remove(i[1])
            
    return sorted(inspected, reverse=True)[0]*sorted(inspected, reverse=True)[1]

            


# In[427]:


print(f"part 1 answer: {monkey_business(monkeys)}")


# In[428]:


def monkey_business_2(monkeys, rounds):
    
    monkeys_dict = {}
    for i in range(len(monkeys)):
        monkeys_dict[i]={'Operation': {'op': monkeys[i][2][23:24], 'num':  monkeys[i][2][25:]}, 'Items': [int(worry_level) for worry_level in monkeys[i][1][18:].split(',')],'Test': int(monkeys[i][3][20:]), 'If True': int(monkeys[i][4][29:]), 'If False': int(monkeys[i][5][30:])}
    
    inspected = [0]*len(monkeys)
    product = 1
    for i in range(len(monkeys)):        
        product = product * monkeys_dict.get(i).get('Test')

    for i in range(rounds):
            
        for monkey_num in range(len(monkeys)):
            monkey = monkeys_dict.get(monkey_num)
            true = []
            false = []
            for item in monkey.get('Items'):
                if monkey_num==2:
                    new = item*item
                    inspected[monkey_num] += 1
                elif '*' in monkey.get('Operation').get('op'):
                    new = item*int(monkey.get('Operation').get('num'))
                    inspected[monkey_num] += 1
                else:
                    new = item+int(monkey.get('Operation').get('num'))
                    inspected[monkey_num] += 1
                new = new%product
                    
                
                if new%monkey.get('Test')==0:
                    true.append((new, item))

                else:
                    false.append((new, item))
            
            for i in true:
                monkeys_dict.get(monkey.get('If True')).get('Items').append(i[0])
                monkey.get('Items').remove(i[1])
            for i in false:
                monkeys_dict.get(monkey.get('If False')).get('Items').append(i[0])
                monkey.get('Items').remove(i[1])
            
    return sorted(inspected, reverse=True)[0]*sorted(inspected, reverse=True)[1]

            


# In[429]:


print(f"part 2 answer: {monkey_business_2(monkeys, 10000)}")


# In[ ]:




