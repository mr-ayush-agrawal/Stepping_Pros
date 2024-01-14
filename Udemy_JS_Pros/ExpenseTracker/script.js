// This is incomplete as this was not a good apraocah to solve the problem -> later self solve 

// // This is not optimized program as we are rendering all the expenses insterd of adding only the last one
// const btn = document.getElementById('add')
// const list = document.querySelector('.expenseList')
// const total = document.querySelector('.total')
// let Expenses = []
// let totalAmount = 0

// btn.addEventListener('click', ()=> {
//     const disc = prompt("Enter the discription of The Expense")
//     const amt = parseFloat(prompt("Enter the Expense Amount"))
//     console.log(amt, disc)
//     if (amt && disc){
//         const exp = {
//             discription : disc,
//             Amount : amt
//         }
//         totalAmount+=amt
//     }    
//     renderExpense()
// })

// function renderExpense() {
//     let HTML = ''
//     Expenses.forEach(expense => {
//         HTML += `
//             <div class = "item">
//                 <div class="disc">${expense.discription}</div>
//                 <div class="Amount">${expense.Amount}</div>
//                 <button id="del">&times</button>
//             </div>
//         `
//     })
//     list.innerHTML = HTML
//     total.innerText = totalAmount
// }