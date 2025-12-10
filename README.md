# **Merge Sort Visualizer**

---

## 📸 **Demo Screenshot**
*(Add your own screenshot once deployed)*

![Demo](screenshots/demo.png)

---

# 🧠 **Problem Breakdown & Computational Thinking**

## **What the App Does**
This project demonstrates **Merge Sort**, an efficient **O(n log n)** divide-and-conquer sorting algorithm.  
The app takes a comma-separated list of integers, recursively **splits** it, **sorts** each half, and **merges** them while showing every step clearly.

---

# 🧩 **Computational Thinking Breakdown**

---

## **1. Decomposition**
Merge Sort naturally breaks the problem into smaller parts:

- Parse user input into a list  
- Recursively split the list into left and right halves  
- Sort each half independently  
- Merge the two sorted halves  
- Display each step to help learners understand the algorithm  

---

## **2. Pattern Recognition**
Merge Sort uses repeated structures:

- Every list is split at the midpoint  
- Every merge compares the smallest elements of each side  
- Merging continues until one side is empty  

These predictable patterns make it ideal for visualization.

---

## **3. Abstraction**
To simplify the user experience:

- Only essential steps (splits, comparisons, merges) are shown  
- Internal Python details (indices, recursion depth) are hidden  
- Indentation visually represents recursion depth  
- Users interact only through a textbox and a button  

---

## **4. Algorithmic Thinking**
Merge Sort follows a clear, logical three-step process:

1. **Divide** — split the list into halves  
2. **Conquer** — recursively sort each half  
3. **Combine** — merge the sorted halves into a final list  

This structure guarantees efficient and correct sorting.

---

# ⚙️ **How to Run Locally**

### **1. Install dependencies**
```bash
pip install -r requirements.txt

