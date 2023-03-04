// import { AmbientLight } from "three";
import * as THREE from "/node_modules/three/build/three.module.js";
import { OrbitControls } from "/node_modules/three/examples/jsm/controls/OrbitControls.js";
import data from "/zCV.json";
// Get the data
// var theData = [];
// var displayData = function (data) {
//	 theData = Object.assign({}, data);
// };
// $.ajax({
//	 url: "zCV.json",
//	 type: "GET",
//	 dataType: "json",
//	 async: false,
//	 success: function (data) {
//		 displayData(data);
//	 },
// });

//Scene
const scene = new THREE.Scene();

//Color the sphere
const fatherMaterial = new THREE.MeshStandardMaterial({ color: "#00ff83" });
const sonMaterial = new THREE.MeshStandardMaterial({ color: "#ff0000" });

//! Create a sphere for	the fathers
for (let j = 0; j < data[0].length; j++) {
	var sphere = new THREE.SphereGeometry(data[0][j]["Radius"] * data[0][j]["Scale"], 64, 64);

	var mesh = new THREE.Mesh(sphere, fatherMaterial);

	mesh.position.set(data[0][j]["Point"][0], data[0][j]["Point"][1], data[0][j]["Point"][2]);
	scene.add(mesh);
	// spheres.push(sphere);
}

//! Create a sphere for	the sons
for (let j = 0; j < data[1].length; j++) {
	var sphere = new THREE.SphereGeometry(data[1][j]["Radius"] * data[1][j]["Scale"], 64, 64);
	var mesh = new THREE.Mesh(sphere, sonMaterial);
	mesh.position.set(data[1][j]["Point"][0], data[1][j]["Point"][1], data[1][j]["Point"][2]);
	scene.add(mesh);
}

//TODO
//Light
const pointLight = new THREE.PointLight(0xffffff, 1, 100);
const ambientLight = new THREE.AmbientLight(0xffffff, 0.1);
pointLight.position.set(-10, 10, 10);
scene.add(pointLight);
scene.add(ambientLight);

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
// controls.enablePan = false
// controls.enableZoom = false
controls.autoRotate = true;
// controls.autoRotateSpeed = 0.5

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

const loop = () => {
	controls.update();
	//	Live update
	renderer.render(scene, camera);
	window.requestAnimationFrame(loop);
};
loop();
