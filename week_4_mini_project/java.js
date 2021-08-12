function playTheGame() {
    if (!confirm("Would you like to play the game?")) {
      alert("No problem, Goodbye");
      return;
    }
    let computerNumber = Math.round(Math.floor(Math.random() * 11));
    let usersGuessNumber;
    for (var i = 0; i < 3; i++) {
      let usersGuessNumber = getUserGuessNumber();
      if (!usersGuessNumber) return;
      if (test(usersGuessNumber, computerNumber)) return;
    }
    alert("out of chances");
    return;
  }
  function getUserGuessNumber() {
    let userGuessNumber = parseInt(
      prompt("Please enter a number between 0 and 10")
    );
    if (!userGuessNumber) {
      alert("Sorry not a number, Goodbye");
      return;
    }
    if (userGuessNumber > 10 || userGuessNumber < 0) {
      alert("Sorry not a good number, Goodbye");
      return;
    }
    return userGuessNumber;
  }
  function test(userNumber, computerNumber) {
    if (userNumber === computerNumber) {
      alert("WINNER");
      return true;
    }
    if (userNumber > computerNumber) {
      alert("Your number is bigger than the computer's, guess again");
      return false;
    }
    if (userNumber < computerNumber) {
      alert("Your number is smaller than the computer's, guess again");
      return false;
    }
  }


  
  
  //bonus second exercise
  
  function playTheGame() {
    if (!confirm("Would you like to play the game?")) {
      alert("No problem, Goodbye");
      return;
    }
    let computerNumber = Math.round(Math.floor(Math.random() * 11));
    let usersGuessNumber;
    for (var i = 0; i < 3; i++) {
      usersGuessNumber = getUserGuessNumber();
      if (test(usersGuessNumber, computerNumber)) return;
    }
    alert("out of chances");
    return;
  }
  function getUserGuessNumber() {
    let userGuessNumber;
    let isNotValidNumber;
    do {
      userGuessNumber = parseInt(
        prompt("Please enter a number between 0 and 10")
      );
      isNotValidNumber =
        !userGuessNumber || userGuessNumber > 10 || userGuessNumber < 0;
      isNotValidNumber = userGuessNumber == 0 ? false : isNotValidNumber;
      if (isNotValidNumber)
        alert(
          `Sorry the number ${userGuessNumber} not a valid number, please enter a number between 0 and 10`
        );
    } while (isNotValidNumber);
    return userGuessNumber;
  }
  function test(userNumber, computerNumber) {
    if (userNumber === computerNumber) {
      alert("WINNER");
      return true;
    }
    if (userNumber > computerNumber) {
      alert("Your number is bigger than the computer's, guess again");
      return false;
    }
    if (userNumber < computerNumber) {
      alert("Your number is smaller than the computer's, guess again");
      return false;
    }
  }