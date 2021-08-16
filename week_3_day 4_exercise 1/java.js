for (let i = 0; i <= 15; i++) {
    if (i % 2 == 0){
        console.log(`${i} odd`)
    }
    else{
        console.log(`${i} even`)

    }
}

/*let names= ["john", "sarah", 23, "Rudolf",34]
for (let = 0; i < names.length; i++) {
}*/

/*function computeage(myAge){
    var dadage = 1.2 + myAge
    console.log(`my mum age is ${myAge} and my dad age is ${dadage}`)

}
computeage(20)*/

function age(myAge){
    return myAge*2
}
console.log(age(20))
