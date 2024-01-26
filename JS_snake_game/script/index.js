// Defining the HTML elements which we are going to manipulate
const board = document.getElementById('game-board')
const instructions = document.getElementById('instructions')
const logo = document.getElementsByClassName('logo')[0]

// Game Variables
const gridSize = 20;
let snake = [{ x: parseInt((gridSize + 1) / 2), y: parseInt((gridSize + 1) / 2) }]
let food = generateFood()
let gameInterval;
let direction = 'r';
let gameSpeed = 200;
let start = false;


// Draw Game map -> Draws snake and food
function draw() {
    board.innerHTML = '';
    drawSnake();
    drawFood();
}

function drawSnake() {
    snake.forEach((segment) => {
        const snakeEle = createEle('div', 'snake')
        setPosition(snakeEle, segment);
        board.appendChild(snakeEle);
    });
}

// Functions creates snake/food div
function createEle(tag, className) {
    const ele = document.createElement(tag);
    ele.className = className;
    return ele;
}

// setting the postition 
function setPosition(ele, pos) {
    ele.style.gridColumn = pos.x;
    ele.style.gridRow = pos.y;
}

function drawFood() {
    const foodEle = createEle('div', 'food');
    setPosition(foodEle, food);
    board.appendChild(foodEle);

}

function generateFood() {
    const x = Math.floor((Math.random() * gridSize) + 1);
    const y = Math.floor((Math.random() * gridSize) + 1);
    return { x, y };
}

// Moving the snake
function move() {
    const head = { ...snake[0] }
    switch (direction) {
        case 'r':
            head.x++;
            break;
        case 'l':
            head.x--;
            break;
        case 'u':
            head.y--;
            break;
        case 'd':
            head.y++;
            break;
    }
    snake.unshift(head);
    if (head.x === food.x && head.y === food.y) {
        food = generateFood()
    }
    else
        snake.pop();

    clearInterval();  // Clearing clear past interval
}

function startGame() {
    start = true;
    instructions.style.display = 'none';
    logo.style.display = 'none';
    incSpeed()
    gameInterval = setInterval( ()=> {
        move();
        // checkCollision();   
        draw();
    }, gameSpeed)
}



// KeyPress event listner
function handleKey(e) {
    if((!start && e.code === 'Space') || (!start && e.key  === ' ')){
        startGame()
    }
    switch(e.key){
        case 'ArrowUp': direction = 'u'; break;
        case 'ArrowDown': direction = 'd'; break;
        case 'ArrowRight': direction = 'r'; break;
        case 'ArrowLeft': direction = 'l'; break;
    }
}

// TEST

document.addEventListener('keydown', handleKey)