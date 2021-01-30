import json
import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)


class SearchDictionary(Extension):
    def __init__(self):
        super(SearchDictionary, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        items.append(
            ExtensionResultItem(
                icon="images/icon.png",
                name="name",
                description="description",
                on_enter=HideWindowAction(),
            )
        )

        return RenderResultListAction(items)


if __name__ == "__main__":
    SearchDictionary().run()
