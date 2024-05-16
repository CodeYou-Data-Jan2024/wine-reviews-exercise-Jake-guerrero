# add your code here

import pandas as pd

reviews = pd.read_csv('winemag-data-130k-v2.csv')
mean_points = reviews.groupby('country')['points'].mean().apply(lambda point: round(point, 1))
countries_reviewed = reviews.value_counts('country')
new_df = (countries_reviewed, mean_points)
results = pd.concat(new_df, axis = 1)
results.to_csv('reviews-per-country.csv')
print(results)