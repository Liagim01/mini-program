'''
This file contains the FrameCapture class responsible for capturing frames from a video file.
'''
import cv2
class FrameCapture:
    def __init__(self, file_path):
        self.file_path = file_path
    def capture_frames(self, directory):
        try:
            video_capture = cv2.VideoCapture(self.file_path)
            success, image = video_capture.read()
            count = 0
            while success:
                frame_path = f"{directory}/frame_{count}.jpg"
                cv2.imwrite(frame_path, image)
                success, image = video_capture.read()
                count += 1
            video_capture.release()
        except cv2.error as e:
            raise Exception(f"Error capturing frames: {str(e)}")