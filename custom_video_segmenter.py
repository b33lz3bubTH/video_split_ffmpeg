from moviepy.editor import VideoFileClip
import os

class VideoSegmenter:
    def __init__(self, input_video, output_folder, segment_duration_min=15):
        self.input_video = input_video
        self.output_folder = output_folder
        self.segment_duration_min = segment_duration_min

    def split_video(self):
        full_clip = VideoFileClip(self.input_video)
        total_duration = full_clip.duration
        segment_duration = self.segment_duration_min * 60

        segment_number = 1
        while total_duration > segment_duration:
            start_time = total_duration - segment_duration
            end_time = total_duration
            segment_clip = full_clip.subclip(start_time, end_time)

            output_filename = self._generate_output_filename(segment_number)
            output_path = os.path.join(self.output_folder, output_filename)

            self._write_video_clip(segment_clip, output_path)
            print(f"Created segment: {output_path}")
            
            total_duration -= segment_duration
            segment_number += 1

    def _generate_output_filename(self, segment_number):
        base_name = os.path.splitext(os.path.basename(self.input_video))[0]
        return f"{base_name}_part{segment_number}.mp4"

    def _write_video_clip(self, video_clip, output_path):
        with video_clip as clip:
            clip.write_videofile(
                output_path,
                codec="libx264",
                temp_audiofile='temp-audio.m4a',
                remove_temp=True,
                audio_codec='aac'
            )

if __name__ == "__main__":
    input_video_path = "/home/sourav/Downloads/The Kerala Story (2023) 1080p Hindi HDTS x264 AAC - QRips.mp4"
    output_folder_path = "output_segments"
    segment_duration_minutes = 15

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    segmenter = VideoSegmenter(input_video_path, output_folder_path, segment_duration_min=segment_duration_minutes)
    segmenter.split_video()
