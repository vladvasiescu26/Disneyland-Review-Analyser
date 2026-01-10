# Import text-based user interface functions
from tui import (
    display_title,
    display_main_menu,
    display_view_menu,
    display_visual_menu,
    display_export_menu,
    get_user_choice,
    show_message
)

# Import data processing functions
from process import (
    load_data,
    reviews_by_park,
    count_reviews_by_park_and_location,
    average_score_by_year,
    avg_score_by_park_and_location
)

# Import visualisation functions
from visual import (
    plot_reviews_per_park,
    plot_top_locations_for_park,
    plot_avg_rating_by_month
)

# Import exporter classes for OOP task
from exporter import TXTExporter, CSVExporter, JSONExporter


# Program entry point
def main():
    # Display title once at program start
    display_title()

    # Load dataset into a list
    data = load_data("data/disneyland_reviews.csv")

    # Confirm dataset loading and number of rows
    show_message(f"Dataset loaded successfully. Number of rows: {len(data)}")

    # Run program continuously until user exits
    while True:
        display_main_menu()
        choice = get_user_choice()

        if choice == "A":
            show_message("You have chosen option A - View Data")
            handle_view_menu(data)

        elif choice == "B":
            show_message("You have chosen option B - Visualise Data")
            handle_visual_menu(data)

        elif choice == "C":
            show_message("You have chosen option C - Export Data")
            handle_export_menu(data)

        elif choice == "X":
            show_message("Exiting program. Goodbye.")
            break

        else:
            show_message("Invalid menu choice. Please try again.")


# Handle View Data submenu (Section B + D)
def handle_view_menu(data):
    display_view_menu()
    choice = get_user_choice()

    if choice == "A":
        park = input("Enter park name: ")
        results = reviews_by_park(data, park)
        for review in results:
            print(review)

    elif choice == "B":
        park = input("Enter park name: ")
        location = input("Enter reviewer location: ")
        count = count_reviews_by_park_and_location(data, park, location)
        print(f"Number of reviews: {count}")

    elif choice == "C":
        park = input("Enter park name: ")
        year = input("Enter year (YYYY): ")
        avg = average_score_by_year(data, park, year)
        print(f"Average rating: {avg}")

    elif choice == "D":
        results = avg_score_by_park_and_location(data)
        for park, locations in results.items():
            print(f"\n{park}")
            for location, avg in locations.items():
                print(f"  {location}: {avg:.2f}")

    else:
        show_message("Invalid submenu choice.")


# Handle Visualisation submenu (Section C)
def handle_visual_menu(data):
    display_visual_menu()
    choice = get_user_choice()

    if choice == "A":
        plot_reviews_per_park(data)

    elif choice == "B":
        park = input("Enter park name: ")
        plot_top_locations_for_park(data, park)

    elif choice == "C":
        park = input("Enter park name: ")
        plot_avg_rating_by_month(data, park)

    else:
        show_message("Invalid submenu choice.")


# Handle Export submenu (Section D – OOP)
def handle_export_menu(data):
    display_export_menu()
    choice = get_user_choice()

    if choice == "A":
        TXTExporter(data).export()

    elif choice == "B":
        CSVExporter(data).export()

    elif choice == "C":
        JSONExporter(data).export()

    else:
        show_message("Invalid export option.")


# Run program
if __name__ == "__main__":
    main()
