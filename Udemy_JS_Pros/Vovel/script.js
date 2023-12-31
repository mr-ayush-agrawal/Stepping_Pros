function isVovel (char){
    const vovels = ['a','e','i','o','u']
    return vovels.includes(char)
}

document.querySelector('button').addEventListener('click', ()=> {
    let text = document.getElementById('text').value.toLowerCase()
    let vovCount = 0;
    for (const char of text) {
        if (isVovel(char))
            vovCount++;
    }

    // Need to update the reult
    document.getElementById('result').textContent = `Total Vovels in text is ${vovCount}`
})