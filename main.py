import logging
import os

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

from Dictionary import Dictionary

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
    description="Configure path to the dictionary file in:\n"
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
            return message_dictionary_path_not_configured

        dict_file_path = f'{dict_path}.dict'

        if not os.path.exists(dict_file_path):
            return message_invalid_dictionary_file

        query = event.get_argument() or ""

        if not query:
            return message(
                name="Type a word to lookup",
                description=f"Dictionary: {dict_path}"
            )

        dictionary = Dictionary(dict_path)

        try:
            result = dictionary.lookup(query)
            desc = f"{result}\n\n"
        except dictionary.WordNotFound:
            desc = 'Word not found in dictionary.'

        return RenderResultListAction(ExtensionResultItem(
            icon="images/icon.png",
            name=query,
            description=desc,
            on_enter=HideWindowAction()
        ))


if __name__ == "__main__":
    SearchDictionary().run()
