from nautobot.extras.plugins import PluginConfig

class ComponentsPlugin(PluginConfig):
    name = 'nautobot_plugin'
    verbose_name = 'Components'
    description = 'Track smaller components'
    author = 'jawny'
    base_url = 'components'
    required_settings = []
    default_settings = {}
    version = '0.1'
    min_version = '1.1.0'
    max_version = '1.9999'
    caching_config = {}

config = ComponentsPlugin
