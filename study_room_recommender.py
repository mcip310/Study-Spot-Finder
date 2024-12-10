import os
import sqlite3

# Clear terminal logs
def clear_logs():
    os.system('cls' if os.name == 'nt' else 'clear')

# Connect to the database
def connect_to_db():
    return sqlite3.connect("study_spaces.db")

# Query the database based on user input
def query_study_spaces(conn, campus, busyness, needs_computer, wants_to_eat):
    cursor = conn.cursor()

    # Base query
    query = """
    SELECT room_name, building, popularity, has_computers
    FROM study_spaces
    WHERE 1=1
    """
    params = []

    # Add campus filter if not "No Preference"
    if campus != "No Preference":
        query += " AND campus = ?"
        params.append(campus)

    # Add filters for busyness
    if busyness == "Quiet":
        query += " AND popularity <= 5"
    elif busyness == "Background noise":
        query += " AND popularity > 5"

    # Add filters for computers if specified
    if needs_computer == "Yes":
        query += " AND has_computers = 'Yes'"
    elif needs_computer == "No":
        query += " AND has_computers = 'No'"

    # Add filters for food preferences
    if wants_to_eat == "Yes":
        query += """
        AND (room_name LIKE '%cafe%' 
             OR room_name LIKE '%cafeteria%' 
             OR room_name LIKE '%atrium%' 
             OR room_name LIKE '%food%')
        """
    elif wants_to_eat == "No":
        query += """
        AND (room_name NOT LIKE '%cafe%' 
             AND room_name NOT LIKE '%cafeteria%' 
             AND room_name NOT LIKE '%atrium%' 
             AND room_name NOT LIKE '%food%')
        """

    # Execute the query
    cursor.execute(query, params)
    return cursor.fetchall()

# Get user input with validation (case-insensitive)
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input == "NP":
            return "No Preference"
        if user_input.lower() in [option.lower() for option in valid_options]:
            # Return the correctly formatted option
            return next(option for option in valid_options if option.lower() == user_input.lower())
        print(f"Invalid input. Please choose from {', '.join(valid_options)} or type NP for No Preference.")

# Restart the questionnaire
def restart_questionnaire():
    print("\nNo study spaces found matching your preferences. Let's try again.\n")
    input("Press Enter to restart...")
    clear_logs()
    user_interface()

# User Interface
def user_interface():
    clear_logs()
    print("Welcome to the Enhanced Study Room Finder!")

    # Validate campus input
    campus = get_valid_input(
        "Enter your preferred campus (e.g., College Ave, Busch, Livingston, Cook/Douglass) or type NP for No Preference: ",
        ["College Ave", "Busch", "Livingston", "Cook/Douglass"]
    )
    busyness = get_valid_input(
        "Do you prefer 'quiet' spaces, 'background noise', or type NP for No Preference: ",
        ["Quiet", "Background noise"]
    )
    needs_computer = get_valid_input(
        "Do you need a room with a computer? (Yes/No) or type NP for No Preference: ",
        ["Yes", "No"]
    )
    wants_to_eat = get_valid_input(
        "Do you want to eat while you study? (Yes/No) or type NP for No Preference: ",
        ["Yes", "No"]
    )

    # Connect to the database and query
    conn = connect_to_db()
    try:
        results = query_study_spaces(conn, campus, busyness, needs_computer, wants_to_eat)
        if results:
            clear_logs()
            print("Recommended Study Spaces:")
            for room_name, building, popularity, has_computers in results:
                print(f"- {room_name} in {building} (Popularity: {popularity}, Computers: {has_computers})")
            print("\nThank you for using the Study Room Finder!")
        else:
            restart_questionnaire()
    finally:
        conn.close()

    # Ask if the user wants to search again
    restart = get_valid_input("\nWould you like to search for another room? (Yes/No): ", ["Yes", "No"])
    if restart == "Yes":
        clear_logs()
        user_interface()
    else:
        clear_logs()
        print("Goodbye!")

# Run the program
if __name__ == "__main__":
    user_interface()
