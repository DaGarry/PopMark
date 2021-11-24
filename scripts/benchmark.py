# Made by DaGarry and DrSolidDevil
# Github: https://github.com/DaGarry
# Github: https://github.com/DrSolidDevil
#
#
# This benchmark is for old computer that dont support other benchmark because of support. Like lack of support for directX 11, 12 etc.
# It's a Dual Benchmark so you need a cpu and gpu at the same "level". For example: 3060 and a 11600 so its not good for benchmarking a mining setup, etc.
# This benchmark was mostly made for Dr so he could benchmark his scrappers (pc's made from old pc parts).
# Feel free to use or contribute to this code. :)  
# under the GPL-3.0
#
#
#
# the benchmark consists of 5 runs
# One run consists of 20 chops 
# One chop consists of 20 snaps
# One snap consists of 10 frames 
# In total the benchmark is 20,000 frames the formula is: ((10 x 20) x 20) x 5





import tkinter as tk
from tkinter import Canvas, Frame, Tk, BOTH
from win32api import GetSystemMetrics as GSM
import time
import random






#  Settings

bwidth = 1 # width of the border.
cw = int(GSM(0)) - bwidth # fetches the width of the screen.
ch = int(GSM(1)) - bwidth # fetches the height of the screen.
multiplier = 10.0 # the multiplier is a float if it's not a float then it will return an error

root = Tk()




can = Canvas(root, bd=bwidth, height=ch, width=cw) # creates the canvas

class BenchUtil():  # This are the utilites for the benchmark


  def rancolor(self): # picks a color from this small list just for variation dont really need more colors
    colorchoice = random.choice(["#00e7ff", "#ff0000", "#46ff00", "#fff900", "ff0096"])
    return colorchoice
    
  def randXCord (self, cw): #selects position in the x from the entered width
    xcord = random.choice([random.randrange(0, cw), random.randrange(0, cw), random.randrange(0, cw), random.randrange(0, cw)]) 
    return xcord
    
  def randYCord(self, ch): #selects position in the y from the enterd width
    ycord = random.choice([random.randrange(0, ch), random.randrange(0, ch), random.randrange(0, ch), random.randrange(0, ch)]) 
    return ycord

  def benchFrame(self, cw, ch): # creates a single frame of the benchmark
    x0 = BenchUtil().randXCor(cw) - 100
    x1 = x0 + 100
    y0 = BenchUtil().randYCord(ch) - 100
    y1 = y0 + 100

    can.create_rectangle(x0, y0, x1, y1, fill=BenchUtil().rancolor()) #creates a rectangle at the random cordinates 100x100 size
    can.destroy()

  def benchSnap(self, cw, ch, multiplier): # a benchSnap is made of 10 bench frames¨

    if multiplier != float():
      # this makes sure that the multiplier is a float value and not an integer
      return ValueError

    # This runs one snap and mesures the time it takes
    snaptime = time.time()
    
    BenchUtil().benchFrame(cw, ch)
    BenchUtil().benchFrame(cw, ch)
    BenchUtil().benchFrame(cw, ch)
    BenchUtil().benchFrame(cw, ch)
    BenchUtil().benchFrame(cw, ch)
    BenchUtil().benchFrame(cw, ch)
    BenchUtil().benchFrame(cw, ch)
    BenchUtil().benchFrame(cw, ch)
    BenchUtil().benchFrame(cw, ch)
    BenchUtil().benchFrame(cw, ch)

    snaptime = time.time() - snaptime


    snapresult = int(snaptime * multiplier)  
    # multiplies the snap time with the multiplier and then turns it into an integer to allow for a better result. So dont set the multiplier to a integer because that will raise an error in the snap.

    return snapresult

  def benchChop(self, cw, ch, multiplier):

    # this is just a husk function meaning that it just runs a command(function)

    x = BenchUtil().benchSnap(cw, ch, multiplier)
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    x = BenchUtil().benchSnap(cw, ch, multiplier) + x
    
    return x
  
  def benchRun(self, cw, ch, multiplier):

    x = BenchUtil().benchChop(cw, ch, multiplier)
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x
    x = BenchUtil().benchChop(cw, ch, multiplier) + x

    return x


def Benchmark(width, height, multiplier):
  x = BenchUtil().benchRun(width, height, multiplier)
  x = BenchUtil().benchRun(width, height, multiplier) + x
  x = BenchUtil().benchRun(width, height, multiplier) + x
  x = BenchUtil().benchRun(width, height, multiplier) + x
  x = BenchUtil().benchRun(width, height, multiplier) + x
  x = x / 5
  return x
