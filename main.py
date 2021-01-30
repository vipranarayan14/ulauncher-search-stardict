import logging
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
        super().__init__()

        self._load_dict()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

    def _load_dict(self):
        dict_path = self.preferences["dict_path"] or ""

        print("hellohello")

        self.dict_path = dict_path or "dict_path"
        # self.dictionary = initDictionary(dict_path)


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []

        query = event.get_argument() or ""
        # dict_path = json.dumps(extension)

        items.append(
            ExtensionResultItem(
                icon="images/icon.png",
                name="Query",
                description=f"description: {query} hi",
                on_enter=HideWindowAction(),
            )
        )

        return RenderResultListAction(items)


if __name__ == "__main__":
    SearchDictionary().run()
