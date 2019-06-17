# *****************************************************************************
#
# Copyright (c) 2019, the Perspective Authors.
#
# This file is part of the Perspective library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

import os
import os.path
import numpy as np
import pandas as pd
from perspective.table import Perspective
from perspective.table.libbinding import t_schema


class TestSchema(object):
    def test_schema(self):
        column_names = ['Col1', 'Col2', 'Col3', 'Col4', 'Col5']
        types = [int, str, float, np.int64, np.float64]

        dtypes = []
        for name, _type in zip(column_names, types):
            dtypes.append(Perspective._type_to_dtype(_type))

        assert len(column_names) == len(dtypes)
        schema = t_schema(column_names, dtypes)
        print(schema.str())