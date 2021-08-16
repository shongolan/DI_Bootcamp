let number=window.prompt("enter starting number")
number=parseInt(number)
let subtract=1
function song(){
   while(number>0){
       if(subtract==1){
        console.log(`${number} bottles of beer on the wall`)
        console.log(`${number} bottles of beer`)
        console.log(`Take ${subtract} down, pass it around`)
        number=number-subtract
       }
       else{
        console.log(`${number} bottles of beer on the wall`)
        console.log(`${number} bottles of beer`)
        console.log(`Take ${subtract} down, pass them around`)
        number=number-subtract
       }
       subtract++
       
   }
}song()
