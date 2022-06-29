  //toggle show result section
  const targetDiv = document.getElementById("compression-result");
  const submit = document.getElementById("show-button");

  submit.onclick = function() {
      const div = document.getElementById('compression-result')
      const img = document.querySelector("#file")
      console.log(img.clientHeight);

      div.classList.toggle("show")
  };

  //download compressed image section
  const btnDownload = document.querySelector("#download");
  const imgDownload = document.querySelector("#after-image");

  function getFileName(file) {
      return file.substring(file.lastIndexOf('/') + 1);
  }


  btnDownload.addEventListener('click', () => {
      const path = imgDownload.getAttribute('src');
      saveAs(path, "compressed-image");
  })