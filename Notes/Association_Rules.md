## Association Rules:

Customer preferences prediction
Defined by frequency of items bought together and maximize sales.
Flat text file storage

**Which items are frequently bought together**

Posdata, soy homosexual y los cocodrilos me comieron la nariz

* Customer:{Item1, Item2, Item3, ...}
Association rule:

* Frequently added items

Item1 -> Item 3? [Probability of occurence]

**Support threshold**  Minimum itemset to 

Example:
Items = {Coke, Pepsi, Juice, Beer}
* B1 = {Coke, Beer}
* B2 = {Pepsi, Juice, Beer}
* B3 = {Coke, Juice}
* B4 = {Juice, Beer}
* B5 = {Coke, Juice, Beer}
* B6 = {Coke, Beer, Juice, pepsi}

**What is the confidence of the association rule**
{Coke, Beer} ! Juice?
– Confidence = 2 / 3 = 66.67%
– {Coke, Beer} occurs in 3 baskets B1, B5, B6. Out of these 3 baskets,
{Coke, Beer} is found together with Juice in the baskets B5 and B6

## Algorithm

1. Determine number of frequency itemsets support $\geq$ (If item A then B) **A priori principle**

## FP-Tree = Frequent pattern tree
Frequent pattern tree
* Root labeled as 'null' 
* Each node has three fields: item_name, count, node-link

1. Scan DB for the first time to generate L
2. Scan the DB for the secon time, order frequent items in 
each transaction
3. Buld FP-Tree

### Advantages:
*  DB scan twice
* Completeness Given a min-support thershold the db contains all the information
* Compactness Size of tree if bounded by the occurrences of frequent items
* Height of tree is bounded by the maximum number of items in a transaction

### Descending order helps keeping the FP-Tree with less branches.




| TID | Items bought   |
|-----|-----|
| 100 |{f,a,c,d,g,i,m,p}|
| 200 |{a,b,c,f,l,m,o}|
| 300 |{b,g,h,j,o}|
| 400 |{b,c,k,s,p}|
| 500 |{a,f,c,r,l,p,m,n}|


| Item | Frequency |
|-----|-----|
| f |4|
| c |4|
| a |3|
| b |3|
| m |3|
| p |3|


| TID | (ordered) Frequent items  |
|-----|-----|
| 100 |{f,c,a,m,p}|
| 200 |{f,c,a,b,m}|
| 300 |{f,b}|
| 400 |{c,b,p}|
| 500 |{f,c,a,m,p}|




```
a = 0
for i in 4:

```


