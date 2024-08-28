import { Link } from "react-router-dom";
import { categories, others } from "./config";

function Navbar() {
	let navBar: JSX.Element[] = [];
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

	return navBar;
}

export const navBar = Navbar();
