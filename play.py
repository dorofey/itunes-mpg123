#!/usr/bin/python
import os
import sys
import glob

MUSIC_DIR=os.path.join('/Users',os.getlogin(),'Music/iTunes/iTunes Media/Music/')
PLS=os.path.join('/Users',os.getlogin(),'Music/playlist.pls')

arg=' '.join(sys.argv[1:])
if arg.count('/') > 0: band, album = arg.split('/', 1) 
else: band, album = arg, None 


bands = [elm for elm in os.listdir(MUSIC_DIR) if not elm.startswith('.')] #get rid of .DS_Store

tracks = []
for bnd in bands:
    if bnd.lower().startswith(band.lower()):
        band_dir=os.path.join(MUSIC_DIR, bnd)
        band_alb=[elm for elm in os.listdir(band_dir) if not elm.startswith('.')]
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
                
