const toggleBtn = document.getElementById('toggle-btn');
const galleryBtn = document.getElementById('gallery-btn');
const cameraBtn = document.getElementById('camera-btn');
const bgContainer = document.getElementById('bg-container');
const body = document.querySelector('body');

const imageUpload = document.getElementById('image-upload');

let check = 0;

function changeBackground() {
    if (check % 2 == 0) {
        document.body.style.background = "black";
    }
    else {
        document.body.style.background = "white";
    }
    check++;
}

imageUpload.addEventListener('change', (event) => {
    const selectedImage = event.target.files[0];
    const imageUrl = URL.createObjectURL(selectedImage);
    document.body.style.backgroundImage = `url(${imageUrl})`;
});
