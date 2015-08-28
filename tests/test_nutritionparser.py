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

first_line_data = {
    'FOOD_DES.txt': dict(
        NDB_No="01001",
        FdGrp_Cd="0100",
        Long_Desc="Butter, salted",
        Shrt_Desc="BUTTER,WITH SALT",
        ComName="",
        ManufacName="",
        Survey="Y",
        Ref_desc="",
        Refuse="0",
        SciName="",
        N_Factor="6.38",
        Pro_Factor="4.27",
        Fat_Factor="8.79",
        CHO_Factor="3.87",
    ),
    'FD_GROUP.txt': dict(
        FdGrp_Cd="0100",
        FdGrp_Desc="Dairy and Egg Products",
    ),
    'LANGUAL.txt': dict(
        NDB_No="02001",
        Factor_Code="A0113",
    ),
    'LANGDESC.txt': dict(
        Factor_Code="A0107",
        Description="BAKERY PRODUCT, UNSWEETENED (US CFR)",
    ),
    'NUT_DATA.txt': dict(
        NDB_No="01001",
        Nutr_No="203",
        Nutr_Val="0.85",
        Num_Data_Pts="16",
        Std_Error="0.074",
        Src_Cd="1",
        Deriv_Cd="",
        Ref_NDB_No="",
        Add_Nutr_Mark="",
        Num_Studies="",
        Min="",
        Max="",
        DF="",
        Low_EB="",
        Up_EB="",
        Stat_cmt="",
        AddMod_Date="11/1976",
        CC="",
    ),
    'NUTR_DEF.txt': dict(
        Nutr_No="203",
        Units="g",
        Tagname="PROCNT",
        NutrDesc="Protein",
        Num_Dec="2",
        SR_Order="600",
    ),
    'SRC_CD.txt': dict(
        Src_Cd="1",
        SrcCd_Desc="Analytical or derived from analytical",
    ),
    'DERIV_CD.txt': dict(
        Deriv_Cd="A",
        Deriv_Desc="Analytical data",
    ),
    'WEIGHT.txt': dict(
        NDB_No="01001",
        Seq="1",
        Amount="1",
        Msre_Desc="pat (1\" sq, 1/3\" high)",
        Gm_Wgt="5.0",
        Num_Data_Pts="",
        Std_Dev="",
    ),
    'FOOTNOTE.txt': dict(
        NDB_No="02009",
        Footnt_No="01",
        Footnt_Typ="D",
        Nutr_No="",
        Footnt_Txt="Mix of chili pepper, other spices and salt",
    ),
    'DATSRCLN.txt': dict(
        NDB_No="10984",
        Nutr_No="518",
        DataSrc_ID="S3941",
    ),
    'DATA_SRC.txt': dict(
        DataSrc_ID="D1066",
        Authors="G.V. Mann",
        Title="The Health and Nutritional status of Alaskan Eskimos.",
        Year="1962",
        Journal="American Journal of Clinical Nutrition",
        Vol_City="11",
        Issue_State="",
        Start_Page="31",
        End_Page="76",
    ),
}


def test_nutritionparser():
    """Test nutritionparser."""
    # Test if data has been downloaded
    assert os.path.exists("data/FOOD_DES.txt")

    for f in sr27fields.keys():
        for i, data in enumerate(reader("data/{0}".format(f))):
            if i == 0:
                if f in first_line_data:
                    assert data == first_line_data[f]
                for field in sr27fields[f]:
                    assert field in data
            assert isinstance(data, dict)
