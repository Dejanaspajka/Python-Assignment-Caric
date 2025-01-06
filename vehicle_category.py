import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the data
# Load the data from a text file, where values are separated by ':'
data_array = np.loadtxt('data_caric.txt').flatten()
print("Loaded Data:", data_array)

# Step 2: Define the categories
# Categories are defined with their labels and corresponding length ranges
categories = {
    "1: Short vehicles and motorcycles": (0, 4.5),
    "2: Longer vehicles and vans": (4.5, 6.4),
    "3: Buses and vehicles with trailers": (6.4, 14.6),
    "4: Trucks and extended buses": (14.6, 50),
}

# Step 3: Categorize the data
def categorize_data(data, categories):
    category_counts = {category: 0 for category in categories}
    for value in data:
        assigned = False  # Track if value has been categorized
        for category, (lower, upper) in categories.items():
            if lower < value <= upper:  # Open lower bound, closed upper bound
                category_counts[category] += 1
                assigned = True
                break
        if not assigned:
            print(f"Warning: Value {value} did not fit any category")
    return category_counts

# Step 4: Process the data into categories
category_counts = categorize_data(data_array, categories)
print("Category Counts:", category_counts)

# Step 5: Prepare data for plotting
labels = list(category_counts.keys())  # Extract category names
values = list(category_counts.values())  # Extract counts

# Step 6: Create a bar chart
plt.figure(figsize=(10, 6))  # Set the figure size
plt.bar(labels, values, color='skyblue')  # Create the bar chart
plt.xlabel("Vehicle Categories")  # Label for the x-axis
plt.ylabel("Number of Vehicles")  # Label for the y-axis
plt.title("Distribution of Vehicles by Category")  # Chart title
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout for better spacing
plt.show()  # Display the chart