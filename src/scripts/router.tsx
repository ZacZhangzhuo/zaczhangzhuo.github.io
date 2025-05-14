import { beforePrint, afterPrint } from "./util";
import { Blog } from "./config";
import { BlogPage } from "./blog";
import { blogs } from "./config";
import { categories } from "./config";
import { Category } from "./config";
import { CategoryPage } from "./category";
import { createBrowserRouter } from "react-router-dom";
import { createHomePage } from "./home";
import { others } from "./config";
import { Navigate } from "react-router-dom";

function createBlogRouterInfo(blogs: { [key: string]: Blog[] }) {
	let pageInfo = [];
	for (let i in blogs) {
		for (let j = 0; j < blogs[i].length; j++) {
			let blog = blogs[i][j];
			pageInfo.push({
				path: blog._path,
				element: <BlogPage blog={blog} />,
			});
		}
	}

	return pageInfo;
}

function createCategoryRouterInfo(categories: { [key: string]: Category }) {
	let pageInfo = [];
	for (let i in categories) {
		pageInfo.push({
			path: categories[i]._path,
			element: <CategoryPage category={categories[i]} />,
		});
	}
	return pageInfo;
}

function createOthersRouterInfo(others: Blog[]) {
	let pageInfo = [];

	const pageEffect = () => {
		window.onbeforeprint = () => {
			beforePrint({ img_class_replace: "cv_item_logo_img" });
		};
		window.onafterprint = () => {
			afterPrint({ img_class_replace: "cv_item_logo_img" });
		};
	};

	for (let i = 0; i < others.length; i++) {
		pageInfo.push({
			path: others[i]._path,
			element: <BlogPage blog={others[i]} props={{ effect: pageEffect }} />,
		});
	}
	return pageInfo;
}

function createRouters() {
	let routerInfo = [
		{
			path: "/",
			element: createHomePage(),
		},
		{ path: "/zKeys", element: <Navigate to="/zKeys/index.html" /> },
		{ path: "/zKeys/index.html" },
	];

	routerInfo.push(...createCategoryRouterInfo(categories));
	routerInfo.push(...createOthersRouterInfo(others));
	routerInfo.push(...createBlogRouterInfo(blogs));

	return createBrowserRouter(routerInfo);
}

export const routers = createRouters();
