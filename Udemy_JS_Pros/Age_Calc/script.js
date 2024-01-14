const dobInp = document.getElementById('dob')
const calcbtn = document.getElementById('calcbtn')
const resDiv = document.getElementById('result')

calcbtn.addEventListener('click', () => {
    const dob = new Date(dobInp.value)
    const ageM = Date.now() - dob.getTime()
    const ageD = new Date(ageM)
    const age = Math.abs(ageD.getUTCFullYear()-1970)
    resDiv.innerHTML = `Your Age is ${age} years.`
    console.log(age)
})