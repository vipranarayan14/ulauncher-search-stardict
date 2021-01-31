import logging
import os

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

from search import initDictionary, search, WordNotInDictionary

logger = logging.getLogger(__name__)


def message(name, description):
    return RenderResultListAction([
        ExtensionResultItem(
            name,
            description,
            icon="images/icon.png",
        )
    ])


message_dictionary_path_not_configured = message(
    name="Dictionary path not configured!",
    description="Configure path to the dictionary file in\n"
                "Ulauncher > Extensions > StarDict Lookup > Dictionary path"
)

message_invalid_dictionary_file = message(
    name="Invalid dictionary file!",
    description="Either the configured dictionary path is invalid\n"
                "or the path does not contain StarDict files.",
)


class SearchDictionary(Extension):
    def __init__(self):
        super(SearchDictionary, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):

        dict_path = extension.preferences["dict_path"] or ""

        if not dict_path:
            return message(
                name="Dictionary path not configured!",
                description="Configure path to the dictionary file in\n"
                            "Ulauncher > Extensions > StarDict Lookup > Dictionary path"
            )

        dict_file_path = f'{dict_path}.dict'

        if not os.path.exists(dict_file_path):
            return message_invalid_dictionary_file

        query = event.get_argument() or ""

        if not query:
            return message(
                name="Type a word to lookup",
                description=f"Dictionary: {dict_path}"
            )

        dictionary = initDictionary(dict_path)

        try:
            result = f"{search(dictionary, query)}\n\n"
        except WordNotInDictionary:
            result = 'Word not found in dictionary'

        items = [ExtensionResultItem(
            icon="images/icon.png",
            name=query,
            description=result,
            on_enter=HideWindowAction(),
        )]

        return RenderResultListAction(items)


if __name__ == "__main__":
    SearchDictionary().run()
