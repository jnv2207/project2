# 🧩 Logic Box — Pattern Generator & Number Analyzer

<p align="center">
  <img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" width="90" alt="python logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Type-CLI%20Program-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4-red?style=for-the-badge" />
</p>

<p align="center">
  <i>A simple, menu-driven Python program that generates patterns and analyzes number ranges —
  built to practice loops, control statements, and nested logic. 🐍✨</i>
</p>

---

## 📽️ Demo

https://drive.google.com/file/d/1pbwIsxXCl0uGzTXCXbb6wVA_Iimf7Pop/view?usp=drive_link

---

## 📖 Table of Contents

- [About the Project](#-about-the-project)
- [Demo](#️-demo)
- [Features](#-features)
- [Sample Run](#-sample-run)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Assumptions](#-assumptions)
- [Video Explanation](#-video-explanation)
- [Author](#-author)

---

## 🎯 About the Project

**Logic Box** is a Python console application that combines two mini-tools into one menu-driven system:

1. 🔺 **Pattern Generator** — draws a right-angled triangle pattern using nested loops
2. 🔢 **Number Analyzer** — checks odd/even numbers in a range and calculates their sum

This project was built to practice **control structures, `for`/`while` loops, the `range()` function, control statements (`break`, `continue`, `pass`), and nested loops.**

---

## ⚙️ Features

| Feature | Description |
|---|---|
| 🔺 Pattern Generator | Enter the number of rows → get a right-angled triangle made of `*` |
| 🔢 Number Analyzer | Enter a start & end value → see which numbers are odd/even + their total sum |
| 🛡️ Input Validation | Handles invalid inputs gracefully (e.g. negative rows, end < start) |
| 🔁 Menu-Driven Loop | Keep using features until you choose to exit |
| 👋 Clean Exit | Friendly goodbye message when done |

---

## 🖥️ Sample Run

```text
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 1
Enter the number of rows for the pattern: 5

Pattern:
*
**
***
****
*****

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 2

Enter the start of the range: 10
Enter the end of the range: 15
Number 10 is Even
Number 11 is Odd
Number 12 is Even
Number 13 is Odd
Number 14 is Even
Number 15 is Odd
Sum of all numbers from 10 to 15 is: 75

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 3
Exiting the program. Goodbye!
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed → [Download here](https://www.python.org/downloads/)

### Run it locally

```bash
# Clone the repository
git clone https://github.com/<your-username>/logic-box.git

# Move into the project folder
cd logic-box

# Run the program
python logic_box.py
```

---

## 📂 Project Structure

```
logic-box/
├── logic_box.py     # Main program file
├── README.md        # You are here 📍
└── assets/
    └── demo.gif     # Terminal recording shown in the Demo section
```

---

## 📝 Assumptions

- Only a **right-angled triangle** pattern is implemented, as specified in the requirements.
- If the user enters a non-positive number of rows, the program shows an error and re-prompts instead of crashing.
- If the "end" of a range is smaller than the "start," the user is asked to re-enter valid values.
- The program runs continuously in a loop until option `3. Exit` is chosen.

---

## 🎬 Video Explanation

https://drive.google.com/file/d/1pbwIsxXCl0uGzTXCXbb6wVA_Iimf7Pop/view?usp=drive_link

▶️ **[Watch the video explanation]

---

## 👩‍💻 Author

**Janvi**
Computer Science Engineering (CSE) Student

<p align="center">✨ Thanks for checking out Logic Box! ✨</p>
