var baseimg;
var currentimg;
var fileformat;

function uploadpic() {
    document.getElementById("photoshop").style.display = "flex";
    let temp = document.getElementById("file").files[0];
    fileformat = temp.type
    if (temp) {
        let fileReader = new FileReader();
        fileReader.readAsDataURL(temp);
        fileReader.addEventListener("load", function() {
            let imgdiv = document.getElementById("psimage")
            imgdiv.innerHTML = ""
            let img = document.createElement('img');
            img.src = this.result
            baseimg = this.result
            currentimg = this.result
            imgdiv.appendChild(img)
        });
    }
}

async function edit(command) {
    let dataToSend = JSON.stringify({ "imgsource": currentimg });
    let imgdiv = document.getElementById("psimage")
    imgdiv.innerHTML = ""
    const response = await fetch('http://127.0.0.1:5000/' + command, {
        method: 'POST',
        mode: "cors",
        body: dataToSend,
        headers: {
            'Content-Type': 'application/json'
        }
    });
    let myJson = await response.json(); //extract JSON from the http response
    console.log(myJson)
        // do something with myJson
    let img = document.createElement('img');
    img.src = "data:image/" + fileformat + ";base64," + myJson["result"]
    currentimg = "data:image/" + fileformat + ";base64," + myJson["result"]
    imgdiv.appendChild(img)
}