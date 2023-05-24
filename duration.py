from pytube import YouTube

def get_video_duration(video_url):
    try:
        yt = YouTube(video_url)
        duration = yt.length
        return duration
    except Exception as e:
        print("An error occurred:", str(e))
        return None

video_link = input("Enter the YouTube video link, please: ")
duration = get_video_duration(video_link)
if duration:
    print(f"The duration of the video is {duration} seconds.")
else:
    print("Unable to retrieve video duration.")