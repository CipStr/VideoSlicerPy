from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from absl import app, flags, logging
from absl.flags import FLAGS

flags.DEFINE_string('inputFile', '', 'Input file')
flags.DEFINE_string('outputFile', '', 'Output file')
flags.DEFINE_integer('part', 0, 'Part number')


def main(argv):
    # clip lenght in seconds
    clipLength = 20
    if len(argv) < 1:
        raise app.UsageError('Number of command-line arguments must be at least 2 (input and output file).')
    # start time is based on part number
    start = FLAGS.part * clipLength
    # end time is based on part number and clip length
    end = (FLAGS.part + 1) * clipLength
    ffmpeg_extract_subclip(FLAGS.inputFile, start, end, targetname=FLAGS.outputFile)
    logging.info('Video sliced!')


if __name__ == '__main__':
    app.run(main)
