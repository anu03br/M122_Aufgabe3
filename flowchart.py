import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(12, 16))

# Function to add a box to the flowchart
def add_box(ax, text, xy, boxstyle="round,pad=0.3", boxcolor="lightblue", textcolor="black"):
    ax.add_patch(patches.FancyBboxPatch(xy, width=8, height=2, boxstyle=boxstyle, 
                                        edgecolor="black", facecolor=boxcolor))
    ax.text(xy[0] + 4, xy[1] + 1, text, ha="center", va="center", fontsize=10, color=textcolor)

# Function to add an arrow between boxes
def add_arrow(ax, xy_from, xy_to):
    ax.annotate("", xy=(xy_to[0] + 4, xy_to[1]), xytext=(xy_from[0] + 4, xy_from[1] + 1.5),
                arrowprops=dict(arrowstyle="->", lw=2))

# Add boxes and arrows based on the flowchart steps
add_box(ax, "Start", (0, 40))
add_box(ax, "Parse Arguments\n- Check for -f flag\n- Set dry_run based on flag", (0, 36))
add_arrow(ax, (0, 40), (0, 36))

add_box(ax, "Input Folder Path\n- Prompt user for folder path", (0, 32))
add_arrow(ax, (0, 36), (0, 32))

add_box(ax, "Call compare_images(folder_path)", (0, 28))
add_arrow(ax, (0, 32), (0, 28))

add_box(ax, "List image files in folder\nInitialize duplicate_files list", (0, 24))
add_arrow(ax, (0, 28), (0, 24))

add_box(ax, "Loop through each image as original_file\n- If not in duplicate_files", (0, 20))
add_arrow(ax, (0, 24), (0, 20))

add_box(ax, "Open original_file and calculate pixel mean (pix_mean1)", (0, 16))
add_arrow(ax, (0, 20), (0, 16))

add_box(ax, "Loop through image_files to compare\nwith original_file", (0, 12))
add_arrow(ax, (0, 16), (0, 12))

add_box(ax, "If another file (file_check) is not the same as original_file", (0, 8))
add_arrow(ax, (0, 12), (0, 8))

add_box(ax, "Open file_check and calculate pixel mean (pix_mean2)", (0, 4))
add_arrow(ax, (0, 8), (0, 4))

add_box(ax, "If pix_mean1 equals pix_mean2\nadd file_check to duplicate_files", (0, 0))
add_arrow(ax, (0, 4), (0, 0))

add_box(ax, "Return duplicate_files", (0, -4))
add_arrow(ax, (0, 0), (0, -4))

add_box(ax, "Check dry_run status", (0, -8))
add_arrow(ax, (0, -4), (0, -8))

add_box(ax, "If dry_run is True:\n- Print duplicates\n- Print test run message", (-6, -12))
add_arrow(ax, (0, -8), (-6, -12))

add_box(ax, "If dry_run is False:\n- Print duplicates\n- Print delete message", (6, -12))
add_arrow(ax, (0, -8), (6, -12))

add_box(ax, "End", (0, -16))
add_arrow(ax, (-6, -12), (0, -16))
add_arrow(ax, (6, -12), (0, -16))

# Set limits and hide axes
ax.set_xlim(-10, 10)
ax.set_ylim(-20, 42)
ax.axis('off')

# Show the plot
plt.show()
