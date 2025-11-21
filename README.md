This project presents a comprehensive real-time Face Mesh Detection system developed using OpenCV and MediaPipe, offering an accurate and efficient solution for tracking detailed facial landmarks through a live webcam feed. The system uses MediaPipe’s advanced FaceMesh model, which extracts and maps 468 high-precision facial landmarks for each detected face. This level of detail makes the project suitable for a wide range of applications including facial analysis, emotion detection, virtual reality, augmented reality, and AI-based surveillance systems.

A key feature of this project is its capability to automatically detect and select a working camera from the user’s device. Instead of manually specifying a camera index, the script scans multiple camera ports and connects to the first functioning one. This feature makes the application more user-friendly, flexible, and adaptable for systems using multiple webcams or external cameras.

The system continuously processes incoming frames from the camera in real time. Each frame is converted into RGB format and passed through the FaceMesh processing pipeline. When faces are detected, the model generates 468 landmark points per face, which are then converted from normalized coordinates into pixel positions. These landmarks are visualized through a mesh overlay drawn directly on the face, enabling users to observe facial structure, movement, and expressions with high accuracy.

For performance evaluation, the application calculates and displays real-time FPS (Frames Per Second). This feature helps users monitor how efficiently the system is running, especially important for developers optimizing performance or deploying the solution on various hardware platforms.

The project is built around a clean, modular design. The core logic is encapsulated in a reusable FaceMeshDetector class, making it easy to integrate this functionality into larger projects. Developers can also adjust configuration parameters such as detection confidence, tracking confidence, maximum number of faces, and whether to draw the mesh overlay.

Overall, this project serves as a robust foundation for anyone interested in computer vision, face analysis, or real-time AI applications. It is well-structured, easily customizable, and ready for practical deployment or further research. 
🚀 Features

Real-time face mesh detection

Supports multiple faces

Maps 468 facial landmarks per face

Automatic camera detection

FPS display for performance monitoring

Modular and reusable design

Fully customizable detection settings
