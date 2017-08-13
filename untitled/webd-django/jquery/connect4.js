var p1 = prompt("Player 1:Enter your name:");
var p1Color = prompt("Pick a color of your choice:");

var p2 = prompt("Player 2:Enter your name:");
var p2Color = prompt("Pick a color of your choice:");

var game_over = false;

var table = $('table tr');

function changeColor(i,j,color){
	return table.eq(i).find('td').eq(j).find('button').css('background',color);
}

function returnColor(i,j){
	return table.eq(i).find('td').eq(j).find('button').css('background-color');
}

function checkBottom(j){
	var colorReport = returnColor(5,j);
	for(var i = 5; i > -1 ; i--){
		colorReport = returnColor(i,j);
		if (colorReport === 'rgb(181, 188, 182)')
			return i;
	}
}

function colorMatch(one,two,three,four){
	return (one===two && one===three && one===four && one!='rgb(181, 188, 182)' && one!=undefined);
}

function horiCheck(){
	for (var i = 0; i < 6; i++) {
		for (var j = 0; j < 4 ; j++) {
			if (colorMatch(returnColor(i,j),returnColor(i,j+1),returnColor(i,j+2),returnColor(i,j+3)))
				return true;		
		}
	}
}

function vertiCheck(){
	for (var i = 0; i < 7; i++) {
		for (var j = 0; j < 3 ; j++) {
			if (colorMatch(returnColor(j,i),returnColor(j+1,i),returnColor(j+2,i),returnColor(j+3,i)))
				return true;		
		}
	}
}

function diagCheck() {
  for (var col = 0; col < 5; col++) {
    for (var row = 0; row < 7; row++) {
      if (colorMatchCheck(returnColor(row,col), returnColor(row+1,col+1) ,returnColor(row+2,col+2), returnColor(row+3,col+3))) {
        return true;
      }else if (colorMatchCheck(returnColor(row,col), returnColor(row-1,col+1) ,returnColor(row-2,col+2), returnColor(row-3,col+3))) {
        return true;
      }else {
        continue;
      }
    }
  }
}

var current = -1;
var currentName = p2;
var currentColor = p2Color;

$('.board button').on('click',function(){

	while(!game_over){

		current = current * -1;
		if(current === -1){
			var currentName = p2;
			var currentColor = p2Color;
			$('h4').text(p2 + " it is your turn!")
		}
		if(current === 1){
			var currentName = p1;
			var currentColor = p1Color;
			$('h4').text(p1 + " it is your turn!")
		}

		var j = $(this).closest('td').index();
		var bottomAvail = checkBottom(j);
		changeColor(bottomAvail,j,currentColor);
		if (horiCheck() || vertiCheck() || diagCheck()){
			$('h4').text(currentName + " has won");
			game_over=true;
			$('.board  button').attr('disabled','disabled');
		}
	}
}) 

