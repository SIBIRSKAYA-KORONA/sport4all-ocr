import cv2
import numpy as np
import pytesseract

# import matplotlib.pyplot as plt

img = cv2.imread('data/fiba_proto_1.jpg', cv2.THRESH_BINARY)

img_bin = 255 - img
thresh1, img_bin_otsu = cv2.threshold(
    img_bin, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

vertical_kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT, (1, np.array(img).shape[1] // 100))
eroded_image = cv2.erode(img_bin_otsu, vertical_kernel, iterations=3)
vertical_lines = cv2.dilate(eroded_image, vertical_kernel, iterations=3)

hor_kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT, (np.array(img).shape[1] // 100, 1))
eroded_image = cv2.erode(img_bin, hor_kernel, iterations=5)
horizontal_lines = cv2.dilate(eroded_image, hor_kernel, iterations=5)

vertical_horizontal_lines = cv2.addWeighted(
    vertical_lines, 0.5, horizontal_lines, 0.5, 0.0)
vertical_horizontal_lines = cv2.erode(
    ~vertical_horizontal_lines, kernel, iterations=3)

thresh, vertical_horizontal_lines = cv2.threshold(vertical_horizontal_lines, 128,
                                                  255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

bitxor = cv2.bitwise_xor(img, vertical_horizontal_lines)
bitnot = cv2.bitwise_not(bitxor)

# detect contours for following box detection
contours, hierarchy = cv2.findContours(
    vertical_horizontal_lines, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# sort all the contours by top to bottom
contours, bounding_boxes = zip(*sorted(zip(contours, [cv2.boundingRect(cnt) for cnt in contours]),
                                       key=lambda b: b[1][1], reverse=False))

# creating a list of heights for all detected boxes
heights = [bounding_boxes[i][3] for i in range(len(bounding_boxes))]
mean = np.mean(heights)
box = []

# get position (x,y), width and height for every contour and show the contour on image
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w < 1000 and h < 500:
        image = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        box.append([x, y, w, h])

# sorting the boxes to their respective row and column
rows = []
columns = []
previous = box[0]
columns.append(previous)

for i in range(1, len(box)):
    if box[i][1] <= previous[1] + mean / 2:
        columns.append(box[i])
        previous = box[i]
        if i == len(box) - 1:
            rows.append(columns)
    else:
        rows.append(columns)
        columns = []
        previous = box[i]
        columns.append(previous)

# calculating maximum number of cells
max_cols = 0
max_cols_idx = 0
for i in range(len(rows)):
    tmp = len(rows[i])
    if tmp > max_cols:
        max_cols = tmp
        max_cols_idx = i

# retrieving the center of each column
centers = np.array([int(cell[0] + cell[2] / 2) for cell in rows[max_cols_idx]])
centers.sort()

table = []
for row in rows:
    sort_row = [[] for k in range(max_cols)]

    for cell in row:
        diff = abs(centers - (cell[0] + cell[2] / 4))
        idx = list(diff).index(min(diff))
        sort_row[idx] = cell

    table.append(sort_row)

# from every single image-based cell/box the strings are extracted via pytesseract and stored in a list

name_column = 1
point_column = 21

for row in table:
    for idx in (name_column, point_column):
        cell = row[idx]
        if len(cell) == 0:
            continue

        y, x, w, h = cell[0], cell[1], cell[2], cell[3]
        final_img = bitnot[x:x+h, y:y+w]

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
        border = cv2.copyMakeBorder(
            final_img, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=[255, 255])
        resizing = cv2.resize(border, None, fx=2, fy=2,
                              interpolation=cv2.INTER_CUBIC)
        dilation = cv2.dilate(resizing, kernel, iterations=1)
        erosion = cv2.erode(dilation, kernel, iterations=2)

        tmp = bitnot.copy()
        cv2.rectangle(tmp, (x, y), (x+h, y+w), (0, 255, 0), 4)

        out = ''
        if idx == name_column:
            out = pytesseract.image_to_string(
                erosion, config='--oem 3 --psm 10', lang='rus')

        if idx == point_column:
            out = pytesseract.image_to_string(
                erosion, config='-c tessedit_char_whitelist=0123456789 --oem 3 --psm 10')

        print(out)
