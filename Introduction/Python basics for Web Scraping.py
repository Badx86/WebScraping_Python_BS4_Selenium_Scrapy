import pandas as pd

states = ["California", "Texas", "Utah", "Vermont", "New York"]
population = [59613493, 29730311, 21944577, 19299981, 41949499]

dict_states = {'States': states, 'Population': population}

df_states = pd.DataFrame.from_dict(dict_states)
# print(df_states)
df_states.to_csv('states.csv', index=False)


# print(states[-1])

# for state in states:
#     if state == "Utah":
#         print(state)

# with open('test.txt', 'w') as file:
#     file.write("Data successfully scraped!")