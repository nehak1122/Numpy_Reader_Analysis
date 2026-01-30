import numpy as np
import sys

# Redirect stdout to a file
with open('final_output.txt', 'w', encoding='utf-8') as f:
    sys.stdout = f
    
    print("--- 1. Data Loading ---")
    # Load the dataset
    try:
        data = np.genfromtxt('world-happiness-report-2021.csv', delimiter=',', dtype=None, names=True, encoding='utf-8-sig')
        # Display the column names
        print("Column names:")
        print(data.dtype.names)
    except Exception as e:
        print(f"Error loading data: {e}")
        exit(1)

    print("\n--- 2. Basic Statistics ---")
    try:
        ladder_scores = data['Ladder_score']

        mean_score = np.mean(ladder_scores)
        median_score = np.median(ladder_scores)
        std_score = np.std(ladder_scores)

        print(f"Mean Ladder Score: {mean_score:.3f}")
        print(f"Median Ladder Score: {median_score:.3f}")
        print(f"Standard Deviation: {std_score:.3f}")
    except Exception as e:
        print(f"Error in statistics: {e}")

    print("\n--- 3. Top and Bottom Countries ---")
    try:
        # Sort the data by Ladder score in descending order
        sorted_indices = np.argsort(data['Ladder_score'])[::-1]
        sorted_data = data[sorted_indices]

        top_10 = sorted_data[:10]
        bottom_10 = sorted_data[-10:]

        print("Top 10 Happiest Countries:")
        for i, country in enumerate(top_10):
            print(f"{i+1}. {country['Country_name']} ({country['Ladder_score']:.3f})")

        print("\nBottom 10 Least Happy Countries:")
        for i, country in enumerate(bottom_10):
            print(f"{len(data) - 9 + i}. {country['Country_name']} ({country['Ladder_score']:.3f})")
    except Exception as e:
        print(f"Error in rankings: {e}")

    print("\n--- 4. Regional Analysis ---")
    try:
        regions = np.unique(data['Regional_indicator'])

        print("Average Happiness Score by Region:")
        region_scores = []
        for region in regions:
            # Filter data for the current region
            region_mask = data['Regional_indicator'] == region
            region_data = data[region_mask]
            avg_score = np.mean(region_data['Ladder_score'])
            region_scores.append((region, avg_score))

        # Sort regions by score
        region_scores.sort(key=lambda x: x[1], reverse=True)

        for region, score in region_scores:
            print(f"{region}: {score:.3f}")
    except Exception as e:
        print(f"Error in regional analysis: {e}")

    print("\n--- 5. Correlations ---")
    try:
        factors = [
            'Logged_GDP_per_capita',
            'Social_support',
            'Healthy_life_expectancy',
            'Freedom_to_make_life_choices',
            'Generosity',
            'Perceptions_of_corruption'
        ]

        print("Correlation with Ladder Score:")
        for factor in factors:
            # Check if column exists (handling potential naming mismatches if any)
            if factor in data.dtype.names:
                correlation = np.corrcoef(data['Ladder_score'], data[factor])[0, 1]
                print(f"{factor}: {correlation:.3f}")
            else:
                print(f"Warning: Column '{factor}' not found in data.")
    except Exception as e:
        print(f"Error in correlations: {e}")

sys.stdout = sys.__stdout__ # Reset stdout
