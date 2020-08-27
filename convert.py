import multiprocessing
from threading import Thread
import os

dirName = "Plotspng2"


# Creating Directories
def create_directory(dirName):
    try:
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")

# Serial file namer
def namer(x):
    return (f'{x:04}')

def convert_mpeg(outputfile):
    command = 'ffmpeg -r 60 -f image2 -s 1920x1080 -i ' + os.getcwd() + '/Plotspng/p%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p ' + outputfile
    os.system(command)
    print("MPEG Exported!")


# converts image formats
def convert_image(inputfile, outputfile):
    command = ("rsvg-convert %s -o %s ") % (inputfile, outputfile)
    os.system(command)

def convert_serial_svg_old(n, dirName, inputFolder, filetype='png'):
    command = ("convert " + os.getcwd() + "/" + inputFolder + "/g" + str(n) + ".svg " + dirName + "/p" + namer(
        n) + "." + filetype)
    os.system(command)

def convert_serial_svg(n, dirName, inputFolder, filetype='png'):
    command = ("rsvg-convert  %s/%s/g%s.svg -o /p%s.%s") % (os.getcwd(), inputFolder, n, dirName, namer(n), filetype)
    os.system(command)

def batch_convert(inputFolder, outputFile, frames):
    dirName = "PlotsPng"
    os.mkdir(dirName)
    print("Directory ", dirName, " Created ")
    for i in range(frames + 1):
        convert_serial_svg(i, dirName, inputFolder)
    convert_mpeg(outputFile)


def batch_convert_multi(inputFolder, outputFile, frames):
    dirName = "PlotsPng"
    os.mkdir(dirName)
    print("Directory ", dirName, " Created ")
    jobs = []
    for i in range(frames + 1):
        p = multiprocessing.Process(target=convert_serial_svg, args=(i, dirName, inputFolder))
        jobs.append(p)
        p.start()
    convert_mpeg(outputFile)


def generate_frames(worker, frames, *args):
    jobs = []
    for i in range(frames + 1):
        p = multiprocessing.Process(target=worker, args=(i, args,))
        jobs.append(p)
        p.start()


# User Functions
def create_raster(filename, dir=os.getcwd(), savedir=os.getcwd()):
    command = ("convert " + os.getcwd() + "/" + filename + ".svg " + savedir + "/" + filename + ".png")
    os.system(command)

def create_raster2(filename, dir=os.getcwd(), savedir=os.getcwd()):
    command = ("rsvg-convert " + os.getcwd() + "/" + filename + ".svg  -o " + savedir + "/" + filename + ".png")
    os.system(command)



def create_raster_batch2(dir, filename, savename, savedir, num):
    for i in range(num):
        command = ("convert " + os.getcwd() + "/" + dir + '/' + filename + str(
            namer(i)) + ".svg " + os.getcwd() + '/' + savedir + "/" + savename + namer(i) + ".png")
        os.system(command)

def create_raster_batch(dir, filename, savename, savedir, num):
    for i in range(num):
        command = ("rsvg-convert %s/%s/%s%s.svg -o %s/%s/%s%s.png") % (os.getcwd(), dir, filename, namer(i), os.getcwd(), savedir, savename, namer(i))
        os.system(command)

create_raster_batch("ftp", 'g', 'p', 'ftprast', 1)

def create_mpeg(filename, batchname, num, dir=os.getcwd(), framerate='60'):
    command = ('ffmpeg -r %s -f image2 -s 1920x1080 -i %s/%s%s04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p %s') %(framerate,dir, batchname, '%',filename)
    os.system(command)


# creat_mpeg + create_raster_batch
def create_animation(dir, filename, num, savefile, savename='p', framerate=60):
    create_raster_batch(dir, filename, savename, "TempFiles", num)
    create_mpeg(savefile, savename, num, framerate=framerate)


def onlyExport(output):
    convert_mpeg(output)

def clean_up(a, b):
    command = "rm " + a
    os.system(command)

    command = "rm " + b
    os.system(command)
'''
# Convert SVG -> PNG
for i in range(0,100):
    convert_serial_svg()
    command = ("convert "+ os.getcwd() +"/Plots/g"+  str(i)+".svg "+directory+"/p"+ namer(i)+".png")
    os.system(command)


# Convert PNG -> MP4
convert_mpeg()
command = "ffmpeg -r 60 -f image2 -s 1920x1080 -i Plotspng/p%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p test3.mp4"
os.system(command)
print("Done!")

'''
