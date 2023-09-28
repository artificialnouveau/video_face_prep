
# YouTube Video Downloader

This script allows you to download videos and their audio from YouTube using two different methods: `youtube-dl` or `pytube`.

## Prerequisites

You will need the following libraries and tools:

- youtube-dl (if you choose to use the youtube-dl method)
- pytube
- ffmpeg (for audio conversion)

You can install the required Python libraries using pip:

```bash
pip install pytube
```

For `youtube-dl` and `ffmpeg`, you can download and install them from their respective websites or use package managers like `apt`, `brew`, etc.

## Usage

1. **From Python script**

   You can run the code within Python by uncommenting the relevant section and specifying the YouTube link:

   ```python
   video_path, audio_path = download_youtube_video_pytube("https://www.youtube.com/watch?v=ID")
   ```

   Replace `download_youtube_video_pytube` with `download_youtube_video_dl` if you wish to use the youtube-dl method.

2. **From Terminal**

   You can run the script directly from the terminal. Ensure the script name is `download_youtube.py`:

   ```bash
   python download_youtube.py <youtube_link>
   ```

   This will print the paths to the downloaded video and audio.

## How It Works

1. The script allows for two methods to download YouTube videos:
   - Using `youtube-dl`
   - Using `pytube`

2. For each method, the video is downloaded in its highest resolution available in `.mp4` format.

3. Audio from the video is extracted, and then converted and saved in `.wav` format using `ffmpeg`.

4. Special characters in video titles are removed to create sanitized filenames.


# Face Extraction from Videos

This script allows you to extract and save faces from videos, either from a single video or from all videos within a specified directory.

## Prerequisites

You will need the following libraries:

- OpenCV
- NumPy
- face_recognition
- mtcnn
- tqdm

You can install these using pip:

```bash
pip install opencv-python numpy face_recognition mtcnn tqdm
```

## Usage

1. **For Single Video**

   To process a single video, you can use the `find_and_collate_faces()` function. Uncomment the corresponding section in the script and specify your `video_path` and `output_folder`:

   ```python
   video_path = "path_to_input_video_file"
   output_folder = "path_to_output_directory"
   find_and_collate_faces(video_path, output_folder)
   ```

2. **For All Videos in a Directory**

   If you want to process all the `.mp4` videos in a directory, use the `process_all_videos_in_folder()` function. Specify the `input_folder` containing your videos and the `output_folder` where you want to save the extracted faces:

   ```python
   input_folder = 'path_to_input_directory'
   output_folder = 'path_to_output_directory'
   process_all_videos_in_folder(input_folder, output_folder)
   ```

   Then, run the script.

## How It Works

1. The script uses the `MTCNN` detector to detect faces in the video frames.
2. The detected faces are then encoded using `face_recognition`.
3. For each unique face detected, a new video is saved containing only frames where that face appears. The output videos are named based on the original video name with an additional "_person_{idx}" suffix to distinguish between different faces.

## Notes

- Ensure that the paths you provide are correctly pointing to existing directories or files.
- Ensure you have sufficient storage as extracting faces from long videos may generate substantial data.
- The script is set up to process every 10th frame by default (`N=10`). You can adjust `N` if you want to process frames at a different interval.
