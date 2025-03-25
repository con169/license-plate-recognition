from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import localization

# get all connected regions and group together
label_image = measure.label(localization.binary_car_image)

# get max width, height and min width, height of license plate
plate_dimensions = (0.08*label_image.shape[0], 0.2*label_image.shape[0], .15*label_image.shape[1], 0.4*label_image.shape[1])
min_height, max_height, min_width, max_width = plate_dimensions
plate_objects_coordinates = []
plate_like_objects = []
fig, (ax1) = plt.subplots(1)
ax1.imshow(localization.gray_car_image, cmap="gray")

# create list of properties of all labelled regions using regionprops
for region in regionprops(label_image):
    if region.area < 50:
        continue

    # the bounding box coordinates
    min_row, min_col, max_row, max_col = region.bbox
    region_height = max_row - min_row
    region_width = max_col - min_col

    