# **Merge Sort Visualizer**

---

## **Demo Screenshot**

![Demo](screenshots/MergeSortVisualizationDemo.png)

---

# **Breakdown & Computational Thinking**

## **What the App Does**
This project implements a complete **Merge Sort Visualizer** using Python and Gradio. The goal is to help learners understand how the Merge Sort algorithm works internally by showing:

- Every **recursive split**
- Every **merge operation**
- Every **comparison** and **element selection**
- The **final sorted result**
- An additional **Random Array Generator** button that automatically produces a list of integers for instant testing

This tool emphasizes clarity, step-by-step explanation, and strong educational value. Users can sort their own custom input or generate sample data with one click.

---

## Why I Chose Merge Sort

I chose Merge Sort because it has a clear structure that makes it easy to break down, visualize, and explain step-by-step. It also consistently performs well and highlights core concepts like recursion and problem decomposition, which fit the goals of this project.

Key reasons:
- Predictable **O(n log n)** performance  
- Naturally demonstrates recursion  
- Easy to visualize through splits and merges  
- Clean divide-and-conquer design  
- Produces meaningful intermediate steps for learning

---

# **Computational Thinking Breakdown**

---

## **1. Decomposition**
Merge Sort naturally lends itself to decomposition due to its divide-and-conquer structure. The program breaks down the task into:

- **Input Handling**
  - Convert user input from a text field into a list of integers
  - OR generate a random list using the dedicated GUI button

- **Recursive Splitting**
  - Divide the list into left and right halves until each sublist contains only one element

- **Merging**
  - Combine sorted halves into a new sorted list
  - Log every comparison, extraction, and merge action

- **Output Formatting**
  - Display results with indentation to reveal recursion depth
  - Present all steps in a readable, top-to-bottom progression

Each component works independently but contributes to a unified workflow.

---

## **2. Pattern Recognition**
The algorithm exhibits predictable and repeating patterns:

- **Splitting Pattern**
  - All lists are split at the midpoint, regardless of content
  - The splitting depth increases until reaching individual elements

- **Merging Pattern**
  - Always compare the *first* elements from each half
  - Always take the smaller value first
  - Append leftovers after one side empties
  - These patterns remain consistent across all input types

- **Random Generation Pattern**
  - Random integers within a fixed range (0–100 by default)
  - Fixed length unless modified (default = 8 values)
  - Ensures predictable structure but varied content

Recognizing these patterns allows the user to understand *why* the algorithm behaves consistently, even with different inputs.

---

## **3. Abstraction**
The program hides irrelevant technical details and exposes only what is needed for learning:

- Users interact with:
  - A **textbox** for manual input  
  - A **button** to generate a random array  
  - A **button** to start Merge Sort  
  - A **large text output** area that shows all algorithm steps

- Hidden from the user:
  - Recursion stack operations
  - Internal indices
  - Memory allocation details
  - Exception handling logic

- Indentation abstraction:
  - Each recursion depth adds spaces before log entries  
  - This mimics a tree structure and helps users visualize depth-first execution

This level of abstraction allows learners to focus on the *conceptual process* instead of implementation mechanics.

---

## **4. Algorithmic Thinking**
Merge Sort is built upon strong algorithmic reasoning:

1. **Divide**
   - Cut the list into two halves repeatedly
   - Reduces a complex problem into smaller solvable components

2. **Conquer**
   - Recursively sort each half independently
   - Base case is reached when a list has 0 or 1 elements

3. **Combine**
   - Merge the two sorted halves
   - Carefully compare values and build an ordered output list

The Random Array button also reflects algorithmic thinking by automating the creation of example inputs that demonstrate varied algorithmic behavior.

---

# **How to Run Locally**

### **1. Install dependencies**
```
pip install -r requirements.txt
```

### **2. Run the application**
```
python app.py
```

### 3. Open the Gradio Link Printed in the Terminal

After running the application, Gradio will display two URLs in your terminal:

- A **local URL** (usually `http://127.0.0.1:7860`)
- A **temporary public Gradio URL** (looks like `https://xxxxx.gradio.live`)

Click either link to open the Merge Sort Visualizer in your browser.

The interface loads automatically once the link is opened.

---

## **Hugging Face App Link**

https://huggingface.co/spaces/jmuir1/CISC_121-FinalProject

---

# **Algorithm Explanation (Simple Overview)**

## **1. Split**
The list is recursively divided into halves until each sublist contains one element.
This ensures every piece is trivially sorted.

## **2. Sort (Base Case)**
A single-element list is returned directly because it is already sorted.
This is the foundation of the recursion.

## **3. Merge**
Two sorted halves are combined:

- Compare the first elements of each half
- Append the smaller value to the output list
- Continue until one half is empty
- Append remaining elements

---

### **Time & Space Complexity**

Scenario | Complexity
---------|------------
Best Case | O(n log n)
Average Case | O(n log n)
Worst Case | O(n log n)
Space Complexity | O(n)

This makes Merge Sort extremely efficient and predictable, outperforming simplistic O(n²) algorithms such as Bubble Sort, Insertion Sort, and Selection Sort.

---

# **Testing & Verification**

The application was thoroughly tested using a wide range of list types and input behaviors.

---

## **1. Small List**
Input:  
5, 1, 8, 2, 7

Expected Result:  
Correct splits, merges, and final sorted order.

---

## **2. Larger List**
Input:  
38, 27, 43, 3, 9, 82, 10

Expected Result:  
Proper recursive breakdown and final sorted output.

---

## **3. Edge Cases**
Case | Input | Expected Behavior | Result
-----|--------|--------------------|--------
Empty list | "" | Return base-case output | Passed
Single number | 7 | Return unchanged | Passed
Repeated values | 5, 5, 1, 5 | Stable merge logic | Passed
Negative nums | -3, 10, -1 | Correct ordering | Passed
Invalid input | a, b, c | Show error message | Passed
---

### **Edge Case Screenshots**

**Repeated values (5, 5, 1, 5)**  

![Repeated Values](screenshots/MergeSortTest_1.png)`

**Negative numbers (-1, 10, -3)**  

![Negative Numbers](screenshots/MergeSortTest_2.png)`

**Invalid input (a, b, c)**  

![Invalid Input](screenshots/MergeSortTest_3.png)`

---


## **4. Random Array Button Tests**
Example Generated Input:  
34, 2, 78, 11, 5, 0, 45, 12

Verification:
- Correct splitting and merging behavior  
- Handles unpredictable data reliably  
- Confirms both UI and algorithm resilience  

---

# **Steps to Use the App**

1. Enter a comma-separated list **or click "Generate Random Array"**
2. Click **"Run Merge Sort"**
3. Watch the detailed breakdown of recursive splitting and merging
4. Scroll to observe the full process
5. View the final sorted output at the bottom

---

# **Author & Acknowledgment**

Author: James Muir

Created for CISC 121 – Introduction to Computer Science  

Merge Sort algorithm, UI design, testing procedures, and random array feature were developed in accordance with course guidelines.  

---

# **AI Level 4 Usage Disclaimer**

This project was developed with permitted assistance from generative AI tools under the **CISC 121 Level 4 AI usage guidelines**.  
AI support was used strictly for:

- Explaining programming concepts  
- Improving code readability  
- Debugging assistance  
- Formatting documentation  
- Generating example inputs for testing  
- Enhancing clarity of written descriptions

All final code, logic, testing decisions, and structural design were reviewed, verified, and approved by the author to ensure full understanding and academic integrity.

No AI-generated code or text was used without modification, verification, or author oversight.  
Responsibility for all content, correctness, and originality remains solely with the author.

---


