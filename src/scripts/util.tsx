export function beforePrint({ img_class_replace = undefined }: { img_class_replace: string | undefined }) {

	console.log("beforePrint");
	if (img_class_replace) {
		var images = document.getElementsByClassName(img_class_replace) as HTMLCollectionOf<HTMLImageElement>;
		for (var i = 0; i < images.length; i++) {
			var oldSrc = images[i].src;
			var newSrc = oldSrc.replace(/\.(jpg|jpeg|png|gif)$/i, "_print.$1");
			images[i].src = newSrc;
		}
	}
}

export function afterPrint({ img_class_replace = undefined }: { img_class_replace: string | undefined }) {

	if (img_class_replace) {
		var images = document.getElementsByClassName(img_class_replace) as HTMLCollectionOf<HTMLImageElement>;
		for (var i = 0; i < images.length; i++) {
			var oldSrc = images[i].src;
			var newSrc = oldSrc.replace(/_print\.(jpg|jpeg|png|gif)$/i, ".$1");
			images[i].src = newSrc;
		}
	}
}
