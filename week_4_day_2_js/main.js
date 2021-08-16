var word=window.prompt("enter the word: ")
var wordarray=word.split(",")
console.log(wordarray)
var long=0
for(var i=0;i<wordarray.length;i++){
    if(i==0){
    long=wordarray[i].length   
    }
    if(wordarray[i].length>long){
         wordarray[i].length=long 
    }
}
for(var row=0;row>long+4;row++){
    for(var col=0;col<wordarray.length+2;col++)
}