import * as THREE from "three";
// import { Light } from "three";
// import "/zStyles.css";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

//Scene
const scene = new THREE.Scene();

//Create a sphere
const geometry = new THREE.SphereGeometry(1, 64, 64);

//Color the sphere
const material = new THREE.MeshStandardMaterial({ color: "#00ff83" });

//Mesh
const mesh = new THREE.Mesh(geometry, material);

//Add mesh to scene
scene.add(mesh);

//Light
const pointLight = new THREE.PointLight(0xffffff, 1, 100);
pointLight.position.set(-10, 10, 10);
scene.add(pointLight);

//Size
const sizes = { width: window.innerWidth, height: window.innerHeight };

//Camera
const camera = new THREE.PerspectiveCamera(
  45,
  sizes.width / sizes.height,
  0.1,
  100
);
camera.position.z = 3;
scene.add(camera);

//Renderer
const canvas = document.querySelector(".webgl");
const renderer = new THREE.WebGLRenderer({ canvas });
renderer.setSize(sizes.width, sizes.height);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.render(scene, camera);

// Controls
const controls = new OrbitControls(camera, canvas)
controls.enableDamping = true
// controls.enablePan = false
// controls.enableZoom = false
controls.autoRotate = true
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
  controls.update()
//  Live update
  renderer.render(scene, camera);
  window.requestAnimationFrame(loop);

};
loop();
