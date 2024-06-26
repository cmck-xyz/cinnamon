#!/usr/bin/python3

from SettingsWidgets import SidePage
from xapp.GSettingsWidgets import *


class Module:
    name = "workspaces"
    category = "prefs"
    comment = _("Manage workspace preferences")

    def __init__(self, content_box):
        keywords = _("workspace, osd, expo, monitor")
        sidePage = SidePage(_("Workspaces"), "cs-workspaces", keywords, content_box, module=self)
        self.sidePage = sidePage

    def shouldLoad(self):
        return True

    def on_module_selected(self):
        if not self.loaded:
            print("Loading Workspaces module")

            page = SettingsPage()
            self.sidePage.add_widget(page)

            settings = page.add_section(_("Workspace Options"))

            switch = GSettingsSwitch(_("Enable workspace OSD"), "org.cinnamon", "workspace-osd-visible")
            settings.add_row(switch)

            slider = GSettingsRange(_("Workspace OSD duration"), "org.cinnamon", "workspace-osd-timeout", _("Shorter"), _("Longer"), mini=0.2, maxi=1.0, step=0.2, show_value=True)
            slider.content_widget.set_has_origin(False)
            slider.content_widget.add_mark(0.4, Gtk.PositionType.TOP, None)
            slider.content_widget.add_mark(0.6, Gtk.PositionType.TOP, None)
            slider.content_widget.add_mark(0.8, Gtk.PositionType.TOP, None)

            settings.add_reveal_row(slider, "org.cinnamon", "workspace-osd-visible")

            switch = GSettingsSwitch(_("Allow cycling through workspaces"), "org.cinnamon.muffin", "workspace-cycle")
            settings.add_row(switch)

            switch = GSettingsSwitch(_("Only use workspaces on primary monitor (requires Cinnamon restart)"), "org.cinnamon.muffin", "workspaces-only-on-primary")
            settings.add_row(switch)

            switch = GSettingsSwitch(_("Display Expo view as a grid"), "org.cinnamon", "workspace-expo-view-as-grid")
            settings.add_row(switch)

            # Edge Flip doesn't work well, so it's there in gsettings, but we don't show it to users yet
            # switch = GSettingsSwitch(_("Enable Edge Flip"), "org.cinnamon", "enable-edge-flip")
            # settings.add_row(switch)
            # spin = GSettingsSpinButton(_("Edge Flip delay"), "org.cinnamon", "edge-flip-delay", mini=1, maxi=3000, units=_("ms"))
            # settings.add_reveal_row(spin, "org.cinnamon", "enable-edge-flip")

            # switch = GSettingsSwitch(_("Invert the left and right arrow key directions used to shift workspaces during a window drag"), "org.cinnamon.muffin", "invert-workspace-flip-direction")
            # settings.add_row(switch)
