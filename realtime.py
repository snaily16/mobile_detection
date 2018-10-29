import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import os


options = {
	'model': 'cfg/yolo.cfg',
	'load' : 'bin/yolov2.weights',
	'threshold' : 0.6,
	'gpu' : 1.0
	}
	
tfnet = TFNet(options)
colors = [tuple(np.random.rand(3)) for i in range(10)]

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

#FILE_OUTPUT ='output.avi'

#fourcc = cv2.VideoWriter_fourcc(*'X264')
#out = cv2.VideoWriter(FILE_OUTPUT,fourcc, 20.0, (640,480))
i=0
while True:
	stime = time.time()
	ret, frame = capture.read()
	results = tfnet.return_predict(frame)
	
	if ret:
		for color, result in zip(colors, results):
			tl = (result['topleft']['x'], result['topleft']['y'])
			br = (result['bottomright']['x'], result['bottomright']['y'])
			label = result['label']
			confidence = result['confidence']
			text = "{}: {:.0f}%".format(label, confidence * 100)
			if label == 'cell phone':
				frame = cv2.rectangle(frame, tl, br, color, 7)
				frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)
				
				#taking screenshots
				value, image = capture.read()
				cv2.imwrite('pic'+str(i)+'.png', frame)
				os.system('spd-say "warning, mobile phone not allowed"')
				i+=1
				#f=cv2.flip(frame,1)
				#out.write(f)
		cv2.imshow("frame", frame)
		print('FPS {:.1f}'.format(1/(time.time() - stime)))
		print (i)
		if cv2.waitKey(1) & 0xff == ord('q'):
			break
			
	else:
		capture.release()
		cv2.destroyAllWindows()
		break
