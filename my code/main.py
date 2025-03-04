# Level 1: List all free tables
def get_free_tables(restaurant_tables, timeslot):
    free_tables = []
    for col in range(1, len(restaurant_tables[0])):  # Skip the first column (which is row header)
        if restaurant_tables[timeslot][col] == 'o':
            free_tables.append(restaurant_tables[0][col])  # Add table ID
    return free_tables

# Level 2: Find one table for the party size
def find_table_for_party(restaurant_tables, timeslot, party_size):
    for col in range(1, len(restaurant_tables[0])):
        table_capacity = int(restaurant_tables[0][col].split('(')[1].split(')')[0])
        if restaurant_tables[timeslot][col] == 'o' and table_capacity >= party_size:
            return restaurant_tables[0][col]  # Return the table ID
    return None  # If no suitable table found

# Level 3: Find all free tables that fit the party size
def find_all_tables_for_party(restaurant_tables, timeslot, party_size):
    suitable_tables = []
    for col in range(1, len(restaurant_tables[0])):
        table_capacity = int(restaurant_tables[0][col].split('(')[1].split(')')[0])
        if restaurant_tables[timeslot][col] == 'o' and table_capacity >= party_size:
            suitable_tables.append(restaurant_tables[0][col])
    return suitable_tables

# Level 4: Find tables or combinations of adjacent tables for the party size
def find_tables_for_party_with_combinations(restaurant_tables, timeslot, party_size):
    suitable_combinations = []
    
    # Check for individual tables
    for col in range(1, len(restaurant_tables[0])):
        table_capacity = int(restaurant_tables[0][col].split('(')[1].split(')')[0])
        if restaurant_tables[timeslot][col] == 'o' and table_capacity >= party_size:
            suitable_combinations.append([restaurant_tables[0][col]])

    # Check for adjacent table combinations
    for col in range(1, len(restaurant_tables[0]) - 1):
        table1_capacity = int(restaurant_tables[0][col].split('(')[1].split(')')[0])
        table2_capacity = int(restaurant_tables[0][col+1].split('(')[1].split(')')[0])
        
        if (restaurant_tables[timeslot][col] == 'o' and 
            restaurant_tables[timeslot][col+1] == 'o' and
            table1_capacity + table2_capacity >= party_size):
            suitable_combinations.append([restaurant_tables[0][col], restaurant_tables[0][col+1]])

    return suitable_combinations

# Bonus: User-friendly output message
def display_table_combinations(combinations):
    for combo in combinations:
        if len(combo) == 1:
            print(f"Table {combo[0]} is free and can seat {int(combo[0].split('(')[1].split(')')[0])} people.")
        else:
            total_capacity = sum([int(table.split('(')[1].split(')')[0]) for table in combo])
            tables = ' and '.join(combo)
            print(f"Tables {tables} together can seat {total_capacity} people.")


restaurant_tables = [
    [0, 'T1(2)', 'T2(4)', 'T3(2)', 'T4(6)', 'T5(4)', 'T6(2)'],
    [1, 'o', 'o', 'o', 'o', 'o', 'o'],
    [2, 'o', 'x', 'o', 'o', 'o', 'o'],
    [3, 'x', 'o', 'o', 'x', 'o', 'o']
]

restaurant_tables = [
  [0,      'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
  [1,      'o',      'o',      'o',      'o',      'o',      'o'],
  [2,      'o',      'o',      'o',      'o',      'o',      'o'],
  [3,      'x',      'o',      'o',       'x',       'x',    'o',]
  
  print(get get_free_tables(restruant_tables, 1))
  print(find_table_for party(restaurant_table, 1, 2))
  print(find_all_table_for party(restaurant_table, 1, 2))
  print(find_table_for_party_with_combinations(restaurant_table, 1, 5))
  display_table(find_table_for_party_with_combinations(restaurant_table, 1, 5))