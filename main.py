# Import StreamController modules
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder
from src.backend.DeckManagement.InputIdentifier import Input
from src.backend.PluginManager.ActionInputSupport import ActionInputSupport

# Import actions
from .actions.TextOutput import TextOutput

class TextOutputPlugin(PluginBase):
    def __init__(self):
        super().__init__()

        self.lm = self.locale_manager

        ## Register actions
        self.text_output_holder = ActionHolder(
            plugin_base = self,
            action_base = TextOutput,
            action_id_suffix = "TextOutput",
            action_name = self.lm.get("text-output-plugin.actions.text-output.name"),
            action_support={
                Input.Key: ActionInputSupport.SUPPORTED,
                Input.Dial: ActionInputSupport.SUPPORTED,
                Input.Touchscreen: ActionInputSupport.UNTESTED
            }
        )
        self.add_action_holder(self.text_output_holder)

        # Register plugin
        self.register(
            plugin_name = self.lm.get("text-output-plugin.plugin.name"),
            github_repo = "https://github.com/orehren/TextOutputPlugin",
            plugin_version = "1.0.0",
            app_version = "1.4.5-beta"
        )
