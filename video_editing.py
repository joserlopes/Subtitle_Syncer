import sys
from moviepy.editor import *

def parse_time(time):
    time_split = time.split(":")
    return {"hours": int(time_split[0]), "minutes": int(time_split[1]), "seconds": int(time_split[2])}


def time_to_seconds(hours, minutes, seconds): 
    hours_to_seconds = hours * 3600
    minutes_to_seconds = minutes * 60
    return hours_to_seconds + minutes_to_seconds + seconds

def main(args):
    first_time_parsed = parse_time(args[1])
    first_time_seconds = time_to_seconds(first_time_parsed["hours"], first_time_parsed["minutes"], first_time_parsed["seconds"])
    seconds_time_begin_parsed = parse_time(args[2])
    seconds_time_end_parsed = parse_time(args[3])
    seconds_time_begin_seconds = time_to_seconds(seconds_time_begin_parsed["hours"], seconds_time_begin_parsed["minutes"], seconds_time_begin_parsed["seconds"])
    seconds_time_end_seconds = time_to_seconds(seconds_time_end_parsed["hours"], seconds_time_end_parsed["minutes"], seconds_time_end_parsed["seconds"]) 

    clip1 = VideoFileClip(args[0]).subclip(0, first_time_seconds)
    clip2 = VideoFileClip(args[0]).subclip(seconds_time_begin_seconds, seconds_time_end_seconds)

    final_clip = concatenate_videoclips([clip1, clip2])

    final_clip.write_videofile("output_1.mp4")

if __name__ == "__main__":
    main(sys.argv[1:])