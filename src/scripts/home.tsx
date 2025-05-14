import { Link } from "react-router-dom";
import { categories, medias } from "./config";
import { Page } from "./page";

export function createHomePage() {
	return (
		<Page title="ArchZ" bodyStyle={{ margin: "0 0 0 0" }}>
			{/*Video*/}
			<div className="window">
				<div className="mainVideo">
					<video autoPlay loop muted src="/animation.mp4" width="95%"></video>
				</div>
				<div className="mainMenu">
					{/*Logo*/}
					<img src="/logo.png" alt="Logo Image" className="logo" />
					{/*I am a*/}
					<p className="IAMA">I am a ...</p>
					{/*Categories*/}
					{Object.entries(categories).map(([k, v]) => (
						<Link key={v._name} className="textWithLink" to={v._path}>
							{v._name}
						</Link>
					))}
					{/*Media*/}
					{medias.map((i) => {
						return (
							<Link key={i._name} to={i._url}>
								<img className="media" src={i._icon} alt={i._name} />
							</Link>
						);
					})}
				</div>
			</div>
		</Page>
	);
}
