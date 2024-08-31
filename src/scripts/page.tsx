import { useEffect } from "react";

export function Page({
	title,
	children,
	effect = () => {},
	meta = <></>,
	bodyStyle = {},
}: {
	title: string;
	children: JSX.Element;
	effect?: () => void;
	meta?: JSX.Element;
	bodyStyle?: React.CSSProperties;
}) {
	useEffect(effect);
	return (
		<>
			<head>
				<meta charSet="UTF-8" />
				<meta httpEquiv="X-UA-Compatible" content="IE=edge,chrome=1" />
				<meta name="viewport" content="width=device-width, initial-scale=1.0" />
				{meta}
				<script src="/zFunctions.js" />
				<link rel="icon" href="/favicon.ico" />
				<link rel="stylesheet" href="/styles/zStyles.css" />
				<link rel="stylesheet" href="/styles/zMarkdownStyles.css" />
				<title>{title}</title>
			</head>
			<body style={bodyStyle}>
				{children}
				<p className="endnotes">--- Growing, Growing, Brighter Everyday ! ---</p>
			</body>
		</>
	);
}
