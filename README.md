# hand → 3d

Real-time 3D particle system controlled by hand gestures via webcam. Built with MediaPipe Hands + Three.js.

---

## Gestures

| Gesture | Action |
|---|---|
| Pinch (thumb + index) | Grab and move the shape |
| Open hand | Disperse particles |
| L + fist (two hands) | Cycle to next shape |

---

## Shapes

- ♥ Heart
- ○ Torus
- ◉ Sphere
- 〰 DNA
- ∞ Möbius
- ★ Star

---

## Requirements

- Chrome (required for WASM + SharedArrayBuffer)
- Webcam

---

## Running locally

```bash
python server.py
```

Open `http://localhost:8000/hand_visualizer.html` in Chrome.

The local server is required because the browser needs `Cross-Origin-Opener-Policy` and `Cross-Origin-Embedder-Policy` headers to run WASM with multiple threads.

---

## File structure

```
hand_visualizer.html                    main interface
server.py                               local HTTP server with COOP/COEP headers
three.min.js                            Three.js r128
hands.js                                MediaPipe Hands
camera_utils.js                         MediaPipe camera utility
drawing_utils.js                        MediaPipe drawing utilities
hands_solution_simd_wasm_bin.js         WASM bindings
hands_solution_simd_wasm_bin.wasm       WASM runtime
hands_solution_packed_assets_loader.js  asset loader
hands_solution_packed_assets.data       packed models
hand_landmark_full.tflite               landmark model
hands.binarypb                          MediaPipe graph
```

---

## Stack

- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands) — hand landmark detection
- [Three.js](https://threejs.org) — WebGL renderer
