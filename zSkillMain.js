import * as THREE from "three";
import { Vector3 } from "three";
import { OrbitControls } from "jsm/controls/OrbitControls.js";
import { FontLoader } from "jsm/loaders/FontLoader.js";
import { TextGeometry } from "jsm/geometries/TextGeometry.js";

// Get the data
var theData = [];
var displayData = function (data) {
	theData = Object.assign({}, data);
};
$.ajax({
	url: "zCV.json",
	type: "GET",
	dataType: "json",
	async: false,
	success: function (data) {
		displayData(data);
	},
});

const data = theData;

//Scene
const scene = new THREE.Scene();

var fatherTextMeshes = [];
var sonTextMeshes = [];

const fontLoader = new FontLoader();
var rise = 0.1;

fontLoader.load("resources/fonts/Source Sans Pro_Italic.json", (font) => {
	//! Create texts for the fathers
	for (let j = 0; j < data[0].length; j++) {
		var textMesh = new THREE.Mesh();
		const textGeometry = new TextGeometry(data[0][j]["Category"], {
			height: 0.01,
			size: 0.3,
			font: font,
			bevelEnabled: false,
		});

		textMesh.geometry = textGeometry;
		textMesh.material = new THREE.MeshStandardMaterial({ color: "#ffffff21" });
		textMesh.position.set(data[0][j]["Point"][0], data[0][j]["Point"][1], data[0][j]["Point"][2]);
		fatherTextMeshes.push(textMesh);

		scene.add(textMesh);
	}

	//! Create texts for the sons
	for (let j = 0; j < data[1].length; j++) {
		var textMesh = new THREE.Mesh();
		const textGeometry = new TextGeometry(
			data[1][j]["Skill"] +
				"\n" +
				"Scenario: " +
				data[1][j]["Scenario"] +
				"\n" +
				"Level: " +
				removeBackslash(data[1][j]["Level"]) +
				"\n" +
				"Since: " +
				data[1][j]["Since"],
			{
				height: 0.01,
				size: 0.2,
				font: font,
				bevelEnabled: false,
			}
		);

		textMesh.geometry = textGeometry;
		textMesh.material = new THREE.MeshStandardMaterial({ color: "#ffffff", transparent: true });
		textMesh.position.set(data[1][j]["Point"][0], data[1][j]["Point"][1] + rise, data[1][j]["Point"][2]);
		sonTextMeshes.push(textMesh);
		scene.add(textMesh);
	}
});

//! Draw lines between fathers
var fatherLines = [];
const fatherLineMaterial = new THREE.LineBasicMaterial({ color: "#ffffff" });

for (let j = 0; j < data[0].length; j++) {
	var p0 = new Vector3(data[0][j]["Point"][0], data[0][j]["Point"][1], data[0][j]["Point"][2]);
	if (j == data[0].length - 1) {
		var p1 = new Vector3(data[0][0]["Point"][0], data[0][0]["Point"][1], data[0][0]["Point"][2]);
	} else var p1 = new Vector3(data[0][j + 1]["Point"][0], data[0][j + 1]["Point"][1], data[0][j + 1]["Point"][2]);

	var Points = [p0, p1];
	var geometry = new THREE.BufferGeometry().setFromPoints(Points);

	var line = new THREE.Line(geometry, fatherLineMaterial);
	fatherLines.push(line);
	scene.add(line);
}

//! Draw lines between fathers and sons
var sonLines = [];
var LineEnds = [];
for (let j = 0; j < data[0].length; j++) {
	for (let k = 0; k < data[0][j]["Links"].length; k++) {
		var v1 = new Vector3(data[0][j]["Point"][0], data[0][j]["Point"][1], data[0][j]["Point"][2]);
		var v2 = new Vector3(
			data[1][data[0][j]["Links"][k]]["Point"][0],
			data[1][data[0][j]["Links"][k]]["Point"][1],
			data[1][data[0][j]["Links"][k]]["Point"][2]
		);
		var Points = [v1, v2];
		var geometry = new THREE.BufferGeometry().setFromPoints(Points);
		var line = new THREE.Line(geometry, new THREE.LineBasicMaterial({ color: "#ffffff", transparent: true }));
		LineEnds.push([v1, v2]);
		sonLines.push(line);
		scene.add(line);
	}
}

//! Light
// const ambientLight = new THREE.AmbientLight("#ffffff", 1);
// const pointLight = new THREE.PointLight({ color: "#ffffff", intensity: 0.0001, distance: 0.0001 });
// const pointLight = new THREE.PointLight("#ffffff", 30, 30, 5);
const pointLight = new THREE.PointLight("#ffffff", 30, 0, 0);
// pointLight.position.set(0, 0, 0);
// scene.add(ambientLight);
scene.add(pointLight);

//Size
const sizes = { width: window.innerWidth, height: window.innerHeight };

//Camera
const camera = new THREE.PerspectiveCamera(45, sizes.width / sizes.height, 0.1, 100);
camera.position.z = 20;
scene.add(camera);

//Renderer
const canvas = document.querySelector(".webgl");
const renderer = new THREE.WebGLRenderer({ canvas });
renderer.setSize(sizes.width, sizes.height);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.render(scene, camera);

// Controls
const controls = new OrbitControls(camera, canvas);
controls.enableDamping = true;
controls.enableDrag = false;
// controls.enableRotate = false;
controls.maxPolarAngle = Math.PI / 2;
controls.minPolarAngle = Math.PI / 2;
controls.enablePan = false;
controls.enableZoom = false;
controls.autoRotate = true;
controls.autoRotateSpeed = 0.8;

//Resize
window.addEventListener("resize", () => {
	//update sizes
	// console.log(window.innterWidth)
	sizes.width = window.innerWidth;
	sizes.height = window.innerHeight;
	//Updte camera
	camera.updateProjectionMatrix();
	camera.aspect = sizes.width / sizes.height;
	renderer.setSize(sizes.width, sizes.height);
});

var maxDistance = 0;
var minDistance = 10000000;
for (let i = 0; i < LineEnds.length; i++) {
	var dis = camera.position.distanceTo(LineEnds[i][1]);
	if (dis > maxDistance) maxDistance = dis;
	if (dis < minDistance) minDistance = dis;
}
console.log(maxDistance);
console.log(minDistance);

//! Loop
var f = 0;
const loop = () => {
	f++;
	controls.update();
	renderer.render(scene, camera);
	window.requestAnimationFrame(loop);
	pointLight.position.set(camera.position.x, camera.position.y, camera.position.z);

	for (let i = 0; i < fatherTextMeshes.length; i++) {
		fatherTextMeshes[i].lookAt(camera.position);
	}

	for (let i = 0; i < sonTextMeshes.length; i++) {
		sonTextMeshes[i].lookAt(camera.position);
	}

	for (let i = 0; i < sonLines.length; i++) {
		if (sonLines.length != sonTextMeshes.length) {
			return;
		}

		rotateAroundPoint(sonTextMeshes[i], LineEnds[i][0], new Vector3(0, 1, 0), 0.1);
		rotateAroundPoint(sonLines[i], LineEnds[i][0], new Vector3(0, 1, 0), 0.1);
		rotateAroundPoint(LineEnds[i][0], LineEnds[i][0], new Vector3(0, 1, 0), 0.1);
		rotateAroundPoint(LineEnds[i][1], LineEnds[i][0], new Vector3(0, 1, 0), 0.1);

		var dis = camera.position.distanceTo(LineEnds[i][1]);

		var opacity = 1 - ((dis - minDistance) / (maxDistance - minDistance)) * 2.5;

		// console.log(opacity);

		sonLines[i].material.opacity = opacity;
		sonTextMeshes[i].material.opacity = opacity;
	}
};
loop();

function rotateAroundPoint(object, point, axis, anglePerFrame) {
	if (!object) return;
	const angle = (anglePerFrame * Math.PI) / 180; // Convert degrees to radians
	const rotationMatrix = new THREE.Matrix4().makeRotationAxis(axis.normalize(), angle);
	const translationMatrix = new THREE.Matrix4().makeTranslation(point.x, point.y, point.z);
	const inverseTranslationMatrix = new THREE.Matrix4().makeTranslation(-point.x, -point.y, -point.z);
	const finalMatrix = translationMatrix.multiply(rotationMatrix).multiply(inverseTranslationMatrix);
	object.applyMatrix4(finalMatrix);

	// Update the position of the object after the rotation
	// object.position.applyMatrix4(finalMatrix);
}
function removeBackslash(str) {
	return str.replace(/\\/g, "");
}
