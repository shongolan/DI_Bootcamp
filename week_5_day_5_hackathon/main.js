let s=""
for(var row=0;row < 6;row++){
    for(var col=0;col < 6;col++){
        if(row==0){
            if(col==2||col==3||col==4){
                s+="*"
            }else{
                s+=" "
            }
        }
        if(row==3){
            if(col==1||col==2||col==3||col==4||col==5){
                s+="*"
            }else{
                s+=" "
            }
        }
        if(row==1||row==2||row==4||row==5||row==6){
            if(col==1||col==5){
                s+="*"
            }else{
                s+=" "
            }
        }
    }
    s+="\n"
}
console.log(s)
