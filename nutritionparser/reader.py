# -*- coding: utf-8 -*-
#
# This file is part of Nutrition Parser
# Copyright (C) 2015 Lars Holm Nielsen.
#
# Nutrition Parser is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""nutritionparser module."""

from __future__ import absolute_import, unicode_literals, print_function

import csv
import io
import sys
from os.path import basename


PY2 = sys.version_info[0] == 2

delimiter = '~'.encode('ascii') if PY2 else "^"
quotechar = '~'.encode('ascii') if PY2 else '~'


def utf8_encoder(csv_data):
    """Encode Unicode to UTF8.

    Ensures that Python 2 CSV module can handle the data.
    """
    for line in csv_data:
        yield line.encode('utf-8') if PY2 else line


def reader(filepath, fields=None):
    """Read CSV files from USDA National Nutrient Database.

    :param filepath: Path to a USDA data file.
    :param fields: Fields in data file. Default: ``None`` (i.e use SR27 field
        names).
    """
    filename = basename(filepath)

    if fields is None:
        fields = sr27fields

    fieldnames = fields[filename]

    with io.open(filepath, newline='\r\n', encoding='iso-8859-1') as f:
        reader = csv.DictReader(
            utf8_encoder(f),
            fieldnames=fieldnames,
            delimiter=delimiter,
            quotechar=quotechar
        )
        for row in reader:
            yield row


sr27fields = {
    'FOOD_DES.txt': [
        'NDB_No',
        'FdGrp_Cd',
        'Long_Desc',
        'Shrt_Desc',
        'ComName',
        'ManufacName',
        'Survey',
        'Ref_desc',
        'Refuse',
        'SciName',
        'N_Factor',
        'Pro_Factor',
        'Fat_Factor',
        'CHO_Factor',
        'FdGrp_Cd',
        'FdGrp_Desc',
    ],
    'FD_GROUP.txt': [
        'FdGrp_Cd',
        'FdGrp_Desc',
    ],
    'LANGUAL.txt': [
        'NDB_No',
        'Factor_Code',
    ],
    'LANGDESC.txt': [
        'Factor_Code',
        'Description',
    ],
    'NUT_DATA.txt': [
        'NDB_No',
        'Nutr_No',
        'Nutr_Val',
        'Num_Data_Pts',
        'Std_Error',
        'Src_Cd',
        'Deriv_Cd',
        'Ref_NDB_No',
        'Add_Nutr_Mark',
        'Num_Studies',
        'Min',
        'Max',
        'DF',
        'Low_EB',
        'Up_EB',
        'Stat_cmt',
        'AddMod_Date',
        'CC',
    ],
    'NUTR_DEF.txt': [
        'Nutr_No',
        'Units',
        'Tagname',
        'NutrDesc',
        'Num_Dec',
        'SR_Order',
    ],
    'SRC_CD.txt': [
        'Src_Cd',
        'SrcCd_Desc',
    ],
    'DERIV_CD.txt': [
        'Deriv_Cd',
        'Deriv_Desc',
    ],
    'WEIGHT.txt': [
        'NDB_No',
        'Seq',
        'Amount',
        'Msre_Desc',
        'Gm_Wgt',
        'Num_Data_Pts',
        'Std_Dev',
    ],
    'FOOTNOTE.txt': [
        'NDB_No',
        'Footnt_No',
        'Footnt_Typ',
        'Nutr_No',
        'Footnt_Txt',
    ],
    'DATSRCLN.txt': [
        'NDB_No',
        'Nutr_No',
        'DataSrc_ID',
    ],
    'DATA_SRC.txt': [
        'DataSrc_ID',
        'Authors',
        'Title',
        'Year',
        'Journal',
        'Vol_City',
        'Issue_State',
        'Start_Page',
        'End_Page',
    ],
}
"""SR27 field names."""
