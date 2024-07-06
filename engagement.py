import instaloader

def calculate_engagement(l):
    target_profile = input("Enter target profile username: ")
    profile = instaloader.Profile.from_username(l.context, target_profile)

    num_followers = profile.followers
    total_num_likes = 0
    total_num_comments = 0
    total_number_posts = 0

    for post in profile.get_posts():
        total_num_likes += post.likes
        total_num_comments += post.comments
        total_number_posts += 1

    if total_number_posts > 0:
        engagement = float(total_num_likes + total_num_comments) / (num_followers * total_number_posts)
        print(f"Engagement Score: {engagement * 100:.2f}%")
    else:
        print("No posts found.")
