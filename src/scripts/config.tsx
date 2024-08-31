import zConfig from "../config/config.json";

// !Legacy Config
export const legacyConfig = await fetch("/archz-static/legacy_config.json").then((r) => r.json());

// !Category
export class Category {
	_name: string;
	_path: string;

	constructor({ name }: { name: string }) {
		this._name = name;
		this._path = `/${name}`;
	}
}

function getCategories(): Category[] {
	let categories: Category[] = [];
	for (let i = 0; i < zConfig.categories.length; i++) {
		categories.push(new Category({ name: zConfig.categories[i] }));
	}
	return categories;
}
export const categories = getCategories();

// !Media
export class Media {
	_name: string;
	_url: string;
	_icon: string;

	constructor({ name, url, icon }: { name: string; url: string; icon: string }) {
		this._name = name;
		this._url = url;
		this._icon = icon;
	}
}
function getMedia(): Media[] {
	let medias: Media[] = [];
	for (let i = 0; i < zConfig.medias.length; i++) {
		let media = zConfig.medias[i];
		medias.push(new Media({ name: media.name, url: media.url, icon: media.icon }));
	}
	return medias;
}

export const medias = getMedia();

// !Blog
export class Blog {
	_name: string;
	_file: string;
	_path: string;
	_image: string;
	_category: string;
	_type: string;

	constructor({
		name,
		file,
		path,
		image,
		category,
		type = "",
	}: {
		name: string;
		file: string;
		path: string;
		image: string;
		category: string;
		type?: string;
	}) {
		this._name = name;
		this._file = file;
		this._path = path;
		this._image = image;
		this._category = category;
		this._type = type;
	}
}

// !Others
function getOthers(): Blog[] {
	let others: LegacyBlog[] = [];
	others.push(
		new Blog({
			name: "zCV",
			file: "/zCV/zCV_en.html",
			path: "/CV_en",
			image: "/archz-static/about.jpg",
			category: "others",
		}),
		new Blog({
			name: "zCV_CN",
			file: "/zCV/zCV_cn.html",
			path: "/CV_cn",
			image: "/archz-static/about.jpg",
			category: "others",
		})
	);
	for (let i = 0; i < zConfig.others.length; i++) {}
	return others;
}

export const others = getOthers();

class LegacyBlog extends Blog {
	constructor({ blogInfo, category }: { blogInfo: { name: string; file: string; image: string }; category: string }) {
		let _file = `/archz-static/${category}/${blogInfo.file}`;
		if (blogInfo.file.startsWith("http")) {
			_file = blogInfo.file;
		}

		super({
			name: blogInfo.name,
			file: _file,
			path: `/archz-static/${category}/${blogInfo.file.split("/")[0]}`,
			image: `/archz-static/${category}/${blogInfo.image}`,
			category,
		});
	}
}

function getLegacyBlogs() {
	let blogs: { [key: string]: Blog[] } = {};

	for (let category in legacyConfig) {
		let blogInfos = legacyConfig[category as keyof typeof legacyConfig];
		let _blogs = [];
		for (let i = 0; i < blogInfos.length; i++) {
			let blogInfo = blogInfos[i];
			_blogs.push(new LegacyBlog({ blogInfo, category }));
		}
		blogs[category] = _blogs.reverse();
	}
	return blogs;
}

function getPhotographBlogs() {
	let blogs: Blog[] = [];
	for (let i = 0; i < zConfig.zPhotographer.length; i++) {
		let blogInfo = zConfig.zPhotographer[i];
		blogs.push(
			new Blog({
				name: blogInfo.name,
				file: "/",
				path: blogInfo.url,
				image: "/",
				category: "zPhotographer",
				type: "instagram",
			})
		);
	}
	return blogs;
}

const legacyBlogs = getLegacyBlogs();
const photographBlogs = getPhotographBlogs();
export let blogs = legacyBlogs;
blogs["zPhotographer"] = photographBlogs;
