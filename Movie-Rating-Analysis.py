import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Movie": [
        "Inception", "Interstellar", "Avatar",
        "Titanic", "Jawan", "3 Idiots",
        "Dangal", "Bahubali"
    ],
    "Genre": [
        "Sci-Fi", "Sci-Fi", "Action",
        "Romance", "Action", "Comedy",
        "Drama", "Action"
    ],
    "Rating": [
        8.8, 8.7, 7.8,
        7.9, 7.2, 8.4,
        8.3, 8.2
    ],
    "Votes": [
        2200000, 1800000, 1400000,
        1200000, 450000, 850000,
        650000, 900000
    ],
    "Collection_Crore": [
        830, 730, 2900,
        2200, 1150, 460,
        2000, 1800
    ]
}

df = pd.DataFrame(data)

print("Movie Rating Analysis")
print(df)

print("\nHead")
print(df.head())

print("\nTail")
print(df.tail())

print("\nInfo")
df.info()

print("\nDescribe")
print(df.describe())

Highest_Rated_Movie = df["Rating"].max()
print("\nHighest Rated Movie:", Highest_Rated_Movie)

Lowest_Rated_Movie = df["Rating"].min()
print("\nLowest Rated Movie:", Lowest_Rated_Movie)

Movie_Highest_Collection = df.loc[df["Collection_Crore"].idxmax()]
print("\nMovie with Highest Collection")
print(Movie_Highest_Collection)

Movie_Lowest_Collection = df.loc[df["Collection_Crore"].idxmin()]
print("\nMovie with Lowest Collection")
print(Movie_Lowest_Collection)

High_Rating = df[df["Rating"] > 8]
print("\nMovies with Rating > 8")
print(High_Rating)

Action_Movies = df[df["Genre"] == "Action"]
print("\nAction Movies")
print(Action_Movies)

Total_Collection = df.groupby("Genre")["Collection_Crore"].sum()
print("\nGenre Wise Total Collection")
print(Total_Collection)

Average_Rating = df.groupby("Genre")["Rating"].mean()
print("\nGenre Wise Average Rating")
print(Average_Rating)

Total_Movies = df["Genre"].value_counts()
print("\nNumber of Movies in Each Genre")
print(Total_Movies)

df["Tax"] = df["Collection_Crore"] * 0.05

df["Net Collection"] = df["Collection_Crore"] - df["Tax"]

df["Percentage Contribution"] = (
    df["Net Collection"] / df["Net Collection"].sum()
) * 100

print("\nPercentage Contribution")
print(df[["Movie", "Percentage Contribution"]])

df = df.sort_values("Net Collection", ascending=False)

print("\nSorted Data")
print(df)

Good_Movies = df[
    (df["Rating"] > 8) &
    (df["Votes"] > 800000)
]

print("\nMovies with Rating > 8 and Votes > 800000")
print(Good_Movies)

plt.bar(df["Movie"], df["Net Collection"])
plt.title("Movie VS Net Collection")
plt.xlabel("Movie")
plt.ylabel("Net Collection")
plt.show()

Genre_Collection = df.groupby("Genre")["Net Collection"].sum()

plt.bar(Genre_Collection.index, Genre_Collection.values)
plt.title("Genre VS Net Collection")
plt.xlabel("Genre")
plt.ylabel("Net Collection")
plt.show()