from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
import imutils
import cv2
import winsound

frequency = 2500
duration = 1000

def eyeAspectRatio(eye):
    #Vertical
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    #Horizontal
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

count = 0
earThresh = 0.3 #distance between vertical eye coordinate Threshold
earFrames = 48 #consecutive frames for eye closure
shapePredictor = "shape_predictor_68_face_landmarks.dat"
cam = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shapePredictor)
#get the coord of left & right eye
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
while True:
    _, frame = cam.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        
        leftEAR = eyeAspectRatio(leftEye)
        rightEAR = eyeAspectRatio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 0, 255), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 0, 255), 1)

        if ear < earThresh:
            count += 1

            if count >= earFrames:
                cv2.putText(frame, "DROWSINESS DETECTED", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                winsound.Beep(frequency, duration)
        else:
            count = 0

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
    
cam.release()
cv2.destroyAllWindows()