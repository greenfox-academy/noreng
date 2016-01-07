'use strict';

var imageIndex = 0;

var images = [
  'http://lorempixel.com/400/200/technics/1',
  'http://lorempixel.com/400/200/technics/2',
  'http://lorempixel.com/400/200/technics/3',
  'http://lorempixel.com/400/200/technics/4'
];

var bigPicture = document.querySelector('.gallery');
var leftButton = document.querySelector('.left');
var rightButton = document.querySelector('.right');
var thumbnails = document.querySelector('.thumbnails');

leftButton.addEventListener('click', function() {
  if (imageIndex > 0) {
    imageIndex--;
  } else {
    imageIndex = images.length - 1;
  }
  setCurrentImageSource(images[imageIndex]);
});

rightButton.addEventListener('click', function() {
  if (imageIndex < images.length - 1) {
    imageIndex++;
  } else {
    imageIndex = 0;
  }
  setCurrentImageSource(images[imageIndex]);
});

thumbnails.addEventListener('mouseover', function(event) {
  if (event.target.src) {
    setCurrentImageSource(event.target.src);
  }
});

(function createThumbnails(src) {
  var image;
  for (var i = 0; i < images.length; i++) {
    image = document.createElement('img');
    image.setAttribute('src', images[i] );
    thumbnails.appendChild(image);
  }
})()

function setCurrentImageSource(source) {
  bigPicture.setAttribute('src', source);
}
