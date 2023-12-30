const lowerCase = 'qwertyuioplkjhgfdsazxcvbnm'
const upperCase = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
const number = '1234567890'
const symbols = '!@#$%^&*()_-+=<>?/\|][{}:;'

const lengthInp = document.getElementById('length')
const lowerCaseInp = document.getElementById('lowerCase')
const upperCaseInp = document.getElementById('upperCase')
const numberInp = document.getElementById('number')
const symbolsInp = document.getElementById('symbols')

const genBtn = document.getElementById('generate')
const password = document.getElementById('password')

genBtn.addEventListener('click', () => {
    const len = lengthInp.value;
    let charset = ''
    let pswd = ''

    if(lowerCaseInp.checked)
        charset+=lowerCase
    if(upperCaseInp.checked)
        charset+=upperCase
    if(numberInp.checked)
        charset+=number
    if(symbolsInp.checked)
        charset+=symbols

    for (let i=0; i<len; i++)
        pswd += charset.charAt(Math.floor(Math.random()*charset.length))

    password.value = pswd

})