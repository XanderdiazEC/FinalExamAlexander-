#!/usr/bin/env python3

def main():
    # Define party items with their values
    party_items = [
        {"name": "Cake", "value": 20},
        {"name": "Balloons", "value": 21},
        {"name": "Music System", "value": 10},
        {"name": "Lights", "value": 5},
        {"name": "Catering Service", "value": 8},
        {"name": "DJ", "value": 3},
        {"name": "Photo Booth", "value": 15},
        {"name": "Tables", "value": 7},
        {"name": "Chairs", "value": 12},
        {"name": "Drinks", "value": 6},
        {"name": "Party Hats", "value": 9},
        {"name": "Streamers", "value": 18},
        {"name": "Invitation Cards", "value": 4},
        {"name": "Party Games", "value": 2},
        {"name": "Cleaning Service", "value": 11}
    ]

    # Display the list of party items
    print("Available Party Items:")
    for i, item in enumerate(party_items):
        print(f"{i}: {item['name']}")
    
    # Get user input for item selection
    try:
        user_input = input("\nEnter item indices separated by commas (e.g., 0, 2): ")
        selected_indices = [int(idx.strip()) for idx in user_input.split(',')]
        
        # Validate indices
        for idx in selected_indices:
            if idx < 0 or idx >= len(party_items):
                print(f"Invalid index: {idx}. Please use indices between 0 and {len(party_items) - 1}.")
                return
        
        # Get selected items and their values
        selected_items = [party_items[idx] for idx in selected_indices]
        
        # Calculate base party code using bitwise AND
        if not selected_items:
            print("No items selected. Please select at least one item.")
            return
            
        base_code = selected_items[0]["value"]
        bitwise_expression = f"{base_code}"
        
        for item in selected_items[1:]:
            base_code &= item["value"]
            bitwise_expression += f" & {item['value']}"
        
        # Apply conditions to modify the base code
        message = ""
        final_code = base_code
        
        if base_code == 0:
            final_code = base_code + 5
            message = "Epic Party Incoming!"
        elif base_code > 5:
            final_code = base_code - 2
            message = "Let's keep it classy!"
        else:
            message = "Chill vibes only!"
        
        # Prepare selected item names for output
        selected_names = [item["name"] for item in selected_items]
        
        # Generate HTML output
        html_output = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Party Planner Results</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .result-container {{ background-color: #f7f7f7; padding: 20px; border-radius: 5px; }}
                .highlight {{ font-weight: bold; color: #007bff; }}
            </style>
        </head>
        <body>
            <div class="result-container">
                <h2>Party Planner Results</h2>
                <p><span class="highlight">Selected Items:</span> {', '.join(selected_names)}</p>
                <p><span class="highlight">Base Party Code:</span> {bitwise_expression} = {base_code}</p>
                
                <p><span class="highlight">Adjusted Party Code:</span> 
                {base_code} {'+' if base_code == 0 else '-' if base_code > 5 else ''} {5 if base_code == 0 else 2 if base_code > 5 else ''} 
                {f'= {final_code}' if base_code == 0 or base_code > 5 else ''}</p>
                
                <p><span class="highlight">Final Party Code:</span> {final_code}</p>
                <p><span class="highlight">Message:</span> {message}</p>
            </div>
        </body>
        </html>
        """
        
        # Display HTML output
        print("\nHTML Output:")
        print(html_output)
        
        # Save HTML output to a file
        with open("party_result.html", "w") as file:
            file.write(html_output)
        print("\nResults saved to party_result.html")
        
        # Display console output
        print("\nConsole Output:")
        print(f"Selected Items: {', '.join(selected_names)}")
        print(f"Base Party Code: {bitwise_expression} = {base_code}")
        if base_code == 0:
            print(f"Adjusted Party Code: {base_code} + 5 = {final_code}")
        elif base_code > 5:
            print(f"Adjusted Party Code: {base_code} - 2 = {final_code}")
        print(f"Final Party Code: {final_code}")
        print(f"Message: {message}")
        
    except ValueError:
        print("Invalid input. Please enter valid indices separated by commas.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()