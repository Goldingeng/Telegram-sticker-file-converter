import cv2
import os
import imageio
import numpy as np
import uuid

def generate_random_filename():
    return str(uuid.uuid4())[:8]

def animated_sticker(src_folder, result_folder, sticker_size=(512, 512), target_duration=3.0):
    input_files = [os.path.join(src_folder, f) for f in os.listdir(src_folder) if f.lower().endswith(('.webm', '.mp4', '.avi', '.mkv', '.gif'))]
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    
    for file in input_files:
        output_file = os.path.join(result_folder, generate_random_filename() + '.webm')
        writer = imageio.get_writer(output_file, format='webm', codec='vp9', fps=30)
        print(f"Processing: {file}")
        video = cv2.VideoCapture(file)
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(video.get(cv2.CAP_PROP_FPS))
        frame_count = int(fps * target_duration)
        total_frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        loop_count = frame_count // total_frame_count
        remainder_frames = frame_count % total_frame_count
        
        for _ in range(loop_count):
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            for frame_num in range(total_frame_count):
                ret, frame = video.read()
                if not ret:
                    break
                frame = cv2.resize(frame, sticker_size)
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                writer.append_data(frame_rgb)
        
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        for frame_num in range(remainder_frames):
            ret, frame = video.read()
            if not ret:
                break
            frame = cv2.resize(frame, sticker_size)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            writer.append_data(frame_rgb)
        
        writer.close()







