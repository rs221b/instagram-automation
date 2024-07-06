import instaloader

def download_followers_list(l):
    target_profile = input("Enter target profile username: ")
    profile = instaloader.Profile.from_username(l.context, target_profile)

    with open(f"{target_profile}_followers.txt", "w") as file:
        for follower in profile.get_followers():
            file.write(f"{follower.username}\n")

    print(f"Followers list of {target_profile} has been saved to {target_profile}_followers.txt")
