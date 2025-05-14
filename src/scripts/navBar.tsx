import { Link } from "react-router-dom";
import { categories, others } from "./config";
import { cloneElement } from "react";
import { authSection } from "./auth";

export function Navbar(type: string) {
	var navBar: JSX.Element[] = [];
	let items = categories.concat(others);

	navBar.push(
		<Link key="Home" to="/" className="navBar">
			<p>zHome</p>
		</Link>
	);
	for (let i = 0; i < items.length; i++) {
		let category = items[i];
		navBar.push(
			<Link key={category._name} to={category._path} className="navBar">
				<p>{category._name}</p>
			</Link>
		);
	}

	// CV-specific changes
	navBar.pop();

	if (type === "zCV") {
		const lastLink = navBar[navBar.length - 1];
		navBar[navBar.length - 1] = cloneElement(lastLink, {
			children: (
				<p>
					<b>EN</b>·CN
				</p>
			),
			to: "/CV_cn",
		});
	} else if (type === "zCV_CN") {
		const lastLink = navBar[navBar.length - 1];
		navBar[navBar.length - 1] = cloneElement(lastLink, {
			children: (
				<p>
					EN·<b>CN</b>
				</p>
			),
			to: "/CV_en",
		});
	}

	// auth section
	navBar.push(authSection());

	return navBar;
}
