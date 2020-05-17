import os

dirName = "Plotspng2"



# Creating Directories
def createDir(dirName):
    try:
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")


# Serial file namer
def namer(x):
    s = str(x)
    if len(s) == 1:
        return "000" + s
    elif len(s) == 2:
        return "00" + s
    elif len(s) == 3:
        return "0" + s
    else:
        return s


# Create an MPEG from a batch of files
def convert_mpeg(outputfile):
    command = 'ffmpeg -r 60 -f image2 -s 1920x1080 -i ' + os.getcwd() + '/Plotspng/p%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p ' + outputfile
    os.system(command)
    print("MPEG Exported!")


def convert_svg(n, dirName, inputFolder):
    command = ("convert " + os.getcwd() + "/" + inputFolder + "/g" + str(n) + ".svg " + dirName + "/p" + namer(
        n) + ".png")
    os.system(command)

def BatchConvert(inputFolder, outputFile, frames):
    dirName = "PlotsPng"
    os.mkdir(dirName)
    print("Directory ", dirName, " Created ")
    for i in range(frames + 1):
        convert_svg(i, dirName, inputFolder)
    convert_mpeg(outputFile)

#User Functions
def create_raster(filename, dir=os.getcwd(), savedir=os.getcwd()):
    command = ("convert " + os.getcwd() + "/" + dir + filename + ".svg " + savedir + "/" + filename + ".png")
    os.system(command)

def create_raster_batch(dir, filename, savename ,savedir, num):
    for i in range(num):
        command = ("convert " + os.getcwd() + "/" + dir +'/'+ filename + str(namer(i)) + ".svg " + os.getcwd()+'/'+ savedir + "/" + savename + namer(i) + ".png")
        os.system(command)

def create_mpeg(filename, batchname, num, dir = os.getcwd(), framerate='60'):
    command = 'ffmpeg -r ' + framerate +' -f image2 -s 1920x1080 -i ' + dir +'/'+ batchname+'%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p ' + filename
    os.system(command)

# creat_mpeg + create_raster_batch
def create_animation(dir, filename, num, savefile,  savename='p', framerate=60):
    create_raster_batch(dir, filename, savename, "TempFiles", num)
    create_mpeg(savefile, savename, num, framerate=framerate)


def onlyExport(output):
    convert_mpeg(output)


'''
# Convert SVG -> PNG
for i in range(0,100):
    convert_svg()
    command = ("convert "+ os.getcwd() +"/Plots/g"+  str(i)+".svg "+dirName+"/p"+ namer(i)+".png")
    os.system(command)


# Convert PNG -> MP4
convert_mpeg()
command = "ffmpeg -r 60 -f image2 -s 1920x1080 -i Plotspng/p%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p test3.mp4"
os.system(command)
print("Done!")

'''
