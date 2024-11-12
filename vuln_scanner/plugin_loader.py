import importlib
import os

class PluginLoader:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir

    def load_plugins(self):
        plugins = []
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py"):
                plugin_name = filename[:-3]
                plugin = importlib.import_module(f"plugins.{plugin_name}")
                plugins.append(plugin)
        return plugins
