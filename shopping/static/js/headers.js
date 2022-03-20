window.onload = function () {

    var movePic = document.getElementById('movePic');
    var img = movePic.children[0];
    var left = movePic.children[1];
    var right = movePic.children[2];
    var images = ['/static/images/lunbo1.jpg','/static/images/lunbo2.jpg','/static/images/lunbo3.jpg','/static/images/lunbo4.jpg'];
    var minIndex = 0;
    var maxIndex = images.length;
    var currentIndex = 0;

    right.onclick = function () {
            currentIndex ++;
            if (currentIndex === maxIndex){
                currentIndex = 0;
                img.src = images[currentIndex];
            } else{
                img.src = images[currentIndex];
            }
    };
    left.onclick = function () {
        currentIndex --;
        if (currentIndex === -1){
            currentIndex = 3;
            img.src = images[currentIndex];
        }else{
            img.src = images[currentIndex];
        }

    }
};