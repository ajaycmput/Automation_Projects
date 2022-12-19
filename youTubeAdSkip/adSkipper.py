import pyautogui

pyautogui.FAILSAFE = True

def findAndClick():
    while True:
        videoAdCords = pyautogui.locateCenterOnScreen("play.png")
        bannerCoords = pyautogui.locateCenterOnScreen("bannerad.png")
        blackBannerCords = pyautogui.locateCenterOnScreen("black banner.png")

        if videoAdCords or bannerCoords or blackBannerCords is not None:
            break

        if videoAdCords is not None:
            pyautogui.click(videoAdCords)
        elif bannerCoords is not None:
            pyautogui.click(bannerCoords)
        if blackBannerCords is not None:
            pyautogui.click(blackBannerCords)

        findAndClick()

findAndClick()