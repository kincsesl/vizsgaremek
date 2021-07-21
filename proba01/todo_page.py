from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome(options=options)
driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/todo.html")


class TodoPage:
    def __init__(self):
        """ Param:
                todos list of tuple(str, str) - indulo todokat tartalmazo lista
                    first parameter either done-false or done-true
        """
        self.title_initial_value = "To do App"  # konstans felirat
        self.todos_initial_value = [('done-false', 'gather requirements for this "to do" app'),
                      ('done-false', 'build the app in angular'),
                      ('done-false', 'create selenium unit tests'),
                      ('done-false', 'build internal selenium grid, buy devices, fund & setup a test lab - $$$'),
                      ('done-false', 'hire 1 FTE to manage/maintain lab and browsers - even more $$$')]
        self.new_todo_text_initial_value = ""

        self.title_xpath = "//h2"
        self.todos_xpath = "//li/span"
        self.todo_counts_xpath = '//div[@class="container"]/div/span[text()]'
        self.add_button_xpath = "/html/body/div/div/div/form/input[2]"
        self.archive_link_xpath = "/html/body/div/div/div/a"
        self.new_todo_text_initial_xpath = "/html/body/div/div/div/form/input[1]"

    def remaining(self):
        return len(filter(lambda todo: not todo[0], self.todos))

    def todo_count(self):
        return len(self.todos)

    def locate_elements(self):
        self.add_button = driver.find_element_by_xpath(self.add_button_xpath)
        self.title = driver.find_element_by_xpath(self.title_xpath)
        self.archive_link = driver.find_element_by_xpath(self.archive_link_xpath)
        self.todos = driver.find_elements_by_xpath(self.todos_xpath)
        self.todo_counts_label = driver.find_element_by_xpath(self.todo_counts_xpath)
        self.new_todo_input = driver.find_element_by_xpath(self.new_todo_text_initial_xpath)




