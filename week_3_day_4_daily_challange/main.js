let wordNot = "not"
let wordBad = "bad"
let sentence = `The movie is ${wordNot} that ${wordBad}, I like it`
let str = sentence.indexOf(wordNot)
if(str>-1){
    sentence = `The movie is good, I like it`
    console.log(sentence)
    console.log("the movie is "+wordNot+" .that "+wordBad+" I like it") //Concatination (combination of string).
}
else{
    console.log(sentence)
}