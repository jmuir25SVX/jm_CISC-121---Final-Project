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
```

## 🌐 Hugging Face App Link
https://huggingface.co/spaces/jmuir1/CISC_121-FinalProject

---

## 🔍 Algorithm Explanation (Simple Overview)

**Merge Sort** works in three main stages:

### **1. Split**
Divide the list repeatedly until each sublist contains only one element.

### **2. Sort**
A single-element list is already sorted (base case).

### **3. Merge**
Repeatedly compare the smallest elements from each half and append them to build a new sorted list.

---

### **Time & Space Complexity**
- **Worst-case:** O(n log n)  
- **Best-case:** O(n log n)  
- **Space complexity:** O(n) (temporary merge arrays)

---

## ✅ Testing & Verification

### **1. Small List**
**Input:**  
`5, 1, 8, 2, 7`  

**Result:**  
Correct split + merge sequence and proper final order.

---

### **2. Larger List**
**Input:**  
`38, 27, 43, 3, 9, 82, 10`  

**Result:**  
Proper sorting and complete depth-based visualization.

---

### **3. Edge Cases**

| Case            | Input        | Expected Behavior              | Result  |
|-----------------|--------------|--------------------------------|---------|
| Empty list      | ""           | Return base-case output        | Passed  |
| Single number   | 7            | Return unchanged               | Passed  |
| Repeated values | 5, 5, 1, 5    | Stable merge logic             | Passed  |
| Negative nums   | -3, 10, -1   | Correct ordering               | Passed  |
| Invalid input   | a, b, c      | Show error message             | Passed  |

---

## ▶️ Steps to Use the App

1. Enter a comma-separated list of integers  
2. Click "Run Merge Sort"


