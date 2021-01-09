//显示图片详情，鼠标移入时执行
function on(ImgSrc) {
	if (ImgSrc == "undefined" || ImgSrc == null || ImgSrc == "") {return;}
	$("#imgs").attr("src", ImgSrc);	    //给图片容器赋值路径
    $(document).mousemove(function(e) {
		if(e.pageY < window.outerHeight - 300)$("#imgs").css("position", "absolute").css("left", e.pageX+1+"px").css("top", e.pageY+1+"px");
		else $("#imgs").css("position", "absolute").css("left", e.pageX+1+"px").css("top", e.pageY-300-1+"px");
    })
}

//关闭图片，当鼠标移出时执行
function off() {
	$("#imgs").attr("src", "");
	$(document).mousemove(function(e) {
		$("#imgs").css("position", "absolute").css("left", "-400px").css("top", "-400px");
	})
}
