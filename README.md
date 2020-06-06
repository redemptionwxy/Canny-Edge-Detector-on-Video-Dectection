# Canny-Edge-Detector-on-Video-Dectection
Use Canny Edge Detector algorithm on video edge dectection.

Canny_Photo.py is used Canny to detect photo edges.



LiveCannyVideo.py is used Canny to detect videos frame by frame captured lively via camera.



If you want to dectect your own local video, put your video into the same directory as the py file. And create a new folder called 'Frame' to store the output frame images.
Canny_VideotoFrame.py is used Canny Detector to detect the video frame by frame. The last few frames maybe hard for OpenCV to capture, so that probably has cv2.error: OpenCV(4.0.0) error notification.


All the frames are stored in Frame folder, and then run FrametoVideo.py, change fps and frames amount from the original video. Then the new video will be stored in the root direction called demo.mp4


If your original video has audio, then run VideoaddAudio.py to add the original audio to the demo.mp4. Then a new video called demo_out.mp4 has been saved in root direction.
