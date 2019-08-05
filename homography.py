
import cv2
import numpy as np
import matplotlib.pyplot as plt
def mouse_handler(event, x, y, flags, data) :
    
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(data['im'], (x,y),3, (0,0,255), 5, 16);
        cv2.imshow("Image", data['im']);
        if len(data['points']) < 4 :
            data['points'].append([x,y])


def get_four_points(im):
    # Set up data to send to mouse handler
    data = {}
    data['im'] = im.copy()
    data['points'] = []
    
    #Set the callback function for any mouse event
    cv2.imshow("Image",im)
    cv2.setMouseCallback("Image", mouse_handler, data)
    cv2.waitKey(0)
    
    # Convert array to np.array
    points = np.vstack(data['points']).astype(float)
    
    return points

im_src = cv2.imread("5.png")
im_src = cv2.resize( im_src, (600,400))

# Destination image
size = (300,400,3)

im_dst = np.zeros(size, np.uint8)
pts_dst = np.array(
                    [
                    [0,0],
                    [size[0] - 1, 0],
                    [size[0] - 1, size[1] -1],
                    [0, size[1] - 1 ]
                    ], dtype=float
                    )



cv2.imshow("Image", im_src)
pts_src = get_four_points(im_src);

# a = [[ 518. , 708.],
#      [518. , 1033.],
#      [772., 1033.],
#      [  772., 708.]]

# pts_src = np.array(a)
# print(pts_src)


# Calculate the homography
h, status = cv2.findHomography(pts_src, pts_dst)
# Warp source image to destination
im_dst = cv2.warpPerspective(im_src, h, size[0:2])

# Show output
# plt.imshow(im_dst)
cv2.imshow("Image", im_dst)
cv2.waitKey(0)
