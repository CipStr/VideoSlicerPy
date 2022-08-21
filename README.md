# VideoSlicerPy+VideoJoin
Python Video Slicer

Little quality of life project used in yolov3-tf2 containerized version. It simply slices a video.

The command line structure is:  python videoSlicer.py --inputFile path_to_file --outputFile path_to_file --(optional)part part_number --auto enables_auto_slicing_in_x_parts

The part number indicates which one to slice (ex: part 0 slices from 0 to x seconds).

To install dependecies: pip install -r requirements.txt


ADDED: VideoJoin

It joins the sliced parts. 

To use it:  python videoJoin.py --inputFolder path_to_clips_folder (must contain only video files) --outputFile path_to_file
