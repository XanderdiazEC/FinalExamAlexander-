#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()  # Enable error display in the browser

# Dictionary of party items and their corresponding values
party_items = {
    0: ("Cake", 20),
    1: ("Balloons", 21),
    2: ("Music System", 10),
    3: ("Lights", 5),
    4: ("Catering Service", 8),
    5: ("DJ", 3),
    6: ("Photo Booth", 15),
    7: ("Tables", 7),
    8: ("Chairs", 12),
    9: ("Drinks", 6),
    10: ("Party Hats", 9),
    11: ("Streamers", 18),
    12: ("Invitation Cards", 4),
    13: ("Party Games", 2),
    14: ("Cleaning Service", 11)
}

def calculate_party_code(selected_indices):
    if not selected_indices:
        return 0, 0, "No items selected."

    # Convert to int and extract values
    selected_indices = [int(i) for i in selected_indices]
    selected_names = [party_items[i][0] for i in selected_indices]
    selected_values = [party_items[i][1] for i in selected_indices]

    # Perform bitwise AND across all values
    base_code = selected_values[0]
    for val in selected_values[1:]:
        base_code &= val

    # Adjust base code with logic
    if base_code == 0:
        final_code = base_code + 5
        message = "Epic Party Incoming!"
    elif base_code > 5:
        final_code = base_code - 2
        message = "Let's keep it classy!"
    else:
        final_code = base_code
        message = "Chill vibes only!"

    return base_code, final_code, message, selected_names, selected_values

# Print HTTP headers
print("Content-Type: text/html\n")

# Get form data
form = cgi.FieldStorage()
selected_items = form.getlist("items")

# Calculate party code and message
try:
    base_code, final_code, message, names, values = calculate_party_code(selected_items)
except Exception as e:
    print(f"<h1>Error</h1><p>{e}</p>")
    exit()

# Generate HTML output
print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Your Party Plan</title>
</head>
<body>
    <h1>🎉 Your Party Plan 🎉</h1>
    <p><strong>Selected Items:</strong> {', '.join(names)}</p>
    <p><strong>Base Party Code:</strong> {' & '.join(str(v) for v in values)} = {base_code}</p>
    <p><strong>Final Party Code:</strong> {final_code}</p>
    <p><strong>Message:</strong> {message}</p>
</body>
</html>
""")
