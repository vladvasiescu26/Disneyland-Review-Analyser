# Import required modules
import csv
import json
from collections import defaultdict


# Base exporter class
class BaseExporter:
    # Store dataset
    def __init__(self, data):
        self.data = data

    # Aggregate park statistics
    def aggregate(self):
        parks = defaultdict(list)

        for r in self.data:
            parks[r["Branch"]].append(r)

        output = {}

        for park, reviews in parks.items():
            ratings = [int(r["Rating"]) for r in reviews]
            locations = set(r["Reviewer_Location"] for r in reviews)

            output[park] = {
                "total_reviews": len(reviews),
                "positive_reviews": sum(1 for r in ratings if r >= 4),
                "average_rating": round(sum(ratings) / len(ratings), 2),
                "countries": len(locations)
            }

        return output


# TXT exporter
class TXTExporter(BaseExporter):
    def export(self):
        data = self.aggregate()
        with open("export.txt", "w") as file:
            for park, info in data.items():
                file.write(f"{park}\n")
                for key, value in info.items():
                    file.write(f"  {key}: {value}\n")
        print("Exported data to export.txt")


# CSV exporter
class CSVExporter(BaseExporter):
    def export(self):
        data = self.aggregate()
        with open("export.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Park", "Total Reviews", "Positive Reviews", "Average Rating", "Countries"])
            for park, info in data.items():
                writer.writerow([
                    park,
                    info["total_reviews"],
                    info["positive_reviews"],
                    info["average_rating"],
                    info["countries"]
                ])
        print("Exported data to export.csv")


# JSON exporter
class JSONExporter(BaseExporter):
    def export(self):
        data = self.aggregate()
        with open("export.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Exported data to export.json")
