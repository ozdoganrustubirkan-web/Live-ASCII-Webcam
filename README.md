Live ASCII Webcam

This Python project converts the live video stream from your computer's webcam directly into black and white ASCII character art within the terminal screen. It uses image processing (OpenCV) and terminal color codes (ANSI) to create a retro video effect.

Features

Live Stream: Real-time image capture from the camera.

Black/White ASCII: Character mapping from dark to light based on image brightness (@%#*+=-:. ).

Fast Conversion: Uses NumPy for quick and efficient image processing.

Terminal Color: Uses special black text and white background color codes for the ASCII output.

Installation

Ensure you have Python installed on your system before running the project.

Dependencies

This project requires two main libraries:

opencv-python (cv2): For capturing image and camera stream.

numpy: For fast and efficient processing of image data.

Installing Dependencies

Install all required libraries using the following command:

pip install opencv-python numpy


Usage

Once the libraries are installed, running the project is very straightforward.

Starting the Application

Navigate to the directory containing the ascii_webcam.py file in your terminal and run the following command:

python ascii_webcam.py


The camera will automatically open, and the stream will begin converting to ASCII art in the terminal.

Exit

While the application is active, focus on the window and press the q key to safely terminate the program.

Configuration and Settings

You can customize the output by modifying the variables at the beginning of the Python file:

Variable Name

Description

Value Range

ASCII_CHARS

Character set ordered from dark to light.

String (e.g., '$@B%...')

DOWNSCALE_FACTOR

Image size reduction factor. The higher the value, the smaller and faster the output.

Recommended: 6 to 12

FRAME_RATE

Wait time between frames (in seconds). Controls the stream speed.

Recommended: 0.03 to 0.1

How It Works (Working Principle)

The convert_image_to_ascii_bw_reverse function performs the following steps:

Grayscale: The colored frame is converted to black and white (grayscale).

Resizing: The image resolution is reduced using the DOWNSCALE_FACTOR.

Brightness Mapping: Each pixel's brightness value (0-255) is mapped to a character in the ASCII_CHARS list. (Dark pixels are assigned to dense characters like @, and light pixels to space-like characters like ..)

Color Application: The terminal background is set, colors are applied to the characters, and the output is cleared and printed for each new frame.

Contributing

If you wish to contribute to development, report bugs, or suggest new features, please open an "Issue" or send a "Pull Request".
