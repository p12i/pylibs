#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colors import uncolored
from colors import colored


def tablePrinter(table, **kwargs):
    """
    tablePrinter(table, **kwargs) -> string
       Zwraca string zawierajacy tabele na podstawie rekordow zapisanych
       w tabeli tabel. Przyklad:
+=====================+==========+=======+=========+=======+=======+========+
|      Timestamp      | Function | Count |   Sum   |  Min  |  Ave  |  Max   |
+=====================+==========+=======+=========+=======+=======+========+
| 2013-03-29 00:01:00 |      msg |     3 |  20.706 | 0.521 | 6.902 | 18.788 |
| 2013-03-29 00:02:00 |      msg |     2 |   0.693 | 0.122 | 0.346 |  0.571 |
| 2013-03-29 06:51:00 |      msg |     3 |   0.252 | 0.080 | 0.084 |  0.088 |
+=====================+==========+=======+=========+=======+=======+========+
   parametry:
      table : table - Tabela zawierajaca dane, przyklad danych
         ``tab = [[ 'naglowek1' '', '' ], [ 0, 1, 2 ], [3, 4, 5], [6, 7, 8]] ``
                      pierwszy wiersz zawiera naglowki - kazda kolumna musi
                      miec naglowek w przypadku roznych dlugosci wierszy,
                      kolumny uzupelniane sa od lewej strony poszczegolne
                      komorki musza dac sie dac sie konwertowac na obiekt typu
                      string (str())
   parametry nazwane:
       align : string [left|center|right] - wyrownywanie wewnatrz komorki
               do lewej lub prawej strony, domyslnie do lewej
       separator : string - jednoznakowy separator kolumn, domyslnie |
       colors : bool - czy wewnatrz tabeli znajduja sie kolorwe znaki,
                domyslnie False
    """
    align = kwargs.get('align', 'left')
    separator = kwargs.get('separator', '|')
    colors = kwargs.get('colors', False)

    def breakLine(sizes):
        """
        breakLine(sizes): -> string
           Tworzy linie przerwy zlozona ze znakow "="
           W miejsca separatorow kolumn wstawia znak "+"
        parametry:
           sizes : tablica - tablica wartosci int zawierajacych rozmiar
                   poszczegolnych kolumn
        """

        output = ''
        for i in sizes:
            output += '+' + ('=' * (i + 2))  # +2 za spacje na poczatku i koñcu
        return output + "+\n"

    columns = len(table[0])
    columns_size = [0 for i in xrange(columns)]

    for row in table:
        for i in xrange(len(row)):
            if colors:
                columns_size[i] = max(len(uncolored(str(row[i]))),
                                      columns_size[i])
            else:
                columns_size[i] = max(len(str(row[i])),
                                      columns_size[i])

    bl = breakLine(columns_size)
    output = bl

    for i in xrange(len(table[0])):
        output += separator + ' '
        if colors:
            cell_fix = len(table[0][i]) - len(uncolored(table[0][i]))
            output += table[0][i].center(columns_size[i] + cell_fix) + ' '
        else:
            output += table[0][i].center(columns_size[i]) + ' '

    output += separator + "\n" + bl

    for row in table[1:]:
        rowColumns = len(row)
        for i in xrange(len(row)):
            cell_size = columns_size[i]
            if colors:
                cell_size += len(str(row[i])) - len(uncolored(str(row[i])))

            if align == 'left':
                msg = str(row[i]).ljust(cell_size)
            elif align == 'center':
                msg = str(row[i]).center(cell_size)
            else:
                msg = str(row[i]).rjust(cell_size)
            output += "%s %s " % (separator, msg)

        for i in xrange(rowColumns, columns):
            output += separator + ' ' * (columns_size[i] + 2)

        output += separator + '\n'

    output += bl

    return output

if __name__ == "__main__":
    tab = [[colored('Kolumna 1', 'yellow'), colored('Kolumna 2', 'blue'),
            colored('Kolumna 3', 'green')],
           [1, 2],
           [3, 4, 5],
           ['a', 'vvv', 'avava']]
    print tablePrinter(tab, colors=True, align="right")
