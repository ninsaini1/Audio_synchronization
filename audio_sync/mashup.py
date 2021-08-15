from moviepy.editor import *
import random

import os

def mash( vid1, vid2, vid3):
    cap = []

    cap.append(vid1)
    cap.append(vid2)
    cap.append(vid3)

    i=0
    final = VideoFileClip(cap[0]).subclip(0,1)
    clips = []

    while True:
        k = random.randint(0,2)
        t = random.randint(5,10)
    
        clip = VideoFileClip(cap[k])
        clip = clip.subclip(i, i+t)
        clips.append(clip)

        i = i+t
        print(i)
    
        # 30 sec video mashup
        if i >60:
            print('successful')
            break

    final = concatenate_videoclips([v for v in clips])
    final.write_videofile(r'C:\Users\neera\Desktop\Final_Project\l1.mp4')
    return final