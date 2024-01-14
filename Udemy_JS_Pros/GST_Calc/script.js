const btn = document.querySelector("button")

btn.addEventListener('click', (e)=> {
    e.preventDefault();
    const billAmount = parseFloat(document.getElementById('Amount').value)
    const gstRate = parseFloat(document.getElementById('rate').value)

    const tipAmount = billAmount * gstRate/100
    const totalAmount = billAmount + tipAmount

    document.getElementById('GST-amount').textContent = '$ ' + tipAmount.toFixed(2);
    document.getElementById('total-amount').textContent = '$ ' + totalAmount.toFixed(2);
})