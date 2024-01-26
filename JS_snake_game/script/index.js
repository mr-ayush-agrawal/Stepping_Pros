// Defining the HTML elements which we are going to manipulate
const board = document.getElementById('game-board')
const instructions = document.getElementById('instructions')
const logo = document.getElementsByClassName('logo')[0]
const score = document.getElementById('currScore')
const highScoreText = document.getElementById('highScore')

// Game Variables
const gridSize = 20;
let snake = [{ x: parseInt((gridSize + 1) / 2), y: parseInt((gridSize + 1) / 2) }]
let food = generateFood()
let gameInterval;
let direction = 'r';
let gameSpeed = 200;
let start = false;
let highScore = 0;

// Draw Game map -> Draws snake and food
function draw() {
    board.innerHTML = '';
    drawSnake();
    drawFood();
    updateScore();
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
    if (start) {
        const foodEle = createEle('div', 'food');
        setPosition(foodEle, food);
        board.appendChild(foodEle);
    }
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
        incSpeed()
        clearInterval(gameInterval);  // Clearing clear past interval
        gameInterval = setInterval(() => {
            move();
            checkCollision();
            draw();
        }, gameSpeed)
    }
    else
        snake.pop();
}

function startGame() {
    start = true;
    instructions.style.display = 'none';
    logo.style.display = 'none';
    gameInterval = setInterval(() => {
        move();
        checkCollision();
        draw();
    }, gameSpeed)
}

function incSpeed() {
    if (gameSpeed > 150) {
        gameSpeed -= 5;
    }
    else if (gameSpeed > 100)
        gameSpeed -= 3;
    else if (gameSpeed > 50)
        gameSpeed -= 2;
    else if (gameSpeed > 25)
        gameSpeed -= 1;
}


// KeyPress event listner
function handleKey(e) {
    if ((!start && e.code === 'Space') || (!start && e.key === ' ')) {
        startGame()
    }
    switch (e.key) {
        case 'ArrowUp': if(direction!='d') direction = 'u'; break;
        case 'ArrowDown': if(direction!='u') direction = 'd'; break;
        case 'ArrowRight': if(direction!='l') direction = 'r'; break;
        case 'ArrowLeft': if(direction!='r') direction = 'l'; break;
    }
}

function checkCollision() {
    const head = snake[0]
    if (head.x < 1 || head.x > gridSize || head.y > gridSize || head.y < 1)
        resetGame();

    for (let i = 1; i < snake.length; i++) {
        if (head.x == snake[i].x && head.y == snake[i].y)
            resetGame()
    }
}

function resetGame() {
    // updateScore();
    updateHigh();
    stopGame();
    gameSpeed = 200;
    snake = [{ x: 10, y: 10 }];
    food = generateFood();
    direction = 'r';
}

function updateScore() {
    currScore = snake.length - 1;
    score.innerHTML = currScore.toString().padStart(3, " ");
}

function updateHigh() {
    const currScore = snake.length - 1
    if (currScore > highScore)
        highScore = currScore

    highScoreText.textContent = highScore.toString()
    highScoreText.style.display = 'block'
}

function stopGame() {
    clearInterval(gameInterval)
    start = false;
    instructions.style.display = 'block'
    logo.style.display = 'block'
}

// TEST

document.addEventListener('keydown', handleKey)