-- use the ffmpeg video segmenter, its better and fast.

> prime-run python3 equal_parts.py /home/sourav/Downloads/King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG\[TGx\]/King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG.mkv --segment_duration 17


===================
SAMPLE OUTPUT
===================


ffmpeg version n6.1 Copyright (c) 2000-2023 the FFmpeg developers
  built with gcc 13.2.1 (GCC) 20230801
  configuration: --prefix=/usr --disable-debug --disable-static --disable-stripping --enable-amf --enable-avisynth --enable-cuda-llvm --enable-lto --enable-fontconfig --enable-frei0r --enable-gmp --enable-gnutls --enable-gpl --enable-ladspa --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libdav1d --enable-libdrm --enable-libfreetype --enable-libfribidi --enable-libgsm --enable-libharfbuzz --enable-libiec61883 --enable-libjack --enable-libjxl --enable-libmodplug --enable-libmp3lame --enable-libopencore_amrnb --enable-libopencore_amrwb --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libplacebo --enable-libpulse --enable-librav1e --enable-librsvg --enable-librubberband --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtheora --enable-libv4l2 --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpl --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxcb --enable-libxml2 --enable-libxvid --enable-libzimg --enable-nvdec --enable-nvenc --enable-opencl --enable-opengl --enable-shared --enable-version3 --enable-vulkan
  libavutil      58. 29.100 / 58. 29.100
  libavcodec     60. 31.102 / 60. 31.102
  libavformat    60. 16.100 / 60. 16.100
  libavdevice    60.  3.100 / 60.  3.100
  libavfilter     9. 12.100 /  9. 12.100
  libswscale      7.  5.100 /  7.  5.100
  libswresample   4. 12.100 /  4. 12.100
  libpostproc    57.  3.100 / 57.  3.100
Input #0, matroska,webm, from '/home/sourav/Downloads/King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG[TGx]/King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG.mkv':
  Metadata:
    title           : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
    COMMENT         : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
    ENCODER         : Lavf58.76.100
  Duration: 01:30:57.36, start: 0.000000, bitrate: 1225 kb/s
  Stream #0:0: Video: h264 (High), yuv420p(tv, bt709, progressive), 1280x532 [SAR 399:400 DAR 12:5], 23.98 fps, 23.98 tbr, 1k tbn (default)
    Metadata:
      title           : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
      BPS             : 6779632
      NUMBER_OF_FRAMES: 130844
      NUMBER_OF_BYTES : 4624798600
      _STATISTICS_WRITING_APP: mkvmerge v78.0 ('Running') 64-bit
      _STATISTICS_WRITING_DATE_UTC: 2023-09-05 20:07:40
      _STATISTICS_TAGS: BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
      ENCODER         : Lavc58.134.100 libx264
      DURATION        : 01:30:57.328000000
  Stream #0:1(eng): Audio: aac (LC), 48000 Hz, stereo, fltp (default)
    Metadata:
      title           : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
      BPS             : 640000
      NUMBER_OF_FRAMES: 170541
      NUMBER_OF_BYTES : 436584960
      _STATISTICS_WRITING_APP: mkvmerge v78.0 ('Running') 64-bit
      _STATISTICS_WRITING_DATE_UTC: 2023-09-05 20:07:40
      _STATISTICS_TAGS: BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
      ENCODER         : Lavc58.134.100 libfdk_aac
      DURATION        : 01:30:57.355000000
  Stream #0:2(eng): Subtitle: subrip (default)
    Metadata:
      title           : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
      BPS             : 40
      NUMBER_OF_FRAMES: 889
      NUMBER_OF_BYTES : 25910
      _STATISTICS_WRITING_APP: mkvmerge v78.0 ('Running') 64-bit
      _STATISTICS_WRITING_DATE_UTC: 2023-09-05 20:07:40
      _STATISTICS_TAGS: BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
      DURATION        : 01:27:21.495000000
  Stream #0:3(eng): Subtitle: subrip
    Metadata:
      title           : SDH
      BPS             : 45
      NUMBER_OF_FRAMES: 1101
      NUMBER_OF_BYTES : 30651
      _STATISTICS_WRITING_APP: mkvmerge v78.0 ('Running') 64-bit
      _STATISTICS_WRITING_DATE_UTC: 2023-09-05 20:07:40
      _STATISTICS_TAGS: BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
      DURATION        : 01:30:57.277000000
  Stream #0:4(fre): Subtitle: subrip
    Metadata:
      BPS             : 41
      NUMBER_OF_FRAMES: 844
      NUMBER_OF_BYTES : 26455
      _STATISTICS_WRITING_APP: mkvmerge v78.0 ('Running') 64-bit
      _STATISTICS_WRITING_DATE_UTC: 2023-09-05 20:07:40
      _STATISTICS_TAGS: BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
      DURATION        : 01:27:21.321000000
Stream mapping:
  Stream #0:0 -> #0:0 (h264 (native) -> h264 (h264_nvenc))
  Stream #0:1 -> #0:1 (aac (native) -> aac (native))
Press [q] to stop, [?] for help
Output #0, mp4, to '/home/sourav/Documents/video_slicer/output_segments/King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG.mp4':
  Metadata:
    title           : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
    COMMENT         : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
    encoder         : Lavf60.16.100
  Stream #0:0: Video: h264 (Main) (avc1 / 0x31637661), nv12(tv, bt709, progressive), 1280x532 [SAR 399:400 DAR 12:5], q=2-31, 2000 kb/s, 23.98 fps, 24k tbn (default)
    Metadata:
      title           : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
      BPS             : 6779632
      NUMBER_OF_FRAMES: 130844
      NUMBER_OF_BYTES : 4624798600
      _STATISTICS_WRITING_APP: mkvmerge v78.0 ('Running') 64-bit
      _STATISTICS_WRITING_DATE_UTC: 2023-09-05 20:07:40
      _STATISTICS_TAGS: BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
      DURATION        : 01:30:57.328000000
      encoder         : Lavc60.31.102 h264_nvenc
    Side data:
      cpb: bitrate max/min/avg: 0/0/2000000 buffer size: 4000000 vbv_delay: N/A
  Stream #0:1(eng): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 192 kb/s (default)
    Metadata:
      title           : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
      BPS             : 640000
      NUMBER_OF_FRAMES: 170541
      NUMBER_OF_BYTES : 436584960
      _STATISTICS_WRITING_APP: mkvmerge v78.0 ('Running') 64-bit
      _STATISTICS_WRITING_DATE_UTC: 2023-09-05 20:07:40
      _STATISTICS_TAGS: BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
      DURATION        : 01:30:57.355000000
      encoder         : Lavc60.31.102 aac
[out#0/mp4 @ 0x556ea94f4380] video:1311742kB audio:128385kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.256390%
frame=130845 fps=425 q=13.0 Lsize= 1443819kB time=01:30:57.34 bitrate=2167.3kbits/s dup=1 drop=0 speed=17.7x    
[aac @ 0x556eaa74ff00] Qavg: 4746.846
ffmpeg version n6.1 Copyright (c) 2000-2023 the FFmpeg developers
  built with gcc 13.2.1 (GCC) 20230801
  configuration: --prefix=/usr --disable-debug --disable-static --disable-stripping --enable-amf --enable-avisynth --enable-cuda-llvm --enable-lto --enable-fontconfig --enable-frei0r --enable-gmp --enable-gnutls --enable-gpl --enable-ladspa --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libdav1d --enable-libdrm --enable-libfreetype --enable-libfribidi --enable-libgsm --enable-libharfbuzz --enable-libiec61883 --enable-libjack --enable-libjxl --enable-libmodplug --enable-libmp3lame --enable-libopencore_amrnb --enable-libopencore_amrwb --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libplacebo --enable-libpulse --enable-librav1e --enable-librsvg --enable-librubberband --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtheora --enable-libv4l2 --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpl --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxcb --enable-libxml2 --enable-libxvid --enable-libzimg --enable-nvdec --enable-nvenc --enable-opencl --enable-opengl --enable-shared --enable-version3 --enable-vulkan
  libavutil      58. 29.100 / 58. 29.100
  libavcodec     60. 31.102 / 60. 31.102
  libavformat    60. 16.100 / 60. 16.100
  libavdevice    60.  3.100 / 60.  3.100
  libavfilter     9. 12.100 /  9. 12.100
  libswscale      7.  5.100 /  7.  5.100
  libswresample   4. 12.100 /  4. 12.100
  libpostproc    57.  3.100 / 57.  3.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '/home/sourav/Documents/video_slicer/output_segments/King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    title           : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
    encoder         : Lavf60.16.100
    comment         : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
  Duration: 01:30:57.37, start: 0.000000, bitrate: 2167 kb/s
  Stream #0:0[0x1](und): Video: h264 (Main) (avc1 / 0x31637661), yuv420p(tv, bt709, progressive), 1280x532 [SAR 399:400 DAR 12:5], 1969 kb/s, 23.98 fps, 23.98 tbr, 24k tbn (default)
    Metadata:
      handler_name    : VideoHandler
      vendor_id       : [0][0][0][0]
      encoder         : Lavc60.31.102 h264_nvenc
  Stream #0:1[0x2](eng): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 192 kb/s (default)
    Metadata:
      handler_name    : SoundHandler
      vendor_id       : [0][0][0][0]
[segment @ 0x559e50c10240] Opening '/home/sourav/Documents/video_slicer/output_segments/segment_0.mp4' for writing
Output #0, segment, to '/home/sourav/Documents/video_slicer/output_segments/segment_%d.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    title           : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
    comment         : GalaxyRG - King.of.Killers.2023.720p.AMZN.WEBRip.800MB.x264-GalaxyRG
    encoder         : Lavf60.16.100
  Stream #0:0(und): Video: h264 (Main) (avc1 / 0x31637661), yuv420p(tv, bt709, progressive), 1280x532 [SAR 399:400 DAR 12:5], q=2-31, 1969 kb/s, 23.98 fps, 23.98 tbr, 24k tbn (default)
    Metadata:
      handler_name    : VideoHandler
      vendor_id       : [0][0][0][0]
      encoder         : Lavc60.31.102 h264_nvenc
  Stream #0:1(eng): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 192 kb/s (default)
    Metadata:
      handler_name    : SoundHandler
      vendor_id       : [0][0][0][0]
Stream mapping:
  Stream #0:0 -> #0:0 (copy)
  Stream #0:1 -> #0:1 (copy)
Press [q] to stop, [?] for help
[segment @ 0x559e50c10240] Opening '/home/sourav/Documents/video_slicer/output_segments/segment_1.mp4' for writing
[segment @ 0x559e50c10240] Opening '/home/sourav/Documents/video_slicer/output_segments/segment_2.mp4' for writing
[segment @ 0x559e50c10240] Opening '/home/sourav/Documents/video_slicer/output_segments/segment_3.mp4' for writing
[segment @ 0x559e50c10240] Opening '/home/sourav/Documents/video_slicer/output_segments/segment_4.mp4' for writing
[segment @ 0x559e50c10240] Opening '/home/sourav/Documents/video_slicer/output_segments/segment_5.mp4' for writing
[out#0/segment @ 0x559e50a61a00] video:1311742kB audio:128385kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown
size=N/A time=01:30:57.34 bitrate=N/A speed=1.42e+03x 