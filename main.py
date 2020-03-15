from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from AppCredentials import AppCredentials
from UserCredentials import UserCredentials
from time import sleep
import re
import requests

class PyGramSalesBot:

    def findPhotosAndPublishOnIg(self, path, igUserId):
        file = open(path, "r")
        for line in file:
            creationUrl = "https://graph.facebook.com/v6.0/" + igUserId + "/media?image_url=" + line + "&caption=#BronzFonz"
            creationRequest = requests.post(creationUrl)
            creationData = creationRequest.json()
            print(creationData)

    def getUserInstagramAccountId(self, pageId, accessToken, userCredentials):
        IgAccountUrl = "https://graph.facebook.com/v6.0/" + pageId + "?fields=instagram_business_account&access_token=" + accessToken
        IgAccountIdRequest = requests.get(IgAccountUrl)
        IgAccIdData = IgAccountIdRequest.json()
        userCredentials.setIgAccountId(IgAccIdData["instagram_business_account"]["id"])

    def getUserPageId(self, userId, accessToken, userCredentials):
        pageUrl = "https://graph.facebook.com/v6.0/" + userId + "/accounts?access_token=" + accessToken
        pageRequest = requests.get(pageUrl)
        pageData = pageRequest.json()
        pageDataList = pageData["data"]
        userCredentials.setPageId(pageDataList[0]["id"])

    def checkUserPermissions(self, userId, accessToken):
        permissionUrl = "https://graph.facebook.com/v6.0/" + userId + "/permissions?access_token=" + accessToken
        permissionRequest = requests.get(permissionUrl)
        permissionResponse = permissionRequest.json()
        print(permissionResponse)

    def obtainAppAccessToken(self, appCredentials):
        tokenUrl = "https://graph.facebook.com/oauth/access_token?client_id=" + appCredentials.getAppId() \
                   + "&client_secret=" + appCredentials.getAppSecret()\
                   + "&grant_type=client_credentials"
        appAccessTokenRequest = requests.get(tokenUrl)
        data = appAccessTokenRequest.json()
        appCredentials.setAppAccessToken(data["access_token"])

    def validateAccessTokenObtainUser(self, accessToken, appAccessToken, userCredentials):
        validationUrl = "https://graph.facebook.com/debug_token?input_token=" + accessToken + "&access_token=" + appAccessToken
        validationRequest = requests.get(validationUrl)
        validationResponse = validationRequest.json()
        print(validationResponse)
        responseDict = validationResponse["data"]
        userCredentials.setUserId(responseDict["user_id"])

    def extractAccessTokenFromURL(self, url):
        responseList = url.split(",")
        for response in responseList:
            if response.__contains__("access_token=") and response.__contains__("urlFragment"):
                print("Response that contains the token" + response)
                accessToken = re.search('#access_token=(.*)&data_access', response)
                print("Access Token: " + accessToken.group(1))
                return accessToken.group(1)

    def __init__(self):

        appCredentials = AppCredentials()
        userCredentials = UserCredentials()
        chrome_option = webdriver.ChromeOptions()
        options = {"profile.default_content_setting_values.notifications" : 2}
        chrome_option.add_experimental_option("prefs", options)
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance':'ALL'}
        chrome = webdriver.Chrome(desired_capabilities=capabilities, chrome_options=chrome_option)

        loginDialogUrl = "https://www.facebook.com/v6.0/dialog/oauth?client_id=" + appCredentials.getAppId() + \
                      "&redirect_uri=" + appCredentials.getRedirectUri() + \
                      "&state=" + appCredentials.getStateParameters() + \
                      "&response_type=" + appCredentials.getResponseType() + "&scope=" + appCredentials.getScope()
        chrome.get(loginDialogUrl)
        sleep(2)
        chrome.find_element_by_xpath("//*[@id='email']").send_keys(userCredentials.getUserEmail())
        chrome.find_element_by_xpath("//*[@id='pass']").send_keys(userCredentials.getUserPassword())
        chrome.find_element_by_xpath("//*[@id='loginbutton']").click()
        chrome.find_element_by_xpath("//*[@id='platformDialogForm']/div/div[1]/div/div/div/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/span").click()
        sleep(5)

        logs = chrome.get_log('performance')
        for logEntry in logs:
            if logEntry["message"].__contains__("access_token=") and logEntry["message"].__contains__("Network.requestWillBeSent"):
                userCredentials.setAccessToken(self.extractAccessTokenFromURL(logEntry["message"]))

        self.obtainAppAccessToken(appCredentials)
        self.validateAccessTokenObtainUser(userCredentials.getAccessToken(), appCredentials.getAppAccessToken(), userCredentials)
        self.checkUserPermissions(userCredentials.getUserId(), userCredentials.getAccessToken())
        self.getUserPageId(userCredentials.getUserId(), userCredentials.getAccessToken(), userCredentials)
        self.getUserInstagramAccountId(userCredentials.getPageId(), userCredentials.getAccessToken(), userCredentials)
        self.findPhotosAndPublishOnIg(userCredentials.getProductImagesPath(), userCredentials.getIgAccountId())

PyGramSalesBot()