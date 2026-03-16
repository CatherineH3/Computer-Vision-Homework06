# Computer-Vision-Homework06
Homework06 Submission for Computer Vision


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

Reflections:
Through this exercise, I learned about inverse warping and how it’s different from the usual forward mapping. In the original code, we were looping through the source image and putting pixels into the output, but this sometimes left gaps because some output pixels never got a value. This made the image have a bunch of weird lines and missing spots. To fix it, I switched things around and looped over each pixel in the output image, figuring out exactly where it came from in the original image. This “inverse mapping” makes sure every pixel in the transformed image gets a value, so there are no holes or missing lines. I only had to change a few lines: the loops now go over the output pixels, and each output pixel is assigned a color from its corresponding spot in the source image. Doing this made the warped image complete and gave me a better understanding of how pixel mapping works in image transformations. Overall, this exercise helped me see why the order of looping and the direction of mapping really matters when working with images.
