import os

def logout():
    credentials_file = "credentials.pkl"
    if os.path.exists(credentials_file):
        os.remove(credentials_file)
        print("Logged out successfully.")
    else:
        print("No user is currently logged in.")
