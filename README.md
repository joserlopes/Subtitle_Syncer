
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
