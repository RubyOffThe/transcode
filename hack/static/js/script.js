function showAbout(){
	$(".aboutEles").show();
}

function hideAbout(){
	$(".aboutEles").hide();
}


function splashBtnClick(){
	var titleDiv = $("#title-element");
	
	titleDiv.fadeOut(400).queue( function(){
		titleDiv.removeClass("splash")
		$("#splashBtn").hide();
		
		$("#title-element, .row").show();
		// .queue(function(){titleDiv.fadeIn();}
		// 	);
		})
	// .queue( function(){
	// 		titleDiv.fadeIn(500);
	// 		console.log("hi");
	// 	});
}