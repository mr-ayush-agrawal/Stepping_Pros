function calcAmt () {
    // Getting the input
    const princ = parseFloat(document.getElementById('principal').value)
    const interest = parseFloat(document.getElementById('interest').value)
    const tenure = parseFloat(document.getElementById('tenure').value)

    console.log(tenure)

    // performing calc
    const mitAmt = princ + (princ*interest*tenure)/100
    document.getElementById('result').innerText = `Maturity Ammount ₹${mitAmt.toFixed(2)}`
}

document.getElementsByClassName('calcBtn')[0].addEventListener('click',calcAmt)
// console.log(document.getElementsByClassName('calcBtn'))