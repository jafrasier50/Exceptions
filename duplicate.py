names = ["Josh", "Leah", "Ian", "Raven", "Rora", "Hayden", "Ian","Josh"]
not_duplicated_names = []

for name in names:
    if name not in not_duplicated_names:
        not_duplicated_names.append(name)
        
print(not_duplicated_names)
