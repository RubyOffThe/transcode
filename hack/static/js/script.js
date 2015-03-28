

function splashBtnClick(){
	var titleDiv = $("#title-element");
	titleDiv;
	
	titleDiv.fadeOut(400).queue( function(){
		titleDiv.removeClass("splash")
		$("#splashBtn").hide();
		titleDiv.fadeIn(500);
		// titleDiv.show();
		}).queue( function(){});
}