# # -*- coding: utf-8 -*-
# """
# Created on Wed Jan 31 22:49:00 2024

# @author: Francisca Thimothy
# """



# import pandas as df
# import matplotlib.pyplot as plt
# # file =pandas.read_csv("movie_dataset.csv")


# # plt.bar(file["Title"], file["Rank"])
# # plt.xlabel("Title")
# # plt.ylabel("Rank")
# # plt.show()

# df = df.read_csv("movie_dataset.csv", index_col=0)
# print(df.info())

# plt.scatter(df["Title"], df["Rating"])
# plt.xlabel("Title")
# plt.ylabel("Rating")
# plt.show()

# # import seaborn as sns
# # sns.pairplot(file, hue="Genre")
# # plt.show()





 

# import pandas as pd
# import matplotlib.pyplot as plt

# def plot_highest_ranking_movie(input_file):
#     # Load the CSV file into a DataFrame
#     df = pd.read_csv(input_file)

#     # Assuming you have a column named 'Ranking' for movie rankings
#     # You can change 'Ranking' to the actual column name in your dataset
#     highest_ranking_movie = df.loc[df['Rank'].idxmax()]

#     # Plotting the highest-ranking movie
#     plt.bar(df['Title'], df['Rank'])
#     plt.xlabel('Rank')
#     plt.title('Highest Ranking Movie')
#     plt.show()

# if __name__ == "__main__":
#     input_file_path = "C:/Users/Francisca Thimothy/CSS2024_Day03/movie_dataset.csv"  # Replace with your movie dataset CSV file path

#     plot_highest_ranking_movie("C:/Users/Francisca Thimothy/CSS2024_Day03/movie_dataset.csv")


# import pandas as pd
# import matplotlib.pyplot as plt

# #def ("C:/Users/Francisca Thimothy/CSS2024_Day03/movie_dataset.csv")
#     # Load the CSV file into a DataFrame
#     df = pd.read_csv('movie_dataset.csv')
 
#     # Filter the DataFrame based on selected movies
#     selected_df = df[df['Title'].isin()]

#     # Plotting the selected movies
#     plt.barh(selected_df['Title'], selected_df['Rank'])
#     plt.xlabel('Ranking')
#     plt.title('Rankings of Selected Movies')
#     plt.show()

# if __name__ == "__main__":
#     input_file_path = "C:/Users/Francisca Thimothy/CSS2024_Day03/movie_dataset.csv"  # Replace with your movie dataset CSV file path

#     # Replace with the names of the movies you want to plot
#     movies_to_plot = ['Jason Bourne', 'The Dark Knight', 'Rogue One', 'Trolls']

#     plot_selected_movies("C:/Users/Francisca Thimothy/CSS2024_Day03/movie_dataset.csv")







import pandas as pd
import matplotlib.pyplot as plt






# #def plot_selected_movies("movie_dataset.csv")
# df = pd.read_csv('C:/Users/Francisca Thimothy/CSS2024_Day03/movie_dataset.csv')
# movies_to_plot = ["Jason", "Bourne", "The_Dark_Knight", "Rogue_One", "Trolls"]
# df = df[df['Title'].isin(movies_to_plot)]
# #df = df[df['Title'].isin("Jason", "Bourne", "The_Dark_Knight", "Rogue_One", "Trolls")]
    
# df.plot(kind='barh', x='Title', y='Rank', legend=False)
# plt.xlabel('Rank')
# plt.title('Rankings of Selected Movies')
# plt.show()

# if __name__ == "__main__":
#   input_file_path = "C:/Users/Francisca Thimothy/CSS2024_Day03/movie_dataset.csv"  # Replace with your movie dataset CSV file path
#   movies_to_plot = ['Jason Bourne', 'The Dark Knight', 'Rogue One', 'Trolls']

# #plot_selected_movies('movie_dataset.csv', movies_to_plot)
# print(df.columns)

file = pd.read_csv('C:/Users/Francisca Thimothy/CSS2024_Day03/movie_dataset.csv')

average_revenue =file['Revenue (Millions)'].dropna().mean()
#average_revenue = df['Revenue (Millions)'].mean()
average_revenue_2015_2017 = file[(file['Year'] >= 2015) & (file['Year'] <= 2017)]['Revenue (Millions)'].mean()

average_revenue_2015_to_2017 = file[(file['Year'] >= 2015) & (file['Year'] <= 2017)]['Revenue (Millions)'].dropna().mean()




movies_released_2016 = file[file['Year'] == 2016].shape[0]

#movies_released_2016 = file[file['Year'].eq(2016) & file['Year'].notna()].shape[0]

#movies_released_2016 = file[file['Year'].astype(str).str[:4] == '2016'].shape[0]



df = pd.read_csv("C:/Users/Francisca Thimothy/CSS2024_Day03/movie_dataset.csv")
movies_by_nolan = df[df['Director'] == 'Christopher Nolan'].shape[0]
movies_released_2016 = df[df['Year'] == 2016].shape[0]
highly_rated_movies = df[df['Rating'] >= 8.0].shape[0]

median_rating_nolan = df[df['Director'] == 'Christopher Nolan']['Rating'].median()


highest_avg_rating_year = df.groupby('Year')['Rating'].mean().idxmax()


# movies_2006 = df[df['Year'] == 2006].shape[0]
# movies_2016 = df[df['Year'] == 2016].shape[0]

# percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]

percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100


from collections import Counter

# Assuming 'Actors' is the column containing multiple actor names separated by commas
#all_actors = df['Actors'].str.split(',').explode().str.strip()
#most_common_actor = Counter(all_actors).most_common(1)[0][0]




#from collections import Counter

# Assuming 'Actors' is the column containing multiple actor names separated by commas
if isinstance(df['Actors'][0], str):
    Actors = df['Actors'].str.split(',').explode().str.strip()
else:
    Actors = df['Actors'].explode()

most_common_actor = Counter('Actors').most_common(1)[0][0]

# Assuming 'Genre' is the column containing multiple genres per movie
all_genres = df['Genre'].str.split(',').explode().str.strip()
unique_genres_count = all_genres.nunique()

# Assuming numerical features like 'Rating', 'Revenue', 'Budget', 'Runtime' are present in the dataset
numerical_features = df[['Rank', 'Year',
       'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)',
       'Metascore']]

correlation_matrix = numerical_features.corr()
print(correlation_matrix)

#print(df.columns)




import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'Rating', 'Revenue', 'Budget', 'Runtime' are numerical features
numerical_features = df[['Rank', 'Year',
       'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)',
       'Metascore']]

# Calculate the correlation matrix
correlation_matrix = numerical_features.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()

































