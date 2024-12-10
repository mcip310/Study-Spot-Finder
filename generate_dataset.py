import pandas as pd

# College Ave Campus
college_ave_data = {
    "campus": ["College Ave"] * 30,
    "building": [
        "Alexander Library", "Alexander Library", "Alexander Library", "Alexander Library", "Alexander Library",
        "Alexander Library", "Alexander Library", "Alexander Library", "Alexander Library", "Alexander Library",
        "Alexander Library", "Alexander Library", "Alexander Library", "Alexander Library", "Alexander Library",
        "Academic Building", "Academic Building", "Art Library", "Art Library",
        "College Avenue Student Center", "College Avenue Student Center", "College Avenue Student Center",
        "College Avenue Student Center", "College Avenue Student Center", "College Avenue Student Center",
        "School of Communications and Information", "School of Communications and Information",
        "Spring Street SAS Language Lab", "TJ's Cafe at Zimmerli", "Voorhees Hall - Lobby"
    ],
    "room_name": [
        "Digital Learning Commons", "Digital Learning Commons Audio Booth", "Digital Learning Commons Conference Rooms",
        "Digital Learning Commons Huddle Room 128H", "Digital Learning Commons Huddle Room 128M",
        "Digital Learning Commons One Button Studio 132", "Digital Learning Commons One Button Studio 133",
        "Digital Learning Commons Pitch Room", "Digital Learning Commons Study Conference Room", "Room 301A",
        "Room 301B", "Room 301C", "Room 301D", "Room 301E", "Room 301F", "Computer Center Lab", "Learning Center",
        "Art Library", "Art Library Room 105A", "4th Floor Lounge", "Atrium Food Court", "Front Patio",
        "Graduate Student Lounge", "Main Lounge", "Red Lion Cafe", "Common Area", "Student Lounge",
        "Spring Street SAS Language Lab", "TJ's Cafe at Zimmerli", "Voorhees Hall - Lobby"
    ],
    "popularity": [
        8, 4, 8, 5, 5, 4, 4, 3, 9, 7, 7, 7, 7, 7, 7, 7, 9, 6, 6, 7, 10, 3, 3, 10, 3, 3, 2, 1, 1, 3
    ],
    "has_computers": [
        "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "No", "Yes", "No", "No", "No", "No", "No", "No",
        "Yes", "No", "Yes", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No"
    ]
}

# Busch Campus
busch_data = {
    "campus": ["Busch"] * 25,
    "building": [
        "Allison Road Classrooms", "Busch Campus Computing Lab", "Busch Math & Science Learning Center",
        "Busch Student Center", "Busch Student Center", "Busch Student Center", "Busch Student Center",
        "Busch Student Center", "Chemistry & Chemical Biology", "Computer Science Building",
        "Ernest Mario School of Pharmacy", "Fiber Optics Materials Research Building",
        "Library of Science and Medicine", "Library of Science and Medicine", "Library of Science and Medicine",
        "Library of Science and Medicine", "Library of Science and Medicine", "Library of Science and Medicine",
        "Paul Robeson Cultural Center", "Paul Robeson Cultural Center", "Paul Robeson Cultural Center",
        "Paul Robeson Cultural Center", "Paul Robeson Cultural Center", "Richard Weeks Hall of Engineering",
        "Richard Weeks Hall of Engineering"
    ],
    "room_name": [
        "Mezzanine", "Computing Lab", "Learning Center", "Fireside Lounge", "Food Court", "International Lounge",
        "Quiet Lounge", "The Cove", "Lounge", "Lobby", "Atrium", "Lobby", "Room 1", "Room 2", "Room 3", "Room 4",
        "Room 5", "Main Library", "Computer Room", "Gathering Lounge", "Dr. Cheryl A. Wall Reading Room",
        "Meeting Room", "Ujima Conference Room", "Atrium", "Lobby"
    ],
    "popularity": [
        5, 5, 7, 6, 10, 6, 7, 9, 3, 4, 6, 3, 4, 4, 4, 4, 4, 3, 3, 1, 2, 2, 1, 6, 9
    ],
    "has_computers": [
        "No", "Yes", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "Yes", "Yes", "Yes", "Yes",
        "Yes", "Yes", "No", "No", "No", "No", "No", "No", "No"
    ]
}

# Cook/Douglass Campus
cook_douglass_data = {
    "campus": ["Cook/Douglass"] * 22,
    "building": [
        "Chang Library", "Cook Student Center", "Cook Student Center", "Cook Student Center",
        "Cook/Douglass Computer Center", "Douglass Library", "Douglass Library", "Douglass Library",
        "Douglass Library", "Douglass Library", "Douglass Library", "Douglass Library",
        "Douglass Student Center", "Douglass Student Center", "Douglass Student Center",
        "Douglass Student Center", "Douglass Student Center", "Food Sciences Building",
        "Institute of Food Nutrition & Health", "James B. Carey Library", "Mortensen Hall",
        "Stephen and Lucy Science Library"
    ],
    "room_name": [
        "Room 139-6", "2nd Floor Lounge", "2nd Floor Quiet Lounge", "Outside Patio",
        "Main Computer Center", "Main Library", "Capaccio Room", "Room 1A",
        "Room 1B", "Room 1C", "Sabb Room", "Computer Lab", "Douglass Collaborative Center",
        "Douglass Lounge", "Front Outside Patio", "NJC Lounge", "Red Pine Lounge", "Lobby", "Atrium",
        "Main Library", "Lobby", "Main Library"
    ],
    "popularity": [
        3, 6, 6, 5, 8, 9, 6, 6, 6, 6, 3, 5, 5, 9, 5, 2, 2, 5, 6, 5, 7, 7
    ],
    "has_computers": [
        "No", "Yes", "Yes", "No", "Yes", "Yes", "No", "No", "No", "No", "No", "Yes", "Yes",
        "No", "No", "No", "No", "No", "No", "No", "No", "No"
    ]
}

# Livingston Campus
livingston_data = {
    "campus": ["Livingston"] * 15,
    "building": [
        "Business Rockafeller Road", "Business Rockafeller Road", "Carr Library", "Carr Library",
        "Livingston Computing Center", "Livingston Computing Center", "Livingston Student Center",
        "Livingston Student Center", "Livingston Student Center", "Livingston Student Center",
        "Livingston Student Center", "Livingston Student Center", "Livingston Student Center",
        "Tillett Hall", "Tillett Hall"
    ],
    "room_name": [
        "5th Floor Lounge", "Mezzanine Lounge", "Main Library", "Computer Lab",
        "Main Computing Center", "Room 106G", "1st Floor Lounge", "Coffee House",
        "Collaborative Learning Center", "Food Court", "Gathering Lounge", "Livingston Courtyard (Back Patio)",
        "The Space", "Lobby", "Second Floor Lounge"
    ],
    "popularity": [
        7, 7, 5, 5, 7, 3, 8, 8, 5, 9, 6, 6, 6, 8, 6
    ],
    "has_computers": [
        "No", "Yes", "Yes", "Yes", "No", "No", "Yes", "No", "No", "No", "No", "No", "No", "No", "No"
    ]
}

# Combine all datasets
all_data = pd.concat([
    pd.DataFrame(college_ave_data),
    pd.DataFrame(busch_data),
    pd.DataFrame(cook_douglass_data),
    pd.DataFrame(livingston_data)
], ignore_index=True)

# Save the updated dataset
all_data_csv_path = "All_Campus_Study_Spaces_With_Amenities.csv"
all_data.to_csv(all_data_csv_path, index=False)

print(f"Updated dataset saved as {all_data_csv_path}.")
