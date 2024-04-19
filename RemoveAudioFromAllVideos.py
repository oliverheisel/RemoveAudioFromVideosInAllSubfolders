import os
import shutil
from moviepy.editor import VideoFileClip

# Define the base directory containing the videos
## Change it to your base directory!
base_dir = "Your Path here!" 


def process_videos(directory):
    """Process videos by removing sound, converting to MP4, and deleting the original."""
    video_count = 0  # Initialize counter for processed videos
    found_files = False  # Flag to check if there are any eligible files

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith('WOA_') or file.startswith('WA_'):
                continue  # Skip files already processed or marked to be ignored

            found_files = True  # Set the flag as true when eligible files are found
            full_path = os.path.join(subdir, file)
            filename, ext = os.path.splitext(file)
            if ext.lower() in ['.mp4', '.avi', '.mov', '.mkv']:  # Add or remove formats as needed
                # Process the video
                clip = VideoFileClip(full_path)
                clip = clip.without_audio()
                # Define new filename and save
                new_filename = f"WOA_{filename}.mp4"
                new_full_path = os.path.join(subdir, new_filename)
                clip.write_videofile(new_full_path, codec='libx264')
                clip.close()
                print(f"Processed {full_path} and saved as {new_full_path}")

                # Delete the original file after successful conversion
                os.remove(full_path)
                print(f"Deleted original file: {full_path}")

                video_count += 1  # Increment the counter for each processed video

    if video_count == 0:
        print("No eligible video files found for processing.")
    else:
        print(f"Total videos processed: {video_count}")


if __name__ == "__main__":
    process_videos(base_dir)
