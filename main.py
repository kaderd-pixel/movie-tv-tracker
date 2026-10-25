
from tracker import (load_watchlist, add_title, view_watchlist, mark_as_watched)


def display_menu():
    print("\n=== Movie & TV Show Tracker ===")
    print("1. Add a movie or TV show")
    print("2. View my watchlist")
    print("3. Mark a title as watched")
    print("4. Rate a title")
    print("5. Exit")


def main():
    watchlist = load_watchlist()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_title(watchlist)
        elif choice == "2":
            view_watchlist(watchlist)
        elif choice == "3":
            mark_as_watched(watchlist)
        elif choice == "4":
            print("Rating feature coming soon!")
        elif choice == "5":
            print("Thanks for using the tracker!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
