import reflex as rx
from typing import Dict, List, TypedDict

class GeneralState (rx.State):
    active_nav: str = "Dashboard"
    mobile_sidebar_open: bool = False
    open_drawer: bool = False

    
    @rx.event
    def set_active_nav(self, nav_item: str):
        self.active_nav = nav_item
        if self.mobile_sidebar_open:
            self.mobile_sidebar_open = False

    @rx.event
    def set_drawer(self):
        if self.open_drawer:
            self.open_drawer = False
        else:
            self.open_drawer = True

    @rx.event
    def toggle_mobile_sidebar(self):
        self.mobile_sidebar_open = not self.mobile_sidebar_open
    
    @rx.var
    def nav_items(self) -> List[Dict[str, str]]:
        return [
            {
                "name": "Dashboard",
                "icon": "layout-dashboard",
            },
            {"name": "Diagnostics", "icon": "activity"},
            {"name": "Data Center", "icon": "database"},
            {
                "name": "Communications",
                "icon": "message-circle",
            },
            {"name": "Settings", "icon": "settings"},
        ]