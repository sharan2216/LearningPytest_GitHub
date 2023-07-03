dict1={221:'apple',121:'banana',111:'grapes',132:'mango'}

# sorted_key={k:v for k,v in sorted(dict1.items())}
# sorted_value={k:v for k,v in sorted(dict1.items(), key= lambda v: v[1])}
# print(sorted_key)
# print(sorted_value)


sorted_key={k:v for k,v in sorted(dict1.items())}
sorted_val={k:v for k,v in sorted(dict1.items(),key = lambda v:v[1])}
print(sorted_key)
print(sorted_val)