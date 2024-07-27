import flet as ft


from page.overview import Overview

class CustomNavigationRailDestination(ft.UserControl):
    def __init__(self, label):
        super().__init__()
        self.label = label

    def build(self):
        return ft.NavigationRailDestination(
            label_content=ft.Text(self.label),
            padding=ft.Padding(16, 8, 0, 0),
        )

def main(page: ft.Page):

    overview_page = Overview(page)
    
    def button_clicked(e):
        print("clicked")
        page.update()

    Left_Navigation = ft.Column(
        [
            ft.TextButton("Button with 'click' event", on_click=button_clicked, data=0),
            ft.Text("setting"),
        ],
        width=200,
    )

    Left_content = ft.Container(
        content=Left_Navigation,
    )

    Main_content = ft.Container(
        content=overview_page,
        bgcolor=ft.colors.GREY_100,
        expand=True
    )


    view = ft.Column([
        ft.Row([
            Left_content,
            ft.VerticalDivider(width=1),
            Main_content,
        ], expand=True)
    ], expand=True)

    page.add(
        view
    )
    page.update()

ft.app(target=main)