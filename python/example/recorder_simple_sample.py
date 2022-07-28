import time
import numpy

from screen_recorder_sdk import screen_recorder


def main ():
    screen_recorder.enable_dev_log ()
    
    params = screen_recorder.RecorderParams ()
    # params.pid = 0 # use it to set process Id to capture
    # params.desktop_num = 0 # use it to set desktop num, counting from 0

    screen_recorder.init_resources (params)
    screen_recorder.start_crop_video_recording ('video1.mp4', 30, 8000000, True, 500, 500, 900, 900)
    #-->  screen_recorder.start_video_recording ('video1.mp4', 30, 8000000, True) still available for a full screen or use crop version with 0s as last 4 params;
    time.sleep (10)
    screen_recorder.stop_video_recording ()


    screen_recorder.free_resources ()

if __name__ == "__main__":
    main ()
