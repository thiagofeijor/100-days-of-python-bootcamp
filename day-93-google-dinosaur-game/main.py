import pyautogui
import numpy as np
import cv2

while True:
    image = pyautogui.screenshot(region=(90,250,130,180))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    black_pixel_count = np.sum(image < 100)
    white_pixel_count = np.sum(image > 100)
    print(black_pixel_count, white_pixel_count)

    if black_pixel_count > 4000 and black_pixel_count < 30000:
        pyautogui.press('up')
        print('up1')
    elif white_pixel_count > 2000 and white_pixel_count < 30000:
        pyautogui.press('up')
        print('up2')

    cv2.imshow('image', image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
