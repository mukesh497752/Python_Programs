
# Retail Sales Dashboard Using CSV and Matplotlib
# Using OOP

import os
import csv
import matplotlib.pyplot as plt
from datetime import datetime 


class SalesDashboard:

    def __init__(self, filename):
        self.filename = filename
        self.dates = []
        self.products = []
        self.sales = []

    # Read CSV file
    def load_data(self):
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.dates.append(row["Date"])
                self.products.append(row["Product"])
                self.sales.append(float(row["Sales"]))

        print("Sales Data Loaded Successfully!")

    # Display sales data
    def display_data(self):
        print("\nRetail Sales Data:")

        for i in range(len(self.dates)):
            print(self.dates[i], self.products[i],
                  self.sales[i])

    # Line graph
    def line_graph(self):
        daily_sales = {}

        for date, sale in zip(self.dates, self.sales):
            daily_sales[date] = daily_sales.get(date, 0) + sale

        dates = list(daily_sales.keys())
        values = list(daily_sales.values())

        plt.plot(dates, values, marker='o')

        plt.title("Daily Retail Sales")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Bar chart
    def bar_chart(self):
        product_sales = {}

        for product, sale in zip(self.products, self.sales):
            product_sales[product] = product_sales.get(product, 0) + sale

        plt.bar(product_sales.keys(), product_sales.values())

        plt.title("Product-wise Sales")
        plt.xlabel("Product")
        plt.ylabel("Total Sales")
        plt.tight_layout()
        plt.show()


# Create object
dashboard = SalesDashboard(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sales.csv")
)

# Call methods
dashboard.load_data()
dashboard.display_data()
dashboard.line_graph()
dashboard.bar_chart()
