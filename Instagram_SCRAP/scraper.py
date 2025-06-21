# import instaloader

# def fetch_instagram_profile(username):
#     loader = instaloader.Instaloader()
#     try:
#         profile = instaloader.Profile.from_username(loader.context, username)
#         print(f"\n📄 Profile: {profile.username}")
#         print(f"Full Name   : {profile.full_name}")
#         print(f"Bio         : {profile.biography}")
#         print(f"Posts       : {profile.mediacount}")
#         print(f"Followers   : {profile.followers}")
#         print(f"Following   : {profile.followees}")
#         print(f"Profile Pic : {profile.profile_pic_url}\n")
#     except Exception as e:
#         print(f"❌ Error fetching profile: {e}")

# if __name__ == '__main__':
#     user = input("Enter Instagram username: ")
#     fetch_instagram_profile(user)
