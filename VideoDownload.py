from pytube import YouTube

# Ask user for the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object
yt = YouTube(url)

# Get the available video streams (including adaptive streams)
streams = yt.streams.filter(progressive=False)

# Print the available video quality options
print("Available video quality options:")
for i in range(len(streams)):
    print(f"{i+1}. {streams[i].resolution}")

# Ask user to choose the video quality
choice = int(input("Enter the number of the desired video quality: "))

# Get the selected video stream
stream = streams[choice-1]

# Ask user for the destination folder
destination_folder = input("Enter the destination folder path: ")

# Download the video to the specified folder
stream.download(output_path=destination_folder)