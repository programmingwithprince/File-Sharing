const dropArea = document.querySelector(".drop_box"),
  button = document.getElementById("choose");
(list = document.getElementById("list")),
  (dragText = dropArea.querySelector("header")),
  (input = document.getElementById("input"));
let file;
var filename;
var formData;
var urls;
button.onclick = () => {
  input.click();
};

input.addEventListener("change", function (e) {
  var fileName = e.target.files[0].name;
  button.style.display = "none";
  let filedata = `

    <div class="form">
    <h4>${fileName}</h4>
    <input type="email" disabled placeholder="${fileName}">
    <button onclick="upload()" class="btn">Upload</button>
    </div>
    `;
  dropArea.innerHTML = filedata;
  const file = e.target.files[0];
  formData = new FormData();
  formData.append("file", file);
});
setInterval(function () {
  fetch("/get_urls")
    .then(function (resp) {
      // body...
      return resp.json();
    })
    .then(function (data) {
      urls = data;
      console.log(data);
      //document.write(data)

      array = urls.toString().split(",");
      let inner = "";
      //document.write(array)
      //alert(array)
      for (let i = 0; i < array.length; i++) {
        inner += `<li><a style="text-decoration:none;" href="${
          document.URL
        }download/${array[i]}"><span href="#" >${i + 1}</span> ${
          array[i]
        }</li>`;
      }
      list.innerHTML = inner;
    });
}, 2000);
function upload() {
  // functio
  console.log("uploading");
  dropArea.innerHTML = "<h3>File started uploading to to the server...</h3>";
  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then((response) => {
      if (response.ok) {
        dropArea.innerHTML = "<h3>File Uploaded successfully!</h3>";
        return response.json();
      } else {
        // throw new Error("File upload failed");
        dropArea.innerHTML = "<h3>File upload failed</h3>";
      }
    })
    .then((data) => {
      dropArea.innerHTML = "<h3>File Uploaded successfully!</h3>";
      console.log("Server response:", data);
    })
    .catch((error) => {
      console.error("Error uploading file:", error);
    });
  // dropArea.innerHTML = "<h3>File Uploaded successfully!</h3>";
}
