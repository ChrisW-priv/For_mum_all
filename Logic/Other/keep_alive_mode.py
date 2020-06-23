def keep_alive():
	import pyautogui
	try:
		width, height= pyautogui.size()
		while True:
			for column in range(height)[50:]:
				for pix in range(width)[50:]:
					pyautogui.moveTo(pix, column)
	except Exception:
		pass
