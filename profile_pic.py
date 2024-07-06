import instaloader

def download_profile_pic(l):
    target_profile = input("Enter target profile username: ")
    profile = instaloader.Profile.from_username(l.context, target_profile)

    l.download_profilepic(profile)
    print(f"Profile picture of {target_profile} has been downloaded.")
