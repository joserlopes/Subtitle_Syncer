
# Subtitle Syncer

## How to use

- The *first* command line argument is path of the .srt file you want to sync
- The *second* and *third* arguments are respectively the beggining and end times of trimming.
- The new file with the subtitles synced is saved with the path given in the *fourth* command line argument.

## The "base" form is

```sh
python subtitle_syncer.py <original_path.srt> <begin_time> <end_time> <destinition_path.srt>
```

With begin_time and end_time being in hh:mm:ss format.  

## An example would be

```sh
python subtitle_syncer.py my_file.srt 00:30:50 00:35:34 synced_file.srt
```

This syncs the subtitle file *my_file.srt* if the video file related to it where to be cut between minutes 30:50 and 35:34 saving the resulting subtitles file with the name *synced_file.srt*.

---

# Video cutter

## How to use

- The *first* command line argument is the path of the .mp4 file you want to cut
- The *second* and *third* arguments are, respectively, the time in which the cut begins and the time in which it ends
- The *fourth* argument is the time in which the video ends
- The *fifth* argument is the path of the new cutted file

## The "base" form is

```sh
python video_cutter.py <original_path.mp4> <cut_begin_time> <cut_end_time> <video_end_time>  
<new_path.mp4> 
```

With cut_begin_time cut_end_time and video_end_time being in hh:mm:ss format.

## An example would be

```sh
python video_cutter.py my_file.mp4 00:30:50 00:40:30 1:40:38 cut_file.mp4
```

This cuts the original video *my_file.p4* between minutes 30:50 and 40:30 saving the resulting video with the name *cut_file.mp4*.
