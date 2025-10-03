import allure

def attach_regres(response):
    request = response.request

    allure.attach(request.method, name='Method of request',
                  attachment_type=allure.attachment_type.TEXT)

    allure.attach(request.method, name='URL of request',
                  attachment_type=allure.attachment_type.TEXT)

    allure.attach(request.method, name='Body of request',
                  attachment_type=allure.attachment_type.JSON)