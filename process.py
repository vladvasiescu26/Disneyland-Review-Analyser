# Import CSV handling
import csv
from collections import defaultdict


# Load CSV data into a list
def load_data(filepath):
    data = []
    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


# Return all reviews for a specific park
def reviews_by_park(data, park):
    return [r for r in data if r["Branch"].lower() == park.lower()]


# Count reviews by park and reviewer location
def count_reviews_by_park_and_location(data, park, location):
    return sum(
        1 for r in data
        if r["Branch"].lower() == park.lower()
        and r["Reviewer_Location"].lower() == location.lower()
    )


# Calculating average score per year for a park
def average_score_by_year(data, park, year):
    ratings = [
        int(r["Rating"]) for r in data
        if r["Branch"].lower() == park.lower()
        and r["Year_Month"].startswith(year)
    ]
    return round(sum(ratings) / len(ratings), 2) if ratings else 0


# Calculating average score per park by reviewer location
def avg_score_by_park_and_location(data):
    results = defaultdict(lambda: defaultdict(list))

    for r in data:
        results[r["Branch"]][r["Reviewer_Location"]].append(int(r["Rating"]))

    return {
        park: {
            location: sum(values) / len(values)
            for location, values in locations.items()
        }
        for park, locations in results.items()
    }
