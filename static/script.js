function reloadPage() {
  location.reload();
}

function uploadImage() {
  var input = document.getElementById('image-input');
  var resultDiv = document.getElementById('result');
  var uploadedImageContainer = document.getElementById('uploaded-image-container');

  if (input.files.length > 0) {
     var file = input.files[0];
     var fileName = file.name;

     resultDiv.innerHTML = 'File Name: ' + fileName;

     // Create a new image element
     var uploadedImage = new Image();

     // Use a FileReader to set the src attribute
     var reader = new FileReader();
     reader.onload = function (e) {
        uploadedImage.src = e.target.result;
        uploadedImage.style.maxWidth = '100%';
        uploadedImage.style.maxHeight = '300px'; // Adjust as needed

        // Append the image to the container
        uploadedImageContainer.innerHTML = ''; // Clear previous content
        uploadedImageContainer.appendChild(uploadedImage);
     };

     reader.readAsDataURL(file);
  } else {
     resultDiv.innerHTML = 'Please select an image.';
     uploadedImageContainer.innerHTML = ''; // Clear previous content
  }
}

var loader = document.getElementById("pre");
window.addEventListener("load", function(){
   loader.style.display='none';
})

