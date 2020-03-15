class UserCredentials:

    __email = ""
    __password = ""
    __pathOfProductImages = ""
    __accessToken = ""
    __userId = ""
    __pageId = ""
    __igAccId = ""

    def getUserEmail(self):
        return self.__email

    def getUserPassword(self):
        return self.__password

    def getAccessToken(self):
        return self.__accessToken

    def setAccessToken(self, accessToken):
        self.__accessToken = accessToken

    def setUserId(self, userId):
        self.__userId = userId

    def getUserId(self):
        return self.__userId

    def getPageId(self):
        return self.__pageId

    def setPageId(self, pageId):
        self.__pageId = pageId

    def getIgAccountId(self):
        return self.__igAccId

    def setIgAccountId(self, igAccId):
        self.__igAccId = igAccId

    def getProductImagesPath(self):
        return self.__pathOfProductImages