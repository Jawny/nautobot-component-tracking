
from nautobot.extras.plugins import PluginMenuButton, PluginMenuItem
from nautobot.utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link='plugins:nautobot_plugin:components',
        link_text='Components',
        buttons=(
            PluginMenuButton('home', 'Button A', 'mdi mdi-help-circle', ButtonColorChoices.BLUE),
            PluginMenuButton('home', 'Button B', 'mdi mdi-alert', ButtonColorChoices.GREEN),
        )
    ),
)
