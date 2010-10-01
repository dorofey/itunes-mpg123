#!/usr/bin/python
import os
import sys
import glob

USER=os.getlogin()
MUSIC_DIR=os.path.join('/Users',USER,'Music/iTunes/iTunes Media/Music/')
PLS=os.path.join('/Users',USER,'Music/playlist.pls')

def my_list_dir(somedir):
    return [elm for elm in os.listdir(somedir) if not elm.startswith('.')]

arg=' '.join(sys.argv[1:])
band, album = arg.split('/', 1) if arg.count('/') > 0 else arg, None

bands = my_list_dir(MUSIC_DIR)

tracks = []
for bnd in bands:
    if bnd.lower().startswith(band.lower()):
        band_dir=os.path.join(MUSIC_DIR, bnd)
        band_alb=my_list_dir(band_dir)
        for alb in band_alb:
            if not album or alb.lower().startswith(album.lower()):
                alb_dir=os.path.join(band_dir, alb, '*.mp3')
                tracks.extend(glob.glob(alb_dir))

_pls = "\n".join(tracks)
if len(_pls) > 0:
    pls = open(PLS, 'w')
    pls.write(_pls)
    pls.close()
    os.system('mpg123 -C -@ ' + PLS)
                
