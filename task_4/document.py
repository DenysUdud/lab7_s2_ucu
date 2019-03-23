class Document:
    """
    A class for representing document.

    ...

    Attributes
    ----------
    characters: list
       The list with characters of file.
    cursor: object
        The object of Cursor class which represents current position
        of cursor in document.
    filename: str
        The name of file.


    Methods
    -------
    insert(character)
       A method which inserts character to the document in
       current position of cursor.
       :argument character : str

    delete()
       A method which delete current char in document.

    save()
        A method which saves the document.

    string()
        Returns the document in string format.
        :returns str

    """
    def __init__(self):
        """
        A method for initialisation Document object.
        """
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        """
        A method which inserts character to the document in
        current position of cursor.

        Preconditions: if add several symbols <AssertionError> raises
                       if cursor is outside of the document insertion
                       makes on the beginning or end of the document.
                       (if behind start - in the beginning, if out of
                       end - in the end)
        :param character: str
        :return: None
        """
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        """
        A method which delete current char in document.

        Precondition: If delete element which does not exist
                      <IndexError> raises
        :return: None
        """
        del self.characters[self.cursor.position]

    def save(self):
        """
        A method saves the document.

        Precondition: if filename is not defined
                      <FileNotFoundError> raises.
        :return: None
        """
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

    # using property to have access to this method by printing string
    @property
    def string(self):
        """
        Returns the document in string format.
        :return: str
        """
        return "".join((str(c) for c in self.characters))


class Cursor:
    """
    A method for representing cursor in document.

    ...

    Attributes
    ----------
    document: object of Document class
        The document.
    position : int
        The current position of cursor in file.

    Methods
    -------
    forward()
        Method moves cursor forward by adding to position one.
    back()
        Method moves cursor back by subtracting from position one.
    home()
        Moves cursor to the beginning of page.
    end()
        Moves cursor to the end of page.
    """
    def __init__(self, document):
        """
        A method for initialization cursor.
        :param document: object of Document class.
        """
        self.document = document
        self.position = 0

    def forward(self):
        """
        Method moves cursor forward by adding to position one.
        """
        self.position += 1

    def back(self):
        """
        Method moves cursor back by subtracting from position one.
        """
        self.position -= 1

    def home(self):
        """
        Moves cursor to the beginning of page.
        """
        while self.document.characters[
            self.position - 1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        """
        Moves cursor to the end of page.
        """
        while self.position < len(
                self.document.characters) and \
                self.document.characters[
                    self.position
                ].character != '\n':
            self.position += 1


class Character:
    """
    A class for representing character.

    Attributes
    ----------
    character: str
        The char from document. Len of this char must be 1.
    bold : bool
        The identifier whether char is bold.
    italic: bool
        The identifier whether char is italic.
    underline: bool
        The identifier whether char is underline.

    Methods
    -------
    __str__()
        Represents char in str format.
    """
    def __init__(self, character,
                 bold=False, italic=False, underline=False):
        """
        A method for initialization Character object.
        :param character: str
        :param bold: bool
        :param italic: bool
        :param underline: bool
        """
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """
        Return char in str format.
        :returns str
        """
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character


if __name__ == "__main__":
    d = Document()
    d.insert('h')
    d.insert('e')
    d.insert(Character('l', bold=True))
    d.insert(Character('l', bold=True))
    d.insert('o')
    d.insert('\n')
    d.insert(Character('w', italic=True))
    d.insert(Character('o', italic=True))
    d.insert(Character('r', underline=True))
    d.insert('l')
    d.insert('d')
    print(d.string)
    d.cursor.home()
    d.delete()
    d.insert('W')
    print(d.string)
    d.characters[0].underline = True
    print(d.string)
