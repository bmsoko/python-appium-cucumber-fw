class Page:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_element_by_accessibility_id(self, *locator):
        return self.driver.find_element_by_accessibility_id(*locator)

    def click(self,*locator):
        e = self.find_element(*locator)
        e.click()

    def input(self, text, *locator):
        e = self.find_element(*locator)
        e.clear()
        e.send_keys(text)