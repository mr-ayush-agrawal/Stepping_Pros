const list = document.querySelector('ul')
const btn = document.querySelector('button')
const inp = document.querySelector('input') 

btn.addEventListener('click', () => {
    const task = inp.value
    if (task) {
        const li = document.createElement('li')
        li.innerText = task
        // adding delete button
        const delBtn = document.createElement('button')
        delBtn.innerText= 'X'
        delBtn.classList.add('deleteButton')
        delBtn.addEventListener('click', () => {
            li.remove()
        })
        li.appendChild(delBtn)
        list.appendChild(li)
        inp.value = ""
    }
})