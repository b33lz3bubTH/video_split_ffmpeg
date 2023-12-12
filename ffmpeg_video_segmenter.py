
# FFMPEG -> Faster
import subprocess
import os
import argparse
import mimetypes

class VideoSegmenter:
    def __init__(self, input_video, output_folder, segment_duration_min=15):
        self.input_video = input_video
        self.output_folder = output_folder
        self.segment_duration_min = segment_duration_min

    def _check_video_format_as_mp4(self):
        mime_type, _ = mimetypes.guess_type(self.input_video)
        return mime_type == 'video/mp4'

    def _convert_to_mp4_gpu(self, input_file, output_file):
        convert_command = [
            'ffmpeg',
            '-hwaccel', 'cuda',
            '-i', input_file,
            '-c:v', 'h264_nvenc',
            '-c:a', 'aac',
            '-strict', 'experimental',
            '-b:a', '192k',
            output_file
        ]
        subprocess.run(convert_command, check=True)

    def split_video(self):
        input_video = os.path.abspath(self.input_video)
        output_folder = os.path.abspath(self.output_folder)
        segment_duration_sec = self.segment_duration_min * 60

        # Check if the video is already in MP4 format
        if not self._check_video_format_as_mp4():
            # Convert video to MP4 using GPU acceleration
            output_template = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_video))[0]}.mp4")
            self._convert_to_mp4_gpu(input_video, output_template)
        else:
            output_template = input_video

        # Split the video
        ffmpeg_command = [
            'ffmpeg',
            '-i', output_template,
            '-c', 'copy',
            '-map', '0',
            '-f', 'segment',
            '-segment_time', str(segment_duration_sec),
            '-reset_timestamps', '1',
            f"{os.path.join(output_folder, 'segment_%d.mp4')}"
        ]

        subprocess.run(ffmpeg_command, check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Video segmentation tool.")
    parser.add_argument("input_video", help="Path to the input video file.")
    parser.add_argument("--segment_duration", type=int, default=15, help="Segment duration in minutes. Default: 15 minutes")
    args = parser.parse_args()

    input_video_path = args.input_video
    output_folder_path = "output_segments"
    segment_duration_minutes = args.segment_duration

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    segmenter = VideoSegmenter(input_video_path, output_folder_path, segment_duration_min=segment_duration_minutes)
    segmenter.split_video()
