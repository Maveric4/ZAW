import cv2
import numpy as np
import copy
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('vid1_IR.avi')
threshold = 40 #40 #100
maxValue = 255

while(cap.isOpened()):
    ret, frame = cap.read()
    frame2 = copy.deepcopy(frame)
    IG = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(IG, threshold, maxValue, cv2.THRESH_BINARY)
    # thresh2 = cv2.adaptiveThreshold(G, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 2)
    # cv2.imshow('Thresh2', thresh2)

    # Morphological operations
    # kernel = np.ones((5, 5), np.uint8)
    kernel = np.ones((3, 3), np.uint8)
    median1 = cv2.medianBlur(thresh1, 7)
    opening1 = cv2.morphologyEx(median1, cv2.MORPH_OPEN, kernel)
    closing1 = cv2.morphologyEx(opening1, cv2.MORPH_CLOSE, kernel)

    kernel2 = np.ones((5, 5), np.uint8)
    closing2 = cv2.morphologyEx(median1, cv2.MORPH_CLOSE, kernel2, iterations=3)
    opening2 = cv2.morphologyEx(closing2, cv2.MORPH_OPEN, kernel2)

    # Indexation
    output = cv2.connectedComponentsWithStats(opening2, connectivity=8, ltype=cv2.CV_32S)
    # The first cell is the number of labels
    num_labels = output[0]
    # The second cell is the label matrix
    labels = output[1]
    # The third cell is the stat matrix
    # Statistics are accessed via stats[label, COLUMN] where available columns are defined below.
    #     cv2.CC_STAT_LEFT The leftmost (x) coordinate which is the inclusive start of the bounding box in the horizontal direction.
    #     cv2.CC_STAT_TOP The topmost (y) coordinate which is the inclusive start of the bounding box in the vertical direction.
    #     cv2.CC_STAT_WIDTH The horizontal size of the bounding box
    #     cv2.CC_STAT_HEIGHT The vertical size of the bounding box
    #     cv2.CC_STAT_AREA The total area (in pixels) of the connected component
    stats = output[2]
    # The fourth cell is the centroid matrix
    centroids = output[3]

    # print("num_labels", num_labels)
    # print("labels", labels)
    # print("stats", stats)
    # print("centroid", centroids)
    print(stats[:, 4])
    l_skip = list()
    for i in range(1, num_labels):
        value_to_add = 0
        if stats[i, 3] >= 1.5 * stats[i, 2] and stats[i, 4] >= 1200:  # 1000
            for j in list(range(num_labels)):
                if j != i:
                    if stats[j, 0] >= stats[i, 0] - 50 and stats[j, 0] + stats[j, 2] <= stats[i, 0] + stats[i, 2] + 50 and stats[i, 1] + stats[i, 3]/2 < stats[j, 1]:
                        value_to_add = np.max([value_to_add, stats[j, 3]])
                        l_skip.append(j)
                        print("i:", i)
                        print(" j:", j)
                        print("height: ", stats[j, 3])
            print("value to add:   ", value_to_add)
            if i not in l_skip:
                cv2.rectangle(frame, (stats[i, 0], stats[i, 1]), (stats[i, 0] + stats[i, 2], stats[i, 1] + stats[i, 3] + value_to_add), (0, 255, 0), 1)

    for i in range(num_labels):
        # if stats[i, 3] >= 1.5 * stats[i, 2]:
        cv2.rectangle(frame2, (stats[i, 0], stats[i, 1]), (stats[i, 0] + stats[i, 2], stats[i, 1] + stats[i, 3]), (0, 255, 0), 1)
        cv2.putText(frame2, "%f" % stats[i, 4], (stats[i, 0], stats[i, 1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
        cv2.putText(frame2, "%d" % i, (np.int(centroids[i, 0]), np.int(centroids[i, 1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0)) ## ??

    cv2.imshow('I', frame)
    cv2.imshow("Test", frame2)
    # cv2.imshow('IR', IG)
    # cv2.imshow('Thresh1', thresh1)
    # cv2.imshow('After morpho', closing1)
    # cv2.imshow('After morpho2', opening2)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # przerwanie petli po wcisnieciu klawisza ’q’
        break
cap.release()
cv2.destroyAllWindows()

