#%%
threshold = 3
items= (
  {'f','a','c','d','g','i','m','p'}
, {'a','b','c','f','l','m','o'}
, {'b','f','h','j','o'}
, {'b','c','k','s','p'}
, {'a','f','c','r','l','p','m','n'}

)

item_dict = dict()

for item_set in items:
  for item in item_set:
    if not item in  item_dict:
        item_dict[item] = 1
    else:
      item_dict[item] = item_dict [item] + 1

sort_orders ={x[0]:x[1] for x in sorted(item_dict.items(), key=lambda x: x[1], reverse=True)} 


for i in sort_orders:
  if sort_orders[i]  < threshold:
    sort_orders.pop(i)

print(sort_orders)

# %%
