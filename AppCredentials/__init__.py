class AppCredentials:

    __appId = ""
    __appSecret = ""
    __redirectUri = "https://www.facebook.com/connect/login_success.html"
    __stateParameters = ""
    __responseType = "token"
    __scope = "instagram_basic,pages_show_list,manage_pages"
    __appAccessToken = ""

    def getAppId(self):
        return self.__appId

    def getAppSecret(self):
        return self.__appSecret

    def getRedirectUri(self):
        return self.__redirectUri

    def getStateParameters(self):
        return self.__stateParameters

    def getResponseType(self):
        return self.__responseType

    def getAppAccessToken(self):
        return self.__appAccessToken

    def setAppAccessToken(self, appAccessToken):
        self.__appAccessToken = appAccessToken

    def getScope(self):
        return self.__scope
