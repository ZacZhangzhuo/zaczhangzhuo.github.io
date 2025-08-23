import { Blog } from "./config";
import { useAuth } from "./auth";

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

export function getTimeCreatedFromPath(path: string): Date | null {
	const parts = path.split(/[_\/.\s]/); // _, /, . and space

	for (const part of parts) {
		if (part.length < 10) {
			continue; // Skip if part is too short to be a date
		}
		// in case of YYYY-MM-DD-HH-mm-ss format
		const date = new Date(part.split("-").slice(0, 3).join("-"));

		if (!isNaN(date.valueOf())) {
			return date;
		}
	}

	return null;
}

export function contentVisible(blog: Blog) {
	function isWithinYears(date: Date, numYears: number): boolean {
		return new Date().getFullYear() - date.getFullYear() <= numYears;
	}

	return (
		useAuth() != null ||
		blog._category._displayLimitYear < 0 ||
		isWithinYears(blog._timeCreated, blog._category._displayLimitYear)
	);
}
