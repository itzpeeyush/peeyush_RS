import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(staticMode=False, maxHands=2)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=False)

    if hands:
        for hand in hands:
            
            bbox = hand['bbox']  
            hand_type = hand['type']
            invert = 'Right' if hand_type == 'Left' else 'Left'
            cv2.rectangle(img,(bbox[0],bbox[1]),(bbox[0] + bbox[2]+20, bbox[1] + bbox[3]+20), (0, 255, 0), 2)
            cv2.putText(img, invert, (bbox[0], bbox[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            lmList = hand['lmList']
            for idx, lm in enumerate(lmList):
                x, y, z = lm
                cv2.circle(img, (x, y), 5, (0, 255, 0), cv2.FILLED)
                cv2.line(img,(x,y),(lmList[idx+1][0], lmList[idx+1][1]), (255, 0, 0), 2) if idx < len(lmList) - 1 else None
                fingers = detector.fingersUp(hand)
                cv2.putText(img, str(fingers.count(1))+'fingers up', org=(bbox[0] - 30, bbox[1] - 40), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 255), thickness=2)
    cv2.imshow("Hand", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break