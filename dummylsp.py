"""Language server for dummy lsp mode."""

import logging
from pygls.server import LanguageServer
from lsprotocol import types as lsp
import re

logging.basicConfig(filename='pygls.log', filemode='w', level=logging.DEBUG)


class DummyLSPLanguageServer(LanguageServer):
    """DummyLSP Language Server API."""

    def __init__(self, *args):
        """Construct."""
        super().__init__(*args)


dummy_server = DummyLSPLanguageServer('dummy-server', 'v0.1')


@dummy_server.feature(
    lsp.TEXT_DOCUMENT_SEMANTIC_TOKENS_FULL,
    lsp.SemanticTokensLegend(token_types=["comment"], token_modifiers=[]),
)
def semantic_tokens(ls: DummyLSPLanguageServer, params: lsp.SemanticTokensParams):
    """
    Semantic token parser.

    See [[https://microsoft.github.io/language-server-protocol/specification#textDocument_semanticTokens]]
    for details on how semantic tokens are encoded.
    """

    TOKENS=re.compile(r'/.*(\n|$)')
    
    uri = params.text_document.uri
    doc = ls.workspace.get_document(uri)

    last_line = 0
    last_start = 0

    data = []

    for lineno, line in enumerate(doc.lines):
        last_start = 0

        for match in TOKENS.finditer(line):
            start, end = match.span()
            data += [(lineno - last_line), (start - last_start), (end - start), 0, 0]

            last_line = lineno
            last_start = start

    return lsp.SemanticTokens(data=data)


def main():
    """Entry point."""
    dummy_server.start_io()


if __name__ == '__main__':
    main()
