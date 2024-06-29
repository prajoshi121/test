from functools import reduce
transactions=[100,500,-30,60,50,200,500]
for index,item in enumerate(transactions,start=1):
    print(f"transaction of {index} is: {item}")
total_amount=reduce(lambda x,y:x+y,transactions)
print(f"the total amount of all the transactions is:{total_amount}")

#using reduce to find avg rating of hotel B
from functools import reduce
ratings=[1.4,4.5,5.8,8.9,9.4,4.5]
for index,item in enumerate(ratings,start=1):
    print(f"rating of {index} is:  {item}")
avg=reduce(lambda x,y:x+y/2,ratings)
print(f"the average rating of hotel b is {avg}")
#combinig two dictionary using reduce

from functools import reduce

# List of dictionaries from different sources
data_sources = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"city": "New York", "country": "USA"},
    {"hobby": "Reading", "profession": "Engineer"}
]

# Function to combine two dictionaries
def combine_dicts(d1, d2):
    combined = {}
    for key in set(d1).union(set(d2)):
        if key in d1 and key in d2:
            if isinstance(d1[key], list):
                combined[key] = d1[key] + [d2[key]]
            else:
                combined[key] = [d1[key], d2[key]]
        elif key in d1:
            combined[key] = d1[key]
        else:
            combined[key] = d2[key]
    return combined

# Using reduce to merge all dictionaries
combined_data = reduce(combine_dicts, data_sources)
print(combined_data)




