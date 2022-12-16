// import {language} from "./language"
// import {dialect} from "./language"

const coordinates = [ 'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'];

if ("webkitSpeechRecognition" in window) {
  let speechRecognition = new webkitSpeechRecognition();
  let final_transcript = "";
  let lastCoordinate = "";    // Ultima coordenada encontrada en final_transcript

  speechRecognition.continuous = true;
  speechRecognition.interimResults = true;
  speechRecognition.lang = 'es-ES'

  // speechRecognition.lang = document.querySelector("#select_dialect").value;

  speechRecognition.onstart = () => {
    //document.querySelector("#status").style.display = 'block';
  };
  speechRecognition.onerror = () => {
    //document.querySelector("#status").style.display = 'none';
    console.log("Speech Recognition Error");
  };
  speechRecognition.onend = () => {
    //document.querySelector("#status").style.display = 'none';
    console.log("Speech Recognition Ended");

    lastCoordinate = "none"
    for(let i = 0; i<coordinates.length; i++){
      if (final_transcript.includes(coordinates[i])){
        lastCoordinate = coordinates[i];
      }
    }
    
    if (lastCoordinate != "none"){

      let cpu_pos="";

      switch (lastCoordinate) {
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
      let cellToAddToken = document.querySelector(`[data-id='${cpu_pos}']`);

      // Imprime coordenada encontrada
      console.log("Coordinate: " + lastCoordinate);

      // Identificacion de jugador
      let p = currentPlayer() 
      if (currentPlayer() === 'X') {
        p = 1
      } else {
        p = 2
      }

      let data = {player: p,
        position: lastCoordinate};
      
      if (cellToAddToken.innerHTML == ''){
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
            console.log("result: " + result["1"]);
            makeCPUMove(result["1"]);
          }
        })
        .catch(error => {
          console.error(error);
        });

        cellToAddToken.textContent = currentPlayer();
        gameBoard[cpu_pos] = 'X';

        turn++;
    
        // CHECK IF WE HAVE A WINNER
        isWinner();
        
        // CHANGE BOARD HEADER INFO
        changeBoardHeaderNames();

      } else {
        console.log('Esta celda esta ocupada');
        return;
      }
    }
  }

  speechRecognition.onresult = (event) => {
    let interim_transcript = "";

    for (let i = event.resultIndex; i < event.results.length; ++i) {
      if (event.results[i].isFinal) {
        final_transcript += event.results[i][0].transcript;
      } else {
        interim_transcript += event.results[i][0].transcript;
      }
    }
    document.querySelector("#final").innerHTML = final_transcript;
    document.querySelector("#interim").innerHTML = interim_transcript;
  };

  document.querySelector("#btn__mic__start").onclick = () => {
    document.querySelector("#btn__mic__start").style.display = 'none'
    document.querySelector("#btn__mic__stop").style.display = 'block'

    document.querySelector("#final").innerHTML = "";
    final_transcript = "";
    lastCoordinate = "";

    document.querySelector("#interim").innerHTML = "";
    interim_transcript = "";

    speechRecognition.start();
  };

  document.querySelector("#btn__mic__stop").onclick = () => {
    document.querySelector("#btn__mic__start").style.display = 'block'
    document.querySelector("#btn__mic__stop").style.display = 'none'

    speechRecognition.stop();
  };
} else {
  console.log("Speech Recognition Not Available");
}
