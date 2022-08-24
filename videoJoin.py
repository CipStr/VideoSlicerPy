import os
import time
import urllib.request

from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from absl import app, flags, logging
from absl.flags import FLAGS

flags.DEFINE_string('inputFolder', '', 'Input folder')
flags.DEFINE_string('outputFile', '', 'Output file')
flags.DEFINE_boolean('auto', False, 'Waits for containers and then joins the clips')


def main(argv):
    if FLAGS.auto:
        print('gonna wait for containers')
        # wait 100 seconds for containers to be created
        time.sleep(100)
        page = urllib.request.urlopen("http://172.17.0.1:80/container")
        container_number = page.read()
        # from bytes to string
        container_number = container_number.decode("utf-8")
        # convert to int
        container_number = int(container_number) - 1
        print(container_number)
        while urllib.request.urlopen("http://172.17.0.1:80/oknumber").read().decode("utf-8") != str(container_number):
            print("Waiting for containers...")
            print(urllib.request.urlopen("http://172.17.0.1:80/oknumber").read().decode("utf-8"))
            time.sleep(15)
    # access the folder
    folder = FLAGS.inputFolder
    # get the list of files in the folder
    files = os.listdir(folder)
    # create a list of files to be joined
    filesToJoin = []
    # loop through the files
    for file in files:
        # get the file name
        fileName = os.path.join(folder, file)
        # get the file extension
        fileExtension = os.path.splitext(fileName)[1]
        # if the file is a video file
        if fileExtension == '.avi':
            # add the file to the list of files to be joined
            filesToJoin.append(fileName)
            # sort the list of files to be joined
            filesToJoin.sort()

    clips = [VideoFileClip(c) for c in filesToJoin]
    final_clip = concatenate_videoclips(clips, method="compose")
    logging.info('Video joined!')
    final_clip.write_videofile(FLAGS.outputFile)

if __name__ == '__main__':
    app.run(main)
