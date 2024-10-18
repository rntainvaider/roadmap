const quiz = document.querySelectorAll(".quiz");
let resultQ = 0;

for (let i = 0; i < quiz.length-1; i++) {
    let btnNext = quiz[i].querySelector(".butn");
    btnNext.addEventListener("click", () => {
        radioInput = quiz[i].querySelectorAll(".rad_inp");
        if (chack_input(radioInput)) {
            quiz[i].style.display = 'none';
            quiz[i + 1].style.display = 'flex';
            resultQ += get_value(radioInput)
        }
    })
}

let btnFinish = document.querySelector(".btnF")
const result = document.querySelector(".result");
btnFinish.addEventListener("click", () => {
    const radioInput = quiz[quiz.length - 1].querySelectorAll(".rad_inp");
    if (chack_input(radioInput)) {
        quiz[quiz.length - 1].style.display = 'none';
        result.style.display = 'flex';
        resultQ += get_value(radioInput)
        loadResult(resultQ)
    }
})

function chack_input(radioInput) {
    for (let i = 0; i < radioInput.length; i++) {
        if (radioInput[i].checked) {
            return true
        }
    }
    alert("Выберите хотя бы один ответ")
    return false
}
function loadResult(result) {
    let tex = document.querySelector('.tex');
    let s = `<p>Result: ${result} correct answers to 3 qustions</p>`
    tex.innerHTML = s;
}

function get_value(inputs) {
    for (let i = 0; i < inputs.length; i++) {
        if (inputs[i].checked){
            return parseInt(inputs[i].value);
        }
    }
}