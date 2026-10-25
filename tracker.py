
import json
import os

FILE_NAME = "watchlist.json"


def load_watchlist():
    """Load saved titles from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as file:
        return json.load(file)



def save_watchlist(watchlist):
    """Save titles to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(watchlist, file, indent=4)



def add_title(watchlist):
    """Ask the user for a title and save it."""
    title = input("Enter the movie or TV show title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    print("1. Movie")
    print("2. TV Show")
    choice = input("Choose the type: ").strip()

    if choice == "1":
        title_type = "Movie"
    elif choice == "2":
        title_type = "TV Show"
    else:
        print("Invalid choice. Title was not added.")
        return

    new_title = {
        "title": title,
        "type": title_type,
        "watched": False
    }

    watchlist.append(new_title)
    save_watchlist(watchlist)

    print(f"{title} was added to your watchlist!")


def view_watchlist(watchlist):
    """Display all movies and TV shows in the watchlist."""
    if not watchlist:
        return
    
    print("\n=== My Watchlist ===")

    for index, item in enumerate(watchlist, start=1):
        if item.get("Watched", False):
            status = "Watched"
        else:
            status = "Not Watched"

        print(
            f"{index}. {item['title']} ({item['type']}) - {status}"
        )

def mark_as_watched(watchlist):
    """Mark as movie or TV show as watched."""

    if not watchlist:
        print("\nYour watchlist is empty.")
        return
    view_watchlist(watchlist)

    choice = input(
        "\nEnter the number of the title you watched: "
    ).strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(watchlist):
        print("That number is not on your watchlist.")
        return

    watchlist[index]["watched"] = True
    save_watchlist(watchlist)

    print(
        f"{watchlist[index]['title']} "
        "has been marked as watched!"
    )
