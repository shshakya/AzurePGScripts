import psycopg2

# Connection details for the first PostgreSQL server
host1 = 'server1'
port1 = 5432
database1 = 'database1'
user1 = 'user1'
password1 = 'password'

# Connection details for the second PostgreSQL server
host2 = 'server2'
port2 = 5432
database2 = 'database2'
user2 = 'user2'
password2 = 'password'

# Connect to the first PostgreSQL server
conn1 = psycopg2.connect(
    host=host1,
    port=port1,
    database=database1,
    user=user1,
    password=password1
)

# Connect to the second PostgreSQL server
conn2 = psycopg2.connect(
    host=host2,
    port=port2,
    database=database2,
    user=user2,
    password=password2
)

# Create cursors for both connections
cur1 = conn1.cursor()
cur2 = conn2.cursor()

# Execute the SQL statement on the first server
cur1.execute('SELECT name, setting FROM pg_settings')

# Fetch all rows from the first server
rows1 = cur1.fetchall()

# Execute the SQL statement on the second server
cur2.execute('SELECT name, setting FROM pg_settings')

# Fetch all rows from the second server
rows2 = cur2.fetchall()

# Close the cursors and connections
cur1.close()
cur2.close()
conn1.close()
conn2.close()

# Create a dictionary to store the settings from both servers
settings_dict = {}

# Add settings from the first server to the dictionary
for row1 in rows1:
    name = row1[0]
    setting1 = row1[1]
    settings_dict[name] = (setting1, None)

# Add settings from the second server to the dictionary or update existing ones
for row2 in rows2:
    name = row2[0]
    setting2 = row2[1]
    if name in settings_dict:
        setting1 = settings_dict[name][0]
        settings_dict[name] = (setting1, setting2)

# Sort the settings by name
sorted_settings = sorted(settings_dict.items())

# Display the differences
differences_found = False
print("Differences between {} and {}:".format(host1, host2))
print("{:<25s} {:<25s} {:<25s}".format("Name", "Setting ({})".format(host1), "Setting ({})".format(host2)))
print("-" * 80)
for name, (setting1, setting2) in sorted_settings:
    if setting1 is not None and setting2 is not None and setting1 != setting2:
        differences_found = True
        print("{:<25s} {:<25s} {:<25s}".format(name, setting1, setting2))

if not differences_found:
    print("No differences found.")
