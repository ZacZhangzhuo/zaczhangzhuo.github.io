import zConfig from "../config/config.json";
import { getTimeCreatedFromPath } from "./util";

// !Legacy Config
export const legacyConfig = await fetch("/archz-static/legacy_config.json").then((r) => r.json());

// !Category
export class Category {
	_name: string;
	_displayLimitYear: number;
	_path: string;

	constructor({ name, displayLimitYear, path }: { name: string; displayLimitYear: number; path?: string }) {
		this._name = name;
		this._displayLimitYear = displayLimitYear;
		this._path = path || `/${name}`;
	}
}

function getCategories(): { [key: string]: Category } {
	let categories: { [key: string]: Category } = {};
	for (let i = 0; i < zConfig.categories.length; i++) {
		categories[zConfig.categories[i].name] = new Category({
			name: zConfig.categories[i].name,
			displayLimitYear: zConfig.categories[i].displayLimitYear,
		});
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
	_category: Category;
	_type: string;
	_timeCreated: Date;

	constructor({
		name,
		file,
		path,
		image,
		category,
		type = "",
		timeCreated,
	}: {
		name: string;
		file: string;
		path: string;
		image: string;
		category: Category;
		type?: string;
		timeCreated: Date;
	}) {
		this._name = name;
		this._file = file;
		this._path = path;
		this._image = image;
		this._category = category;
		this._type = type;
		this._timeCreated = timeCreated;
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
			category: categories["others"],
			timeCreated: new Date(),
		}),
		new Blog({
			name: "zCV_CN",
			file: "/zCV/zCV_cn.html",
			path: "/CV_cn",
			image: "/archz-static/about.jpg",
			category: categories["others"],
			timeCreated: new Date(),
		})
	);
	for (let i = 0; i < zConfig.others.length; i++) {}
	return others;
}

export const others = getOthers();

class LegacyBlog extends Blog {
	constructor({
		blogInfo,
		category,
	}: {
		blogInfo: { name: string; file: string; image: string; timeCreated: string };
		category: Category;
	}) {
		let _file = `/archz-static/${category._name}/${blogInfo.file}`;
		if (blogInfo.file.startsWith("http")) {
			_file = blogInfo.file;
		}

		let _timeCreated: Date | null = new Date(blogInfo.timeCreated);
		if (isNaN(_timeCreated.valueOf())) {
			_timeCreated = getTimeCreatedFromPath(blogInfo.file) || getTimeCreatedFromPath(blogInfo.image);
		}

		if (_timeCreated == null) {
			console.error(`Error: ${blogInfo.file} has no timeCreated`);
			_timeCreated = new Date();
		}

		super({
			name: blogInfo.name,
			file: _file,
			path: `/archz-static/${category._name}/${blogInfo.file.split("/")[0]}`,
			image: `/archz-static/${category._name}/${blogInfo.image}`,
			category,
			timeCreated: _timeCreated,
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
			_blogs.push(new LegacyBlog({ blogInfo, category: categories[category] }));
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
				category: categories["zPhotographer"],
				type: "instagram",
				timeCreated: new Date(),
			})
		);
	}
	return blogs;
}

const legacyBlogs = getLegacyBlogs();
const photographBlogs = getPhotographBlogs();
export let blogs = legacyBlogs;
blogs["zPhotographer"] = photographBlogs;
