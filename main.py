import logging
import os

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

from search import initDictionary, search

logger = logging.getLogger(__name__)


class SearchDictionary(Extension):
    def __init__(self):
        super(SearchDictionary, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []

        query = event.get_argument() or ""
        dict_path = extension.preferences["dict_path"] or ""

        if not dict_path:
            items.append(
                ExtensionResultItem(
                    icon="images/icon.png",
                    name="Dictionary path not configured!",
                    description="Configure path to the dictionary file in\n"
                                "Ulauncher > Extensions > StarDict Lookup > Dictionary path",
                    on_enter=HideWindowAction(),
                )
            )

            return RenderResultListAction(items)

        if not os.path.exists(f'{dict_path}.dict'):
            items.append(
                ExtensionResultItem(
                    icon="images/icon.png",
                    name="Invalid dictionary file!",
                    description="Either the configured dictionary path is invalid\n"
                                "or the path does not contain StarDict files.",
                    on_enter=HideWindowAction(),
                )
            )

            return RenderResultListAction(items)

        items.append(
            ExtensionResultItem(
                icon="images/icon.png",
                name="Query",
                description=f"description: {query} + {dict_path} hi",
                on_enter=HideWindowAction(),
            )
        )

        return RenderResultListAction(items)


if __name__ == "__main__":
    SearchDictionary().run()
