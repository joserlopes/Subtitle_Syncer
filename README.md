# Subtitle Syncer

## How to use

- The *first* command line argument is the .srt file you want to sync
- The *second* and *third* arguments are respectively the beggining and end times of trimming.
- The new file with the subtitles synced is saved with the path given in the *fourth* command line argument.

## An example would be as follows

```sh
python subtitle_syncer.py <original_path.srt> <begin_time> <end_time> <destinition_path.srt>
```

with begin_time and end_time being in hh:mm:ss format.
