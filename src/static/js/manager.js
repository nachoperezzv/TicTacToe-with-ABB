"use strict";

window.addEventListener('load', app);

var gameBoard = ['', '', '', '', '', '', '', '', '']; 
var mode = '1';
var turn = 0; // Keeps track if X or O player's turn
var winner = false;


// CREATE PLAYER
const player = (name) => {
  name = name;
  return {name};
};

var playerX = player("");
var playerY = player("");

// NUMBER OF PLAYERS
document.querySelector('#playmode-oneplayer-btn').onclick = () => {
  mode = '1';
  let data = {GameMode: mode};

  fetch('http://localhost:5000/play/GameMode', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(result => {
    console.log(result)
  })
  .catch(error => {
    console.error(error);
  });
}

document.querySelector('#playmode-twoplayers-btn').onclick = () => {
  mode = '2';
  let data = {GameMode: mode};

  fetch('http://localhost:5000/play/GameMode', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(result => {
    console.log(result)
  })
  .catch(error => {
    console.error(error);
  });
}

 // INITIALIZE APP
function app() {
  let inputField = document.querySelector('.input-field').focus();

  const addPlayerForm = document.getElementById('player-form');
  addPlayerForm.addEventListener('submit', addPlayers);

  let replayButton = document.querySelector('.replay-btn');
  replayButton.addEventListener('click', resetBoard);
}

// Add PLAYERS
function addPlayers(event) {
  event.preventDefault();

  if (this.player1.value === '' || this.player2.value === '') {
    alert('Porfavor rellena todos los campos');
    return;
  }

  const playerFormContainer = document.querySelector('.enter-players');
  const boardMain = document.querySelector('.board__main');
  
  playerFormContainer.classList.add('hide-container');
  boardMain.classList.remove('hide-container');

  playerX.name = this.player1.value;
  if(mode == '1'){
    playerY.name = 'CPU';
  } else{
    playerY.name = this.player2.value;
  }

  buildBoard();
}

// RETURN CURRENT PLAYER
function currentPlayer() {
  return turn % 2 === 0 ? 'X' : 'O';
}

// Resize squares in event browser is resized
window.addEventListener("resize", onResize);
function onResize() {
  let allCells = document.querySelectorAll('.board__cell');
  let cellHeight = allCells[0].offsetWidth;
  
  allCells.forEach( cell => {
    cell.style.height = `${cellHeight}px`;
  });
}

// Build Board
function buildBoard() {
  let resetContainer = document.querySelector('.reset');
  resetContainer.classList.remove('reset--hidden');

  onResize();
  addCellClickListener();
  changeBoardHeaderNames();
}

// CELL CLICK EVENT FOR PLAYER TO ATTEMPT TO MAKE MOVE AND RESOLVE CPU MOVE
function getMove(event){

  let currentCell = parseInt(event.currentTarget.firstElementChild.dataset.id);
  let cellToAddToken = document.querySelector(`[data-id='${currentCell}']`);

  let p = currentPlayer() 

  if (currentPlayer() === 'X') {
    p = 1
  } else {
    p = 2
  }
  
  let pos = "0"
  switch (currentCell) {
    case 0:
      pos = "A1";
      break;
    case 1:
      pos = "A2";
      break;
    case 2:
      pos = "A3";
      break;
    case 3:
      pos = "B1";
      break;
    case 4:
      pos = "B2";
      break;
    case 5:
      pos = "B3";
      break;
    case 6:
      pos = "C1";
      break;
    case 7:
      pos = "C2";
      break;
    case 8:
      pos = "C3";
      break;
    default:
      pos = "00"
      break;
  }

  let data = {player: p,
              position: pos};

  fetch('http://localhost:5000/play/move', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(result => {
    console.log(data)
    console.log(result);
    isWinner();
    if (result["0"] !== 'Game Over'){
      makeCPUMove(result["1"]);
    }
  })
  .catch(error => {
    console.error(error);
  });

  if (cellToAddToken.innerHTML !== '') {
    console.log('Esta celda esta ocupada');
    return;
  } else {
    cellToAddToken.textContent = currentPlayer();
    gameBoard[currentCell] = 'X';
  }

  turn++;

  // CHECK IF WE HAVE A WINNER
  isWinner();
  
  // CHANGE BOARD HEADER INFO
  changeBoardHeaderNames();
}

// FUNCTION TO RECEIVE CPU TOKEN POSITION & SHOW IT
function makeCPUMove(cpu_cell) {

  let cpu_pos = 0;

  switch (cpu_cell) {
    case "A1":
      cpu_pos = 0;
      break;
    case "A2":
      cpu_pos = 1;
      break;
    case "A3":
      cpu_pos = 2;
      break;
    case "B1":
      cpu_pos = 3;
      break;
    case "B2":
      cpu_pos = 4;
      break;
    case "B3":
      cpu_pos = 5;
      break;
    case "C1":
      cpu_pos = 6;
      break;
    case "C2":
      cpu_pos = 7;
      break;
    case "C3":
      cpu_pos = 8;
      break;
    default:
      cpu_pos = -1
      break;
  }

  let cellToAddTokenCPU = document.querySelector(`[data-id='${cpu_pos}']`);
  cellToAddTokenCPU.textContent = 'O';
  gameBoard[cpu_pos] = 'O';

  // CHECK IF WE HAVE A WINNER
  isWinner();
    
  // Update turn count so next player can choose
  turn ++;

  // CHANGE BOARD HEADER INFO
  changeBoardHeaderNames();
}

// CELL CLICK EVENT FOR PLAYER TO ATTEMPT TO MAKE MOVE
function makeMove(event) {
  
  let currentCell = parseInt(event.currentTarget.firstElementChild.dataset.id);
  let cellToAddToken = document.querySelector(`[data-id='${currentCell}']`);
  
  let p = currentPlayer() 

  if (currentPlayer() === 'X') {
    p = 1
  } else {
    p = 2
  }
  
  let pos = "0"
  switch (currentCell) {
    case 0:
      pos = "A1";
      break;
    case 1:
      pos = "A2";
      break;
    case 2:
      pos = "A3";
      break;
    case 3:
      pos = "B1";
      break;
    case 4:
      pos = "B2";
      break;
    case 5:
      pos = "B3";
      break;
    case 6:
      pos = "C1";
      break;
    case 7:
      pos = "C2";
      break;
    case 8:
      pos = "C3";
      break;
    default:
      pos = "00"
      break;
  }

  let data = {player: p,
              position: pos};

  fetch('http://localhost:5000/play/move', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(result => {
    console.log(result)
  })
  .catch(error => {
    console.error(error);
  });

  if (cellToAddToken.innerHTML !== '') {
    console.log('Esta celda esta ocupada');
    return;
  } else {
    if (currentPlayer() === 'X') {
      cellToAddToken.textContent = currentPlayer();
      gameBoard[currentCell] = 'X';

      data = {
        'player':'1',
        'position': currentCell
      }

      fetch('http://localhost:5000/play/GameMode', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(result => {
      console.log(result)
    })
    .catch(error => {
      console.error(error);
    });
      

    } else {
      cellToAddToken.textContent = currentPlayer();
      gameBoard[currentCell] = 'O';
    }
  }
    
  // CHECK IF WE HAVE A WINNER
  isWinner();
    
  // Update turn count so next player can choose
  turn ++;

  // CHANGE BOARD HEADER INFO
  changeBoardHeaderNames();
}

function checkIfTie() {
  if (turn > 7) {
    alert('Ya has llenado todas las casillas. Es un empate!!')
  }
}

function isWinner() {
  const winningSequences = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ];

  winningSequences.forEach( winningCombos => {
    let cell1 = winningCombos[0];
    let cell2 = winningCombos[1];
    let cell3 = winningCombos[2];
    if (
      gameBoard[cell1] === currentPlayer() &&
      gameBoard[cell2] === currentPlayer() &&
      gameBoard[cell3] === currentPlayer()
    ) {

      
      const cells = document.querySelectorAll('.board__cell');
      let letterId1 = document.querySelector(`[data-id='${cell1}']`);
      let letterId2 = document.querySelector(`[data-id='${cell2}']`);
      let letterId3 = document.querySelector(`[data-id='${cell3}']`);
      
      cells.forEach( cell => {
        let cellId = cell.firstElementChild.dataset.id;	

        if (cellId == cell1 || cellId == cell2 || cellId == cell3 ) {
          cell.classList.add('board__cell--winner');
        }
      });

      let currentPlayerText = document.querySelector('.board___player-turn');
      if (currentPlayer() === 'X') {
        currentPlayerText.innerHTML = `
          <div class="congratulations">Felicidades ${playerX.name}</div>
          <div class="u-r-winner">Eres el ganador!</div>
        `;
        winner = true;
        removeCellClickListener();
      } else {
        currentPlayerText.innerHTML = `
          <div class="congratulations">Felicidades ${playerY.name}</div>
          <div class="u-r-winner">Eres el ganador!</div>
        `;
        winner = true;
        removeCellClickListener();
      }
    }
  });

  if (!winner) {
    checkIfTie();
  }
  
  return winner;
}

function changeBoardHeaderNames() {
  if (!winner) {
    let currentPlayerText = document.querySelector('.board___player-turn');
    if (currentPlayer() === 'X') {
      currentPlayerText.innerHTML = `
        <span class="name--style">${playerX.name}</span>, te toca.
        <div class="u-r-winner"></div>
      `
    }  else {
      currentPlayerText.innerHTML = `
        <span class="name--style">${playerY.name}</span>, te toca.
        <div class="u-r-winner"></div>
      `
    }
  }
}

function resetBoard() {
  console.log('resetting');

  let data = {N: "None"};
  fetch('http://localhost:5000/play/ResetBoard', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(result => {
    console.log(result)
  })
  .catch(error => {
    console.error(error);
  });
  
  gameBoard = ['', '', '', '', '', '', '', '', '']; 
  
  let cellToAddToken = document.querySelectorAll('.letter');
  cellToAddToken.forEach( square => {
    square.textContent = '';
    square.parentElement.classList.remove('board__cell--winner');
  });

  turn = 0;
  winner = false;

  let currentPlayerText = document.querySelector('.board___player-turn');
  currentPlayerText.innerHTML = `
    <span class="name--style">${playerX.name}</span>, empiezas tu!
    <div class="u-r-winner"></div>
  `
  
  addCellClickListener();
}

function addCellClickListener() {
  
  const cells = document.querySelectorAll('.board__cell');
  
  if(mode == '1'){
    cells.forEach( cell => {
      cell.addEventListener('click', getMove);
    });
  }else{
    cells.forEach( cell => {
      cell.addEventListener('click', makeMove);
    });
  }
  
}

function removeCellClickListener() {
  let allCells = document.querySelectorAll('.board__cell');
  if(mode == '1'){
    allCells.forEach( cell => {
      cell.removeEventListener('click', getMove);
    });
  }else{
    cells.forEach( cell => {
      cell.addEventListener('click', makeMove);
    });
  }
}

