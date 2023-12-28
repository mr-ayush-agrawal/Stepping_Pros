// initalizing the package
const input = require('prompt-sync')()

// Making the symbols and setting the value 
const SYM_Count = {
    'A': 4,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 6,
    'X': 1
}
const SYM_val = {
    'A': 3,
    'B': 7,
    'C': 5,
    'D': 2,
    'E': 1.5,
    'X': 10

}

const symbols = []
for (const [sym, ct] of Object.entries(SYM_Count)) {
    // console.log(sym,ct)
    for (let i = 0; i < ct; i++)
        symbols.push(sym)
}

const deposit = () => {
    do {
        let totalMoney = parseFloat(input("Enter the amount to start : "))
        if (isNaN(totalMoney) || totalMoney <= 0)
            console.log('Invalid deposit, Try again')
        else
            return totalMoney
    } while (true)
}
const getNumberOfLines = () => {
    do {
        let lines = parseInt(input("Enter the Number of lines (1,2,3) : "))
        if (isNaN(lines) || lines <= 0 || lines > 3)
            console.log('Invalid lines, Try again')
        else
            return lines
    } while (true)
}
const getBetAmmount = (balance, lines) => {
    do {
        let bet = parseFloat(input("Enter the bet ammount per line : "))
        if (isNaN(bet) || bet <= 0 || bet > balance / lines)
            console.log('Invalid bet ammount per line, Try again')
        else
            return bet
    } while (true)
}

const spin = () => {
    const reel = []
    // Taking 3 Rows and 3 Columns
    for (let i = 0; i < 3; i++) {
        reel.push([])
        let avlsym = [...symbols]
        for (let j = 0; j < 3; j++) {
            const randIdx = Math.floor(Math.random() * avlsym.length)
            const sym = avlsym[randIdx]
            reel[i].push(sym)
            avlsym.splice(randIdx, 1)
        }
    }
    // Now we need to Transpose the reel
    // WE have [[1,2,3],[1,2,3],[3,1,2]]

    const slotWheel = [[], [], []]
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++)
            slotWheel[i][j] = reel[j][i]
    }
    return slotWheel
}

const printWheel = (wheel) => {
    for (let i = 0; i < 3; i++) {
        let rowString = ''
        for (let j = 0; j < 3; j++) {
            rowString += wheel[i][j];
            if (j != 2)
                rowString += ' | '
        }
        console.log(rowString)
    }
}

function checkWin(wheel, lines, bet) {
    let Winnings = 0;
    for (let row = 0; row < lines; row++) {
        const sym = wheel[row]
        let allSame = true

        for (sm of sym) {
            if (sm != sym[0]) {
                allSame = false
                break
            }
        }

        if (allSame) {
            Winnings += bet * SYM_val[sym[0]]
        }
    }

    return Winnings;
}

function game() {
    let balance = deposit()
    while (true) {
        console.log('Current Balance : ', balance)
        let numLines = getNumberOfLines()
        let betAmmount = getBetAmmount(balance, numLines)
        balance -= betAmmount * numLines
        const w = spin()
        printWheel(w)
        let winnings = checkWin(w, numLines, betAmmount)
        console.log('you won $', winnings)
        balance += winnings
        
        if (balance <= 0){
            console.log('You Ran out of balacne');
            break
        }
        const playAgain = input('To play again press Y ')
        console.log(playAgain)
        if (!(playAgain == 'Y' || playAgain == 'y'))
            break
    }
}

game()