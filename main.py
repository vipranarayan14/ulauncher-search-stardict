import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

# from search import initDictionary, search

logger = logging.getLogger(__name__)


class SearchDictionary(Extension):
    def __init__(self):
        super(SearchDictionary, self).__init__()

        dict_path = self.preferences["dict_path"] or ""

        self.dict_path = dict_path
        # self.dictionary = initDictionary(dict_path)

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []

        query = event.get_argument() or ""

        items.append(
            ExtensionResultItem(
                icon="images/icon.png",
                name="Query",
                description=f"description: {query} + {extension.dict_path}",
                on_enter=HideWindowAction(),
            )
        )

        return RenderResultListAction(items)


if __name__ == "__main__":
    SearchDictionary().run()
