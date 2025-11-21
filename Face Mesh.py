import cv2
import mediapipe as mp
import time

class FaceMeshDetector:
    def __init__(self, staticMode=False, maxFaces=2,
                 minDetectionCon=0.5, minTrackCon=0.5):

        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh

        # Correct keyword arguments
        self.faceMesh = self.mpFaceMesh.FaceMesh(
            static_image_mode=self.staticMode,
            max_num_faces=self.maxFaces,
            min_detection_confidence=self.minDetectionCon,
            min_tracking_confidence=self.minTrackCon
        )

        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findFaceMesh(self, img, draw=True):
        if img is None:
            return img, []

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(imgRGB)
        faces = []

        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                ih, iw, ic = img.shape

                if draw:
                    self.mpDraw.draw_landmarks(
                        img,
                        faceLms,
                        self.mpFaceMesh.FACEMESH_TESSELATION,  # valid connections
                        landmark_drawing_spec=self.drawSpec,
                        connection_drawing_spec=self.drawSpec
                    )

                # Collect landmarks in pixels
                face = []
                for lm in faceLms.landmark:
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x, y])
                faces.append(face)

        return img, faces

# Function to automatically find working camera
def find_working_camera(max_index=5):
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"Using camera index {i}")
                return cap
        cap.release()
    print("No working camera found!")
    return None

def main():
    cap = find_working_camera()
    if cap is None:
        return

    pTime = 0
    detector = FaceMeshDetector(maxFaces=2)

    while True:
        success, img = cap.read()
        if not success or img is None:
            print("Failed to grab frame")
            continue

        img, faces = detector.findFaceMesh(img, draw=True)

        cTime = time.time()
        fps = 1 / (cTime - pTime) if pTime != 0 else 0
        pTime = cTime

        cv2.putText(img, f'FPS:{int(fps)}', (20, 70),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        cv2.imshow("Face Mesh", img)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
