import { initializeApp, FirebaseApp } from "firebase/app";
import { Auth, User } from "firebase/auth";
import { getAuth, signInWithEmailAndPassword, signOut } from "firebase/auth";
import { useState, useEffect } from "react";

const firebaseConfig = {
	apiKey: "AIzaSyADJQEIXtJ6tpQB6oFrpYNPBJ4XA7yIvQE",
	authDomain: "archz-auth.firebaseapp.com",
	projectId: "archz-auth",
	storageBucket: "archz-auth.firebasestorage.app",
	messagingSenderId: "777111541765",
	appId: "1:777111541765:web:19422463a592dcfd74246c",
};

class Firebase {
	app: FirebaseApp;
	auth: Auth;

	constructor() {
		this.app = initializeApp(firebaseConfig, "archz-auth");
		this.auth = getAuth(this.app);
	}

	login(email: string, password: string) {
		if (!email || !password) {
			alert("Email and password are required!");
			return;
		}

		return signInWithEmailAndPassword(this.auth, email, password)
			.then()
			.catch((error) => {
				if (error.code === "auth/invalid-email") {
					alert("Invalid email address format. Please check your email!");
				} else if (error.code === "auth/invalid-credential") {
					alert("Invalid credentials. Please check your email and password!");
				} else {
					alert("Failed to login! Error: " + error.message);
				}
			});
	}
	logout() {
		return signOut(this.auth)
			.then()
			.catch((error) => {
				alert("Failed to logout! Error: " + error.message);
			});
	}
}

const firebase = new Firebase();

export function useAuth() {
	const [currentUser, setCurrentUser] = useState<User | null>(null);

	useEffect(() => {
		const unsubscribe = firebase.auth.onAuthStateChanged((user) => {
			setCurrentUser(user);
		});

		return () => unsubscribe();
	}, []);

	return currentUser;
}

export function authSection() {
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const currentUser = useAuth();

	if (!currentUser) {
		return (
			<div key="auth">
				<form
					className="auth"
					key="auth"
					onSubmit={(e) => {
						e.preventDefault();
						firebase.login(email, password);
					}}
				>
					<div key="loginInput" style={{ width: "fit-content" }}>
						<input
							key="email"
							type="email"
							autoComplete="username"
							placeholder="Email"
							value={email}
							onChange={(e) => setEmail(e.target.value)}
						/>
						<input
							key="password"
							type="password"
							autoComplete="current-password"
							placeholder="Password"
							value={password}
							onChange={(e) => setPassword(e.target.value)}
						/>
					</div>
					<button key="loginButton" type="submit">
						Login
					</button>
				</form>
			</div>
		);
	} else {
		return (
			<div className="auth" key="auth">
				<div key="auth" style={{ width: "fit-content" }}>
					<a className="userInfo">Welcome,</a>
					<a className="userInfo"> {currentUser.email}</a>
				</div>
				<button
					key="logoutButton"
					onClick={() => {
						firebase.logout();
					}}
				>
					Logout
				</button>
			</div>
		);
	}
}
