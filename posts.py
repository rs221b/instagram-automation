import instaloader
import re

def download_post_by_url(l):
    post_url = input("Enter the URL of the post or reel: ")
    
    # Extract shortcode from URL (supporting both post and reel)
    match = re.search(r'(?:https?://www\.instagram\.com)?/(p|reel)/([^/?#&]+)', post_url)
    if not match:
        print("Invalid URL. Please enter a valid post or reel URL.")
        return
    
    shortcode = match.group(2)

    try:
        post = instaloader.Post.from_shortcode(l.context, shortcode)
        l.download_post(post, target=post.owner_username)
        print(f"Post from {post_url} has been downloaded.")
    except Exception as e:
        print(f"An error occurred: {e}")
