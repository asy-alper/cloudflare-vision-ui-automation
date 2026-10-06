\# Vision-Based UI Automation \& HCI Proof of Concept



\*\*Disclaimer:\*\* This project was developed strictly for educational purposes and academic research regarding Human-Computer Interaction (HCI) and standard web automation detection limitations. It is not intended to bypass security mechanisms or violate any website's Terms of Service. The author assumes no responsibility for any misuse.



\## Overview

This repository contains a Python-based Proof of Concept (PoC) demonstrating how visual recognition and simulated biometric mouse movements can be utilized in GUI automation. Rather than relying on DOM manipulation (which is often restricted or monitored), this script uses Computer Vision techniques to interact with dynamically rendered UI elements.



\## Key Engineering Features

\* \*\*Region of Interest (ROI) Optimization:\*\* Instead of scanning the entire screen, the script calculates a dynamic bounding box (40% width, 80% height of the center screen) to reduce CPU overhead and drastically decrease image processing time.

\* \*\*Computer Vision Tuning:\*\* Utilizes `pyautogui.locateCenterOnScreen` with grayscale conversion and confidence thresholding (0.8) for rapid and accurate UI element detection.

\* \*\*Human-like Trajectory Simulation:\*\* 

&#x20; \* Implements `pyautogui.easeInOutQuad` easing functions to simulate the natural acceleration and deceleration of human mouse movements.

&#x20; \* Adds randomized micro-delays (0.1s - 0.3s) before click events to mimic human hesitation.

&#x20; \* Ensures cursor displacement post-interaction to avoid triggering unwanted tooltips or hover states.



\## Technologies Used

\* Python 3

\* PyAutoGUI (for coordinate mapping and I/O simulation)

\* OpenCV (under the hood for confidence-based image recognition)



\## Setup

1\. Ensure the target UI element image (e.g., `target\_element.png`) is in the root directory.

2\. Run the script. An emergency fail-safe is enabled; dragging the mouse to any corner of the screen will abort the process.

