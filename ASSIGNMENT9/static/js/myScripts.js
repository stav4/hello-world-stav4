function DarkerColor(x){
    document.getElementById(x).style.backgroundColor = "rgba(222, 245, 247, 0.6)";
 }
 function LighterColor(x){
    document.getElementById(x).style.backgroundColor = "rgba(255, 255, 255, 0.50)";
 }
function SendMessage(){
   alert("Thank you for messsging me!");
   document.getElementById("afterSend").innerHTML= "Your message has been successfully sent!";

}