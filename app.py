import gradio as gr

# ----------------------------------------
# Merge Sort Visualizer
# ----------------------------------------
def merge_sort_visualized(arr, depth=0, steps=None):
    # Initialize the list that stores all steps (only on first call)
    if steps is None:
        steps = []

    # Indentation helps visualize recursion depth in the output
    indent = "  " * depth
    steps.append(f"{indent}Splitting: {arr}")

    # Base case: a list of length 0 or 1 is already sorted
    if len(arr) <= 1:
        steps.append(f"{indent}Returning (base case): {arr}")
        return arr, steps

    # Find the midpoint to divide the list into two halves
    mid = len(arr) // 2

    # Recursively sort the left and right halves
    left_half, steps = merge_sort_visualized(arr[:mid], depth + 1, steps)
    right_half, steps = merge_sort_visualized(arr[mid:], depth + 1, steps)

    # Now merge the two sorted halves
    merged = []
    i = j = 0
    steps.append(f"{indent}Merging: {left_half} + {right_half}")

    # Repeat until one half is exhausted
    while i < len(left_half) and j < len(right_half):
        # Compare elements and take the smaller one
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            steps.append(f"{indent}→ Taking {left_half[i]} from left")
            i += 1
        else:
            merged.append(right_half[j])
            steps.append(f"{indent}→ Taking {right_half[j]} from right")
            j += 1

    # Append any remaining elements from the left half
    while i < len(left_half):
        merged.append(left_half[i])
        steps.append(f"{indent}→ Taking remaining {left_half[i]} from left")
        i += 1

    # Append any remaining elements from the right half
    while j < len(right_half):
        merged.append(right_half[j])
        steps.append(f"{indent}→ Taking remaining {right_half[j]} from right")
        j += 1

    # Log the merged result at this recursion level
    steps.append(f"{indent}Merged result: {merged}")
    return merged, steps


# ----------------------------------------
# UI wrapper: converts user input into a list of ints
# ----------------------------------------
def run_merge_sort(list_str):
    # Safely convert input string into a list of integers
    try:
        arr = [int(x.strip()) for x in list_str.split(",") if x.strip() != ""]
    except:
        return "Invalid input. Enter comma-separated integers."

    # Run merge sort and get the generated steps
    sorted_arr, steps = merge_sort_visualized(arr)

    # Display the entire step-by-step visualization
    return "\n".join(steps)


# ----------------------------------------
# Gradio Interface
# ----------------------------------------
with gr.Blocks(title="Merge Sort Visualizer") as demo:

    # Title + instructions
    gr.Markdown("### 🔁 Merge Sort Visualizer — Step-by-Step Explanation")

    # Textbox for user list input
    list_input = gr.Textbox(
        label="Enter a list of numbers (comma-separated)",
        placeholder="Example: 38, 27, 43, 3, 9, 82, 10"
    )

    # Output box showing each sorting step
    output_box = gr.Textbox(
        label="Merge Sort Steps",
        lines=30
    )

    # Button to run the algorithm
    run_btn = gr.Button("Run Merge Sort")

    # Connect button → function → output
    run_btn.click(
        fn=run_merge_sort,
        inputs=list_input,
        outputs=output_box
    )

# Launch the web app
demo.launch()
