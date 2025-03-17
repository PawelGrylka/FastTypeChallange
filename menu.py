class Menu:
    def __init__(self, language_selected, languages):
        self.language_selected = language_selected
        self.menu_elements = languages.get(language_selected, {})

    def show_menu(self):
        print(f"1. {self.menu_elements.get('firstElementMenu', 'N/A')}")
        print(f"2. {self.menu_elements.get('secondElementMenu', 'N/A')}")
        print(f"3. {self.menu_elements.get('thirdElementMenu', 'N/A')}")
        print(f"4. {self.menu_elements.get('fourthElementMenu', 'N/A')}")
