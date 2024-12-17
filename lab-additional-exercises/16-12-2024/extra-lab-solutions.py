# Import required packages
import csv
import json
import random


# Define the file path
filepath = 'your_path_to/netflix_titles.csv'


### This function is just to handle some errors in the file, ignore it and proceed with the steps

# def clean_netflix_dataset(input_filepath, output_filepath=None):
#     """
#     Cleans the Netflix dataset by fixing common issues and writes to a new file.
    
#     Args:
#         input_filepath (str): Path to the original netflix_titles.csv file
#         output_filepath (str): Path for the cleaned file. If None, will append '_cleaned' to original
#     """
#     if output_filepath is None:
#         output_filepath = input_filepath.replace('.csv', '_cleaned.csv')
    
#     # Read all lines first
#     with open(input_filepath, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
    
#     # Get header
#     header = lines[0]
    
#     # Initialize cleaned lines with header
#     cleaned_lines = [header]
    
#     i = 1
#     while i < len(lines):
#         line = lines[i].strip()
        
#         # Skip empty lines
#         if not line:
#             i += 1
#             continue
            
#         # Check if this line needs to be combined with the next one
#         # (specifically for the Memphis Belle case)
#         if 'Memphis Belle: A Story of a' in line:
#             next_line = lines[i + 1].strip()
#             line = line + ' ' + next_line
#             i += 2
#         # Skip the problematic fragment
#         elif line == 'and probably will."':
#             i += 1
#             continue
#         else:
#             # Verify this is a complete record by counting commas and quotes
#             quote_count = line.count('"')
#             if quote_count % 2 == 0 and line.count(',') == 11:  # We expect 11 commas for 12 fields
#                 cleaned_lines.append(line + '\n')
#             i += 1
    
#     # Write cleaned data
#     with open(output_filepath, 'w', encoding='utf-8', newline='') as file:
#         file.writelines(cleaned_lines)
    
#     print(f"Cleaned file written to: {output_filepath}")
#     print(f"Original line count: {len(lines)}")
#     print(f"Cleaned line count: {len(cleaned_lines)}")
    
#     # Verify the cleaned file
#     with open(output_filepath, 'r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         record_count = sum(1 for _ in reader)
#         print(f"Number of records in cleaned file: {record_count}")
    
#     return output_filepath

# # Usage example
# filepath = clean_netflix_dataset(filepath)


def open_dataset(filepath):
    """
    Opens the Netflix dataset and returns a file object.
    Args:
        filepath (str): Path to the netflix_titles.csv file
    Returns:
        file object: File object for reading the dataset
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file

def print_first_line(filepath):
    """
    Reads and prints the first line of the dataset (headers). 
    Args:
        filepath (str): Path to the netflix_titles.csv file
    Returns:
        str: First line of the file (headers)
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        first_line = file.readline().strip()
        print(f"Headers: {first_line}")
        return first_line

def count_lines(filepath):
    """
    Counts total number of non-empty lines in the dataset.
    Args:
        filepath (str): Path to the netflix_titles.csv file
    Returns:
        int: Total number of non-empty lines including header
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        line_count = sum(1 for line in file if line.strip()) # as I was mentioning during the lab, this is the most efficient way to count, not storing lines in memory
        print(f"Total lines in file: {line_count}")
        return line_count

def create_show_dictionaries(filepath):
    """
    Creates a list of dictionaries from the dataset where each dictionary
    represents one show/movie.
    Args:
        filepath (str): Path to the netflix_titles.csv file
    Returns:
        list: List of dictionaries containing show information
    """
    shows = []
    with open(filepath, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file) # refer to lesson 6, exercise 2, for this method
        for row in csv_reader:
            shows.append(row)
    print(f"Created {len(shows)} show dictionaries")
    return shows

### This function is returning a line mismatch due to problems in the original file, don't worry, proceed simply being aware that there is a count mismatch
def verify_line_count(total_lines, shows):
    """
    Verifies that the number of dictionaries matches the number of data lines.
    Args:
        total_lines (int): Total number of lines in file (including header)
        shows (list): List of show dictionaries
    Returns:
        bool: True if counts match, False otherwise
    """
    if len(shows) == total_lines - 1:  # Subtract 1 for header
        print("✓ Line count verification successful!")
        return True
    else:
        print("✗ Line count mismatch!")
        print(f"Total lines (minus header): {total_lines - 1}")
        print(f"Number of show dictionaries: {len(shows)}")
        return False

def get_unique_genres(shows):
    """
    Gets all unique genres from the dataset.
    Args:
        shows (list): List of show dictionaries
    Returns:
        set: Set of unique genres
    """
    genres = set()
    for show in shows:
        # Split genres and strip whitespace
        show_genres = [genre.strip() for genre in show['listed_in'].split(',')]
        genres.update(show_genres)
    return genres

def create_genre_clusters():
    """
    Creates predefined genre clusters for recommendation.
    Returns:
        dict: Dictionary of genre clusters
    """
    return {
        "Nightmares_and_spooky": ["TV Horror", "Thrillers", "Crime TV Shows"],
        "Family_friendly": ["Kids' TV", "Family Movies", "Children & Family Movies"],
        "Learning_time": ["Documentaries", "Science & Nature TV", "Docuseries"],
        "International": ["International Movies", "International TV Shows", "Korean TV Shows", "Anime Features"]
    }

def recommend_similar_show(show, shows, genre_clusters):
    """
    Recommends a similar show based on genre clusters.
    Args:
        show (dict): Current show dictionary
        shows (list): List of all show dictionaries
        genre_clusters (dict): Dictionary of genre clusters  
    Returns:
        str: Title of recommended show or None if no recommendation found
    """
    current_genres = show['listed_in'].split(',')
    current_genres = [genre.strip() for genre in current_genres]
    
    # Find matching cluster
    matching_cluster = None
    for cluster, genres in genre_clusters.items():
        # I get that this can be confusing, the next lines means: considering each cell of the "listed_in" column, splitting the string at ", " and considering each item
        # retrieved in this way, for each of them check if there is a match with the elements in "matching_cluster", if so: stop searching
        if any(genre in genres for genre in current_genres): 
            matching_cluster = genres # this is a simplified version of a recommender system, because it prefers every time the first match, without considering other factors
            break 
    
    if matching_cluster:
        # Find all shows in the same cluster
        similar_shows = [
            s['title'] for s in shows 
            if s['title'] != show['title'] and 
            any(genre.strip() in matching_cluster 
                for genre in s['listed_in'].split(','))
        ]
        
        if similar_shows:
            return random.choice(similar_shows)
    
    return None



# Open dataset
file = open_dataset(filepath)

# Read and print first line
first_line = print_first_line(filepath)

# Count lines
total_lines = count_lines(filepath)

# Create dictionaries
shows = create_show_dictionaries(filepath)

# Verify line count
verification_result = verify_line_count(total_lines, shows)

# Get unique genres and create recommendations
unique_genres = get_unique_genres(shows)
print("Unique genres:", unique_genres)

# Create genre clusters
genre_clusters = create_genre_clusters()
print("Genre clusters:", json.dumps(genre_clusters, indent=2))

# Get a recommendation for the first show as an example
recommendation = recommend_similar_show(shows[0], shows, genre_clusters)
print(f"For show '{shows[0]['title']}', we recommend: {recommendation}") # here you can specify on which line you are operating, changing the index between squared brackets
