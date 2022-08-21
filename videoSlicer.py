import os

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from absl import app, flags, logging
from absl.flags import FLAGS

flags.DEFINE_string('inputFile', '', 'Input file')
flags.DEFINE_string('outputFile', '', 'Output file')
flags.DEFINE_integer('part', 0, 'Part number')
flags.DEFINE_boolean('auto', False, 'Auto slices video and puts clips in clips folder   ')


def main(argv):
    clipLength = 20
    if FLAGS.auto:
        # create folder if it doesn't exist
        if not os.path.exists('./clips'):
            os.makedirs('clips')
        #get video length
        videoLength = VideoFileClip(FLAGS.inputFile).duration
        # get number of parts
        parts = int(videoLength / clipLength)
        # loop through parts
        for i in range(parts):
            # get part number
            part = i
            # get part name
            partName = './clips/part' + str(part) + '.mp4'
            # extract part
            ffmpeg_extract_subclip(FLAGS.inputFile, i * clipLength, (i + 1) * clipLength, targetname=partName)
            # print part name
            print(partName)
    else:
        # clip lenght in seconds
        if len(argv) < 1:
            raise app.UsageError('Number of command-line arguments must be at least 1 (input and (output file or auto mode)).')
        # start time is based on part number
        start = FLAGS.part * clipLength
        # end time is based on part number and clip length
        end = (FLAGS.part + 1) * clipLength
        # add part number to output file name
        outputFile = FLAGS.outputFile + '_' + str(FLAGS.part) + '.mp4'
        ffmpeg_extract_subclip(FLAGS.inputFile, start, end, targetname=outputFile)
        logging.info('Video sliced!')


if __name__ == '__main__':
    app.run(main)

