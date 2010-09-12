#!/usr/bin/php
<?php
define('MUSIC_DIR', '/Users/dorofey/Music/iTunes/iTunes Media/Music/');
$dh = opendir(MUSIC_DIR);
while (($file = readdir($dh)) !== false) {
    if(strpos($file, '.') !== 0) $bands[] = $file;
}
closedir($dh);

$_ar = $argv;
array_shift($_ar);
$_ar = explode('/',implode(' ', $_ar));

$_band = $_ar[0];
$_album= (isset($_ar[1]))?$_ar[1]:'';
foreach ($bands as $band) {
    if(strpos(strtolower($band), strtolower($_band)) === 0) {
        printf("Band: %s found!\n", $band,$_band,$_album);
        $banddir = MUSIC_DIR . $band . '/';
        $dh = opendir($banddir);
        $albums = array();
        while (($file = readdir($dh)) !== false) {
            if(strpos($file, '.') !== 0 && (!$_album || strpos(strtolower($file), strtolower($_album)) === 0))
                $albums[] = $file;
        }
        closedir($dh);
        foreach($albums as $album) {
            $dir = $banddir . $album . '/';
            $dh = opendir($dir);
            while (($file = readdir($dh)) !== false) {
                if(strpos($file, '.') !== 0)
                    $tracks[] = $dir . $file;
            }
            
        }
        if(count($tracks > 0)) {
            $fp = fopen('/Users/dorofey/Music/playlist.txt', 'w');
            foreach($tracks as $track) {
                fputs($fp, $track . "\n");
            }
            fclose($fp);
            exec('mpg123 -C -@ ' . '/Users/dorofey/Music/playlist.txt');
        }
    }
}

?>