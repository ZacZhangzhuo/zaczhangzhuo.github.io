import { Link } from "react-router-dom";
import { Blog, blogs, Category, categories } from "./config";
import { Navbar } from "./navBar";
import { Page } from "./page";

function getCategoryItem(blog: Blog) {
	let content = <></>;
	if (blog._category === categories["zPhotographer"]) {
		if (blog._type === "instagram") {
			content = <iframe src={blog._path} scrolling="no" />;
		} else {
			console.error("Invalid type for zPhotographer");
		}
	} else if (blog._file.startsWith("http")) {
		content = (
			<div className="item" key={blog._name}>
				<a href={blog._file}>
					<img className="item_image" src={blog._image} alt={blog._name} />
					<p className="item_name">{blog._name}</p>
				</a>
			</div>
		);
	} else {
		content = (
			<Link to={blog._path}>
				<img className="item_image" src={blog._image} alt={blog._name} />
				<p className="item_name">{blog._name}</p>
			</Link>
		);
	}

	return (
		<div className="item" key={blog._name}>
			{content}
		</div>
	);
}

function getCategoryGrid(items: Blog[]) {
	var itemSortedByYear: { [key: string]: Blog[] } = {};

	for (const item of items) {
		const year = item._timeCreated.getFullYear();
		if (!itemSortedByYear[year]) {
			itemSortedByYear[year] = [];
		}
		itemSortedByYear[year].push(item);
	}

	return (
		<div>
			{Object.keys(itemSortedByYear)
				.sort()
				.reverse()
				.map((year) => {
					return (
						<div key={year}>
							<h3 className="year">{year}</h3>
							<div style={{ display: "flex" }}>
								<div className="timeline" />
								<div className="mainGrid">
									{itemSortedByYear[year].map((item) => {
										return getCategoryItem(item);
									})}
								</div>
							</div>
						</div>
					);
				})}
		</div>
	);
}

export function CategoryPage({ category }: { category: Category }) {
	return (
		<Page title={category._name}>
			<>
				{/* Menu bar */}
				<div className="navBar">{Navbar(category._name)}</div>
				<div className="topMargin" />
				{/* Main content */}
				{getCategoryGrid(blogs[category._name])}
			</>
		</Page>
	);
}
