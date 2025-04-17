<h1 align="center">🏎️ A Car Race Simulator</h1>

<p align="center">
  <i>A simple, fun, and object-oriented car race simulator built using pure HTML, CSS, and JavaScript.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-OOP-green?style=flat-square">
  <img src="https://img.shields.io/badge/Status-Completed-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Made%20With-💛%20Vanilla%20JS-orange?style=flat-square">
</p>

---

## 🎯 About the Project

This is a basic car racing game built with **classes and objects** in Python. The cars "race" across the screen with simple animations. It’s ideal for beginners exploring Object-Oriented Programming (OOP) in web development.

---

## 🧠 Features

- 🧱 Simple layout with HTML, CSS, JavaScript
- 🧠 Object-Oriented Python logic using `class Car {}`
- 🎯 Random speed generation for racing simulation
- 💨 Start/Reset buttons
- 🖼️ Pure front-end — Development, Backend:-Python

---

## 🔍 Project Preview


---

```javascript
class Car {
  constructor(name, color, position) {
    this.name = name;
    this.color = color;
    this.position = position;
  }

  move() {
    const speed = Math.random() * 10;
    this.position += speed;
    return this.position;
  }
}


---

## 🛠️ Tech Used

| Tech       | Role                                     |
|------------|------------------------------------------|
| HTML       | Structure of the game                    |
| CSS        | Basic styling/animation                  |
| JavaScript | Web Development                     |
| Python     | OOP Logic For Race (Class And Object)    |
---

## 🧩 How It Works

- Each car is an object created from a `Car` class.
- Cars get random speeds and move on each frame.
- First car to reach the end wins.
- You can reset the game using a button.

---

## 🗂 Folder Structure
A-Car-Race-Simulator/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
└── README.md

---

## 🚀 Getting Started

### Run Web Version Locally

```bash
git clone https://github.com/Omkarok2510/A-Car-Race-Simulator.git
cd A-Car-Race-Simulator
python app.py

