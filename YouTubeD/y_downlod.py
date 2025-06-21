# from pytube import YouTube

# def download_video(url):
#     try:
#         yt = YouTube(url)
#         print(f"\n🎬 Title       : {yt.title}")
#         print(f"📺 Channel     : {yt.author}")
#         print(f"⏱️ Duration    : {yt.length // 60} min {yt.length % 60} sec")
#         print(f"👁️ Views       : {yt.views}")
#         print(f"📅 Published on: {yt.publish_date.date()}")

#         stream = yt.streams.get_highest_resolution()
#         print(f"\n⬇️ Downloading: {stream.resolution} - {stream.mime_type}...\n")
#         stream.download()
#         print("✅ Download completed!\n")

#     except Exception as e:
#         print(f"❌ Error: {e}")

# if __name__ == "__main__":
#     video_url = input("🔗 Enter YouTube Video URL: ")
#     download_video(video_url)
