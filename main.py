import getpass
import pickle
import engagement
import login_module as login
import logout
import followers
import posts
import profile_pic

CREDENTIALS_FILE = "credentials.pkl"

def save_credentials(username, password):
    with open(CREDENTIALS_FILE, "wb") as file:
        pickle.dump((username, password), file)

def load_credentials():
    try:
        with open(CREDENTIALS_FILE, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None, None

def main():
    username, password = load_credentials()
    l = None
    if not username or not password:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        save_credentials(username, password)
        l = login.login(username, password)
    else:
        l = login.login(username, password)

    if not l:
        print("Failed to login. Exiting.")
        return

    while True:
        print("Options:")
        print("1. Calculate Engagement Score")
        print("2. Download Followers List")
        print("3. Download Specific Post or Reel by URL")
        print("4. Download Profile Picture")
        print("5. Logout")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            engagement.calculate_engagement(l)
        elif choice == "2":
            followers.download_followers_list(l)
        elif choice == "3":
            posts.download_post_by_url(l)
        elif choice == "4":
            profile_pic.download_profile_pic(l)
        elif choice == "5":
            logout.logout()
            break
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
