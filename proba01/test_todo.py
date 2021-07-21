from todo_page import TodoPage


def test_initial_data_on_screen():
    todo_page = TodoPage()
    todo_page.locate_elements()

    assert todo_page.new_todo_input.text == todo_page.new_todo_text_initial_value
    for index, todo in enumerate(todo_page.todos_initial_value):
        assert todo_page.todos[index].text == todo[1]
        assert todo_page.todos[index].get_attribute("class") == todo[0]