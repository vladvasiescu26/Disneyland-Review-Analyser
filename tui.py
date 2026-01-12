# Display program title 
def display_title():
    title = "Disneyland Review Analyser"

    # Create dash line equal to number of characters in title
    line = "-" * len(title)

    print(line)
    print(title)
    print(line)

# Display Main 
def display_main_menu():
    print("\nPlease enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[C] Export Data")
    print("[X] Exit")


# Display View Data submenu
def display_view_menu():
    print("\nPlease enter one of the following options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per Year by Park")
    print("[D] Average Score per Park by Reviewer Location")


# Display Visualisation submenu
def display_visual_menu():
    print("\nPlease enter one of the following options:")
    print("[A] Most Reviewed Parks")
    print("[B] Park Ranking by Nationality")
    print("[C] Most Popular Month by Park")


# Display Export submenu
def display_export_menu():
    print("\nPlease enter one of the following options:")
    print("[A] Export as TXT")
    print("[B] Export as CSV")
    print("[C] Export as JSON")


# Get and standardise user input
def get_user_choice():
    return input("Enter your choice: ").strip().upper()


# Display a message to the user
def show_message(message):
    print(message)
