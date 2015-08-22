# -*- coding: utf-8 -*-
#
# This file is part of Nutrition Parser
# Copyright (C) 2015 Lars Holm Nielsen.
#
# Nutrition Parser is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.


"""Tests for `nutritionparser` module."""

import os

from nutritionparser import reader, sr27fields


def test_nutritionparser():
    """Test nutritionparser."""
    # Test if data has been downloaded
    assert os.path.exists("data/FOOD_DES.txt")

    for f in sr27fields.keys():
        for i, data in enumerate(reader("data/{0}".format(f))):
            if i == 0:
                for field in sr27fields[f]:
                    assert field in data
            assert isinstance(data, dict)
