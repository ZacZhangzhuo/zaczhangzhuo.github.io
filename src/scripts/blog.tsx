import parse, { attributesToProps, HTMLReactParserOptions } from "html-react-parser";
import { useState } from "react";
import Markdown from "react-markdown";
import rehypeRaw from "rehype-raw";
import { Blog } from "./config";
import { Navbar } from "./navBar";
import { Page } from "./page";

export function BlogPage({ blog, props = {} }: { blog: Blog; props?: any }) {
	const [content, setContent] = useState("");

	if (blog._file.endsWith(".md")) {
		// TODO: add string replace for markdown texts.
		fetch(blog._file)
			.then((response) => {
				return response.text();
			})
			.then((t) => {
				setContent(t);
			})
			.catch((e) => {
				console.error(e);
			});

		return (
			<Page title={blog._name} {...props}>
				<>
					{/* Menu bar */}
					<div className="navBar">{Navbar(blog._name)}</div>
					{/* Main content */}
					<Markdown
						rehypePlugins={[rehypeRaw]}
						urlTransform={(url) => (url.startsWith("http") ? url : `${blog._path}/${url}`)}
					>
						{content}
					</Markdown>
				</>
			</Page>
		);
	} else if (blog._file.endsWith(".html")) {
		fetch(blog._file)
			.then((response) => {
				return response.text();
			})
			.then((t) => {
				if (t != undefined) {
					let _t = t.split("<!-- End of Menu Bar -->")[1].split('<p class="endnotes">')[0];
					setContent(_t);
				}
			})
			.catch((e) => {
				console.error(e);
			});
		const replace_options: HTMLReactParserOptions = {
			replace(domNode: any) {
				if (domNode.name === "img") {
					let props = attributesToProps(domNode.attribs);
					return (
						<img
							{...props}
							src={blog._path.includes("CV") ? `zCV/${props.src}` : `${blog._path}/${props.src}`}
							alt={blog._name}
						/>
					);
				}
			},
		};

		return (
			<Page title={blog._name} {...props}>
				<>
					{/* Menu bar */}
					<div className="navBar">{Navbar(blog._name)}</div>
					{/* Main content */}
					{parse(content, replace_options)}
				</>
			</Page>
		);
	} else {
		return (
			<Page title={blog._name} meta={<meta httpEquiv="refresh" content={`0;URL=${blog._file}`}></meta>}>
				<></>
			</Page>
		);
	}
}
