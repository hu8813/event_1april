<?php

function inputPlayer() {
    fwrite(STDOUT, 'Choose rock, paper, or scissors: ');
    $player1 = strtolower(trim(fgets(STDIN)));
    return $player1;
}

function playGame() {
    $player1 = inputPlayer();
    $playerarr = ["rock", "paper", "scissors"];
    $player2 = $playerarr[rand(0,2)];
    if ($player1 == $player2) {
        echo "It's a draw! Game will continue till there's a winner.\n";
        playGame();
    } elseif ($player1 == 'rock' && $player2 == 'scissors') {
        echo "Congratulations! You won! The computer chose $player2.";
    } elseif ($player1 == 'rock' && $player2 == 'paper') {
        echo "Sorry, you lost. The computer chose $player2";
    } elseif ($player1 == 'paper' && $player2 == 'rock') {
        echo "Congratulations! You won! The computer chose $player2.";
    } elseif ($player1 == 'paper' && $player2 == 'scissors') {
        echo "Sorry, you lost. The computer chose $player2";
    } elseif ($player1 == 'scissors' && $player2 == 'paper') {
        echo "Congratulations! You won! The computer chose $player2.";
    } elseif ($player1 == 'scissors' && $player2 == 'rock') {
        echo "Sorry, you lost. The computer chose $player2";
    } else {
        echo "Invalid input!";
    }
    echo "\n";
}

playGame();
?>