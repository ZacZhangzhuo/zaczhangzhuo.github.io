import { Link } from "react-router-dom";
import { Blog, blogs, Category } from "./config";
import { navBar } from "./navBar";
import { Page } from "./page";

function getCategoryItem(blog: Blog) {
	let content = <></>;
	if (blog._category === "zPhotographer") {
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

export function CategoryPage({ category }: { category: Category }) {
	return (
		<Page title={category._name}>
			<>
				{/* Menu bar */}
				<div className="navBar">{navBar}</div>
				{/* Main content */}
				<div className="mainGuid">
					{blogs[category._name].map((i) => {
						return getCategoryItem(i);
					})}
				</div>
			</>
		</Page>
	);
}
