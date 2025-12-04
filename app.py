import gradio as gr

# ----------------------------------------
# Merge Sort Visualizer
# ----------------------------------------
def merge_sort_visualized(arr, depth=0, steps=None):
    if steps is None:
        steps = []

    indent = "  " * depth
    steps.append(f"{indent}Splitting: {arr}")

    if len(arr) <= 1:
        steps.append(f"{indent}Returning (base case): {arr}")
        return arr, steps

    mid = len(arr) // 2

    left_half, steps = merge_sort_visualized(arr[:mid], depth+1, steps)
    right_half, steps = merge_sort_visualized(arr[mid:], depth+1, steps)

    merged = []
    i = j = 0
    steps.append(f"{indent}Merging: {left_half} + {right_half}")

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            steps.append(f"{indent}→ Taking {left_half[i]} from left")
            i += 1
        else:
            merged.append(right_half[j])
            steps.append(f"{indent}→ Taking {right_half[j]} from right")
            j += 1

    while i < len(left_half):
        merged.append(left_half[i])
        steps.append(f"{indent}→ Taking remaining {left_half[i]} from left")
        i += 1

    while j < len(right_half):
        merged.append(right_half[j])
        steps.append(f"{indent}→ Taking remaining {right_half[j]} from right")
        j += 1

    steps.append(f"{indent}Merged result: {merged}")
    return merged, steps


# ----------------------------------------
# UI wrapper
# ----------------------------------------
def run_merge_sort(list_str):
    try:
        arr = [int(x.strip()) for x in list_str.split(",") if x.strip() != ""]
    except:
        return "Invalid input. Enter comma-separated integers."

    sorted_arr, steps = merge_sort_visualized(arr)
    return "\n".join(steps)


# ----------------------------------------
# Gradio Interface
# ----------------------------------------
with gr.Blocks(title="Merge Sort Visualizer") as demo:
    gr.Markdown("### 🔁 Merge Sort Visualizer — Step-by-Step Explanation")

    list_input = gr.Textbox(
        label="Enter a list of numbers (comma-separated)",
        placeholder="Example: 38, 27, 43, 3, 9, 82, 10"
    )

    output_box = gr.Textbox(
        label="Merge Sort Steps",
        lines=30
    )

    run_btn = gr.Button("Run Merge Sort")
    run_btn.click(fn=run_merge_sort, inputs=list_input, outputs=output_box)

demo.launch()
