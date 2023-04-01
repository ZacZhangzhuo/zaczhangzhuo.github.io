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
