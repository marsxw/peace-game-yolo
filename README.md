# Peace Game YOLOv8 Project

This project is a test implementation of a "Battle Royale" game using YOLOv8 for character recognition. It currently includes several key features and functionalities but also faces some challenges.

## 📂 Project Structure
- `aim.py`: Code for aiming at recognized characters.
- `main.ui`: The Qt UI file for the graphical interface.
- `main_ui.py`: Python file for handling the main UI logic.
- `test`: Test directory.
- `train`: Directory for training data and scripts.
- `utils.py`: Utility functions.
- `video`: Directory for video files.

## 🎮 Current Features
1. **Character Recognition and Aiming**: 
   - The YOLOv8 model is used to identify character positions, and the system automatically adjusts aim towards recognized characters.
   
2. **Mouse and Keyboard Event Capture**:
   - Captures user input events like mouse movements and keyboard actions for further processing and game interaction.
   
3. **Weapon and Attachment Recognition**:
   - Uses OpenCV to identify and compare weapons and attachments in the game image.

4. **Qt GUI**:
   - Provides a user interface for adjusting aiming parameters and configuring recoil settings for different weapons.

## 🚩 Current Issues
1. **Low YOLOv8 Detection Accuracy**:
   - The current dataset used for training is too small, leading to errors in character position detection.

2. **Incorrect Weapon Configuration Recognition**:
   - OpenCV sometimes misidentifies weapons and attachments, affecting the overall gameplay experience.

3. **Slow Multithreaded Interaction**:
   - The multithreading implementation is slow and consumes significant system resources, impacting performance.

## 🚀 Future Improvements
- **Increase Dataset Size**:
  - Improve the accuracy of the YOLOv8 model by expanding the training dataset with more diverse and accurate data.
  
- **Improve Weapon Recognition**:
  - Enhance the OpenCV recognition process for weapons and attachments to reduce misidentification errors.
  
- **Optimize Multithreading**:
  - Refactor the multithreading code to improve speed and reduce resource consumption, ensuring smoother gameplay.
