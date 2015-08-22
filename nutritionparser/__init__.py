# -*- coding: utf-8 -*-
#
# This file is part of Nutrition Parser
# Copyright (C) 2015 Lars Holm Nielsen.
#
# Nutrition Parser is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

r"""Nutrition Parser parses USDA National Nutrient Database files.

Getting the data
----------------
First, download the actual data from USDA's website at
http://www.ars.usda.gov/Services/docs.htm?docid=24912 (currently only release
SR27 is supported). Download the ASCII version.

.. code-block:: console

    $ mkdir data
    $ cd data
    $ wget https://www.ars.usda.gov/SP2UserFiles/Place/12354500/Data/\\
    > SR27/dnload/sr27asc.zip
    $ unzip sr27asc.zip
    $ ls -1
    DATA_SRC.txt
    DATSRCLN.txt
    DERIV_CD.txt
    FD_GROUP.txt
    FOOD_DES.txt
    FOOTNOTE.txt
    LANGDESC.txt
    LANGUAL.txt
    NUTR_DEF.txt
    NUT_DATA.txt
    SRC_CD.txt
    WEIGHT.txt
    sr27_doc.pdf
    sr27asc.zip

The ``.txt`` files are actually CSV files with special quote and delimiter
characters. The included PDF file contains full documentation of all fields
in the CSV files.

Parsing the data
----------------
Parsing a data file is easy, just import the ``reader`` and point it to the
data file you want to parse:

    >>> from nutritionparser import reader
    >>> for l in reader('data/FD_GROUP.txt'):
    ...     print(l['FdGrp_Desc'])
    Dairy and Egg Products
    Spices and Herbs
    Baby Foods
    Fats and Oils
    Poultry Products
    Soups, Sauces, and Gravies
    Sausages and Luncheon Meats
    Breakfast Cereals
    Fruits and Fruit Juices
    Pork Products
    Vegetables and Vegetable Products
    Nut and Seed Products
    Beef Products
    Beverages
    Finfish and Shellfish Products
    Legumes and Legume Products
    Lamb, Veal, and Game Products
    Baked Products
    Sweets
    Cereal Grains and Pasta
    Fast Foods
    Meals, Entrees, and Side Dishes
    Snacks
    American Indian/Alaska Native Foods
    Restaurant Foods

You can also inspect the fields available for each file:

    >>> from nutritionparser import sr27fields
    >>> for f in sr27fields['FOOD_DES.txt']:
    ...     print(f)
    NDB_No
    FdGrp_Cd
    ...
    FdGrp_Desc

Full documentation for each fields is available in the included POF file of the
data.
"""

from __future__ import absolute_import, unicode_literals, print_function

from .reader import reader, sr27fields
from .version import __version__

__all__ = ('__version__', 'reader', 'sr27fields')
