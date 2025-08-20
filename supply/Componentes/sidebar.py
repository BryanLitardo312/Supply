import reflex as rx
from ..States.backend import GeneralState
from typing import Dict

def navigation_item(item: Dict[str, str]) -> rx.Component:
    return rx.el.button(
        rx.icon(tag=item["icon"], class_name="mr-3 size-5"),
        rx.el.span(item["name"]),
        on_click=lambda: GeneralState.set_active_nav(item["name"]),
        class_name=rx.cond(
            GeneralState.active_nav == item["name"],
            "w-full flex items-center px-4 py-3 text-sm font-medium rounded-lg bg-cyan-600/20 text-cyan-300 border border-cyan-600/30",
            "w-full flex items-center px-4 py-3 text-sm font-medium rounded-lg text-gray-400 hover:bg-gray-800 hover:text-gray-200 transition-colors duration-150",
        ),
    )

def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.image(
                    src="/primax_logo.png",
                    width="3rem",
                    height="auto",
                    #alt="Descripción de la imagen",
                ),
                rx.el.h1(
                    "Primax Ecuador",
                    class_name="text-xl font-bold text-gray-100 tracking-wider",
                ),
                rx.el.button(
                    rx.icon(tag="x", class_name="size-5"),
                    on_click=GeneralState.toggle_mobile_sidebar,
                    class_name="ml-auto md:hidden p-2 text-gray-400 hover:text-gray-200",
                ),
                class_name="flex items-center p-4 mb-6 border-b border-gray-700/50 md:border-b-0",
            ),
            rx.el.nav(
                rx.el.div(
                    rx.foreach(
                        GeneralState.nav_items,
                        navigation_item,
                    ),
                    class_name="space-y-2",
                ),
                class_name="px-4 mb-auto flex-1 overflow-y-auto",
            ),
            class_name="flex flex-col h-full",
        ),
        class_name=rx.cond(
            GeneralState.mobile_sidebar_open,
            "fixed inset-y-0 left-0 z-50 w-64 text-gray-300 flex flex-col border-r border-gray-700/50 transform transition-transform duration-300 ease-in-out md:translate-x-0 [background-color:#0D0D0D] h-screen",
            "fixed inset-y-0 left-0 z-40 w-64 text-gray-300 flex-col border-r border-gray-700/50 transform -translate-x-full transition-transform duration-300 ease-in-out md:flex md:translate-x-0 md:static md:z-auto [background-color:#0D0D0D] h-screen",
        ),
    )
