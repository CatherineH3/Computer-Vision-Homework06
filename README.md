# Computer-Vision-Homework06
Homework06 Submission for Computer Vision

*Catherine Healy*

Here is the original image:

<img width="648" height="494" alt="image" src="https://github.com/user-attachments/assets/24e8c3fa-f2c0-4fa4-875f-323968b9c40b" />


Next, I select the corners of the image:

<img width="650" height="496" alt="image" src="https://github.com/user-attachments/assets/e47abe83-5569-4c64-b04c-73f903b5bb92" />


I then get a warped image with many missing points:

<img width="896" height="368" alt="image" src="https://github.com/user-attachments/assets/d234d0fc-8333-4b7c-82d0-b453cb2c81d3" />


After applying inverse warping, this is the final result:

<img width="899" height="369" alt="image" src="https://github.com/user-attachments/assets/23b3ac13-65d9-4a4b-ae07-b21e5bd086fb" />


Please note:
I had to modify the dimensions of the display code because it was too large to fit properly on my computer screen.

# Reflection:

In the original forward-mapping approach, I noticed that some areas of the warped image were denser than others. It seems like the transformation stretches parts of the image unevenly. The upper left corner of the artwork gets stretched more than the areas closer to me. When I loop over the source pixels and map them forward, some output pixels don’t get any value, especially in the stretched regions, which is why those corners have lots of missing spots. Areas that are closer (bottom right corner) and less stretched get more source pixels landing on them, so they look denser and more complete. Using inverse mapping fixes this because I loop over the output pixels instead and figure out where each one comes from in the original image, making sure every pixel gets a value no matter how stretched it is.

From this exercise, I learned more about how inverse mapping works. In the original code, I was looping through the source image and putting pixels into the output, but this sometimes left gaps because some output pixels never got a value. This made the image have a bunch of weird lines and missing spots. To fix it, I switched things around and looped over each pixel in the output image, figuring out exactly where it came from in the original image. This “inverse mapping” makes sure every pixel in the transformed image gets a value, so there are no holes or missing lines. I only had to change a few lines: the loops now go over the output pixels, and each output pixel is assigned a color from its corresponding spot in the source image. Doing this made the warped image complete and gave me a better understanding of how pixel mapping works in image transformations. Overall, this exercise helped me see why the order of looping and the direction of mapping really matters when working with images.

If you look at my code, you'll also note that I tried an alternate method, which was successful (note it is temporarily commented out). It is a more concise method that does the same thing, but uses a grid and cv2.perspectiveTransform to compute all source coordinates at once and fill the output image in a single step.
