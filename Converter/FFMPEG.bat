FOR /F "tokens=*" %%G IN ('dir /b *.mp*') DO ffmpeg -i "%%G" -c:a libvorbis -q:a 4 "%%~nG.ogg"