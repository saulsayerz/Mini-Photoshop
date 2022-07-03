var baseimg;
var currentimg;
var fileformat;
var filename;
var arrimg;
var step;

function uploadpic() {
    arrimg = new Array()
    document.getElementById("photoshop").style.display = "flex";
    let temp = document.getElementById("file").files[0];
    fileformat = temp.type
    filename = temp.name
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
            step = 0
            arrimg.push(baseimg)
            console.log(arrimg)
        });
    }
}

async function edit(command) {
    arrimg = arrimg.slice(0, step + 1)
    let dataToSend = JSON.stringify({ "imgsource": currentimg });
    let imgdiv = document.getElementById("psimage")
    const response = await fetch('http://127.0.0.1:5000/' + command, {
        method: 'POST',
        mode: "cors",
        body: dataToSend,
        headers: {
            'Content-Type': 'application/json'
        }
    });
    let myJson = await response.json();
    imgdiv.innerHTML = ""
    step += 1
    let img = document.createElement('img');
    img.src = "data:image/" + fileformat + ";base64," + myJson["result"]
    currentimg = "data:image/" + fileformat + ";base64," + myJson["result"]
    arrimg.push(currentimg)
    console.log(arrimg)
    imgdiv.appendChild(img)
}

function reset() {
    arrimg = arrimg.slice(0, 1)
    step = 0
    currentimg = baseimg
    let imgdiv = document.getElementById("psimage")
    imgdiv.innerHTML = ""
    let img = document.createElement('img');
    img.src = baseimg
    imgdiv.appendChild(img)
}

function undo() {
    if (step > 0) {
        step -= 1
        currentimg = arrimg[step]
        let imgdiv = document.getElementById("psimage")
        imgdiv.innerHTML = ""
        let img = document.createElement('img');
        img.src = currentimg
        imgdiv.appendChild(img)
    }
}

function redo() {
    if (step < arrimg.length - 1) {
        step += 1
        currentimg = arrimg[step]
        let imgdiv = document.getElementById("psimage")
        imgdiv.innerHTML = ""
        let img = document.createElement('img');
        img.src = currentimg
        imgdiv.appendChild(img)
    }
}

function save() {
    const linkSource = currentimg;
    const downloadLink = document.createElement("a");
    downloadLink.href = linkSource;
    downloadLink.download = filename.split('.')[0] + "-edited";
    downloadLink.click();
}