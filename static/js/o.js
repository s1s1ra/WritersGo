function topics(ch){
  var topics;
  switch(ch){
    case 0:
      topics = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"];
      break;
    case 1:
      topics = ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"];
      break;
    case 2:
      topics = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];
      break;
    case 3:
      topics = ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"];
      break;
    case 4:
      topics = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"];
      break;
    }
    document.getElementById("demo").innerHTML = topics[Math.floor(Math.random() * 10)];
  }
