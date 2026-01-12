# Import matplotlib for chart
import matplotlib.pyplot as plt
from collections import Counter, defaultdict


# Pie chart showing number of reviews per park
def plot_reviews_per_park(data):
    counts = Counter(r["Branch"] for r in data)
    plt.pie(counts.values(), labels=counts.keys(), autopct="%1.1f%%")
    plt.title("Number of Reviews per Park")
    plt.show()


# Bar chart showing top 10 locations by average rating
def plot_top_locations_for_park(data, park):
    ratings = defaultdict(list)

    for r in data:
        if r["Branch"].lower() == park.lower():
            ratings[r["Reviewer_Location"]].append(int(r["Rating"]))

    averages = {k: sum(v) / len(v) for k, v in ratings.items()}
    top = dict(sorted(averages.items(), key=lambda x: x[1], reverse=True)[:10])

    plt.bar(top.keys(), top.values())
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Average Rating")
    plt.title(f"Top 10 Reviewer Locations for {park}")
    plt.show()


# Bar chart showing average rating per month
def plot_avg_rating_by_month(data, park):
    months = defaultdict(list)

    for r in data:
        if r["Branch"].lower() == park.lower():
            month = int(r["Year_Month"].split("-")[1])
            months[month].append(int(r["Rating"]))

    ordered = sorted(months.items())
    labels = [str(m) for m, _ in ordered]
    values = [sum(v) / len(v) for _, v in ordered]

    plt.bar(labels, values)
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.title(f"Average Rating by Month for {park}")
    plt.show()
