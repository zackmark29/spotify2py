var isplaying = false; 

function MusicPlayer() {

    if (isplaying === false) {
        isplaying = true;
        document.getElementById("AudioSource").play()
        document.getElementById("controls").src = "assets/img/pause.png"
    } 
    
    else if (isplaying === true) {
        isplaying = false;
        document.getElementById("AudioSource").pause()    
        document.getElementById("controls").src = "assets/img/play.png"
    };

}
