import cv2
import os
import imageio
import numpy as np
from config import generate_random_filename

def crop_center(frame, size):
    height, width, _ = frame.shape
    if width > height:
        cropped = frame[:, (width - height) // 2:(width + height) // 2]
    else:
        cropped = frame[(height - width) // 2:(height + width) // 2, :]
    return cv2.resize(cropped, size)

def adjust_video_parameters(video, target_duration=3.0, target_fps=30):
    original_fps = int(video.get(cv2.CAP_PROP_FPS))
    original_duration = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) / original_fps
    frame_count = int(target_duration * target_fps)

    if original_duration <= target_duration and original_fps <= target_fps:
        return video, original_duration, original_fps

    return video, original_duration, original_fps

def animated_sticker(src_folder, result_folder, sticker_size=(512, 512), target_duration=3.0, target_fps=15):
    input_files = [os.path.join(src_folder, f) for f in os.listdir(src_folder) if f.lower().endswith(('.webm', '.mp4', '.avi', '.mkv', '.gif'))]
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    for file in input_files:
        try:
            output_file = os.path.join(result_folder, generate_random_filename() + '.webm')
            writer = imageio.get_writer(output_file, format='webm', codec='vp9', fps=target_fps)
            print(f"Processing: {file}")
            video = cv2.VideoCapture(file)

            video, original_duration, original_fps = adjust_video_parameters(video, target_duration=target_duration, target_fps=target_fps)

            frame_count = int(target_duration * target_fps)

            for i in range(frame_count):
                frame_num = int((i / frame_count) * original_duration)
                ret, frame = video.read()
                if not ret:
                    break
                frame = crop_center(frame, sticker_size)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                writer.append_data(frame)

            writer.close()
            print(f"Processed: {file}")
        except Exception as e:
            print(f"Error processing {file}: {str(e)}")
            continue






