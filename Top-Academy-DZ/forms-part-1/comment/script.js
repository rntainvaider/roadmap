const BTN = document.querySelector(".btn_send");
const divBoxs = document.querySelector(".boxs");
const yourName = document.querySelector("#name");
const container = document.querySelector(".container");
const message = document.querySelector("#message")
let x = 0;

function test() {
    if (yourName.value === "") {
        alert("Введите имя")
        return false
    } else if (message.value === "") {
        alert("Введите сообщение")
        return false
    }
    return true
}

BTN.addEventListener("click", () => {
    const newDate = new Date().toLocaleString();
    if (test()) {
        let box = document.createElement("div");
        box.className = "boxs";
        container.appendChild(box)
    
        let boxs = document.createElement("div");
        boxs.className = "name_data";
        box.appendChild(boxs)
    
        let spanName = document.createElement("span");
        spanName.className = "name";
        let spanDate = document.createElement("span");
        spanDate.className = "data_time";
        boxs.append(spanName);
        boxs.append(spanDate);
        spanName.textContent = yourName.value;
        spanDate.textContent = newDate;
    
        let messageText = document.createElement("div");
        messageText.className = "comment";
        box.appendChild(messageText)
        let tegP = document.createElement("p");
        messageText.append(tegP);
        tegP.textContent = message.value;
    }
})