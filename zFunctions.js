function adjustIframe() {
	var ifm = document.getElementById("iframe");
	if (document.documentElement.clientHeight > document.documentElement.clientWidth) {
		ifm.height = document.documentElement.clientHeight;
		ifm.width = document.documentElement.clientWidth;
	} else {
		ifm.height = document.documentElement.clientHeight * 0.5;
		ifm.width = document.documentElement.clientWidth * 0.5;
	}
}
function replaceImagesBeforePrint(className) {
	var images = document.getElementsByClassName(className);
	for (var i = 0; i < images.length; i++) {
		var oldSrc = images[i].src;
		var newSrc = oldSrc.replace(/\.(jpg|jpeg|png|gif)$/i, "_print.$1");

		images[i].src = newSrc;
	}

}
