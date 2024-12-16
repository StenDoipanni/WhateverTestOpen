# Netflix Shows Dataset Analysis Exercise

## Dataset Description

We'll be working with the Netflix Shows dataset, which contains information about movies and TV shows available on Netflix as of 2019. The dataset is available at:
[Netflix Shows Dataset](https://github.com/comp-think/comp-think.github.io/blob/master/laboratory/data/netflix_titles.csv)

The CSV file contains the following columns:
- `show_id`: Unique ID for every movie/TV show
- `type`: Type of content (Movie or TV Show)
- `title`: Title of the content
- `director`: Director(s) of the content
- `cast`: Actors involved
- `country`: Country of production
- `date_added`: Date when added on Netflix
- `release_year`: Original release year
- `rating`: TV Rating (e.g., TV-MA, PG-13)
- `duration`: Length (minutes for movies, seasons for TV shows)
- `listed_in`: Categories/Genres
- `description`: Brief synopsis

## Exercise Objective

Test step by step with incremental difficulty your abilities acquired during the course.

## Required Steps

### Step 1: Project Creation
Create a new project with the appropriate directory structure.

💡 **Hint**: Give the project a meaningful name.

### Step 2: Basic Project Structure
Set up the main script and create necessary folders.

💡 **Hint**: Remember to create a dedicated folder for your `data`, as well as relevant python scripts (check [last lab lesson](https://comp-think.github.io/laboratory/site/chapter/06/) if you don't remember).

### Step 3: Package Import
Import the required Python packages to handle CSV and JSON data.

💡 **Hint**: Which packages do you need for reading CSV files and working with JSON objects?

### Step 4: Dataset Opening
Create code to open and access the Netflix dataset.

💡 **Hint**: Remember that it is useful to handle potential file errors and encoding issues.

### Step 5: First Line Reading
Write code to read and display the first line of the dataset.

💡 **Hint**: The first line contains important information about your data structure.

### Step 6: Line Counting
Implement functionality to count the total number of lines in the file.

💡 **Hint**: This can be done in several ways, but try to consider the most efficient way to count lines in a large file.

### Step 7: Dictionary Creation
Transform each line of the dataset into a dictionary.

💡 **Hint**: The dictionary keys should match your column names.

### Step 8: Data Verification
Compare the number of created dictionaries with the line count.

💡 **Hint**: Remember to account for the header row in your calculations.


### Step 9 - Let's play with some real semantics
In the column `listed_in` you have all the genres with which Netflix classifies its shows.
1. Find all the unique genres used by Netflix.
2. Manually analyse them, and create (at least) one dictionary that works as guidance for a `recommender system`. A recommender system is a tool designed to propose to a user a certain piece of content "related to" something that the user liked.
3. Define a function that, for each line of the file, checks the genre(s) in the `listed_in` column, and if the entry is in your dictionary, it returns the title of another different random show that is in the same cluster that you have defined.

The expected output structure should be something like this:
```
{
    "Name of Genre Cluster": ["related_genre_1", "related_genre_2"]
}

e.g.

{
    "Nightmares_and_spooky": ["TV Horror", "Thrillers", "Crime TV Shows"]
}
```


💡 **Hint**: To get the list of unique genres it could turn useful the difference between lists and sets.
1. Manually design the structure of at least one dictionary.
2. Use tha package `random` to randomize the show recommended.


-------------------------------------------------------------------------------------

## Project Structure

Your final project should look like this:
```
netflix_analysis/
├── main.py
└── data/
    └── netflix_titles.csv
```

## Requirements

- Python 3.x
- CSV file handling knowledge
- Basic understanding of dictionaries
- Error handling experience
- Testing function

## Getting Started

1. Download the Netflix dataset from the provided link and place it in the `data` folder
2. Follow the steps above to complete the exercise


## Notes

- All code should be well-documented
- Use appropriate Python naming conventions
- Bonus: Include error handling for file operations

Solutions will be provided separately after completion of the exercise.