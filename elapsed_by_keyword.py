#!/usr/bin/env python

"""Usage: elapsed_by_keyword path/to/output.xml 

Reads result of a test run from Robot output file
and outputs "keyword elapsed_time"
sorted by the elapsed time in each keyword.
"""

import sys
import datetime
from robot.api import ExecutionResult, ResultVisitor

class ExecutionKeywordStats(ResultVisitor):

    def __init__(self):
        self.elapsed_by_kw = {}

    def end_keyword(self, keyword):
        if keyword.name in self.elapsed_by_kw:
            self.elapsed_by_kw[keyword.name] = self.elapsed_by_kw[keyword.name] + keyword.elapsedtime
        else:
            self.elapsed_by_kw[keyword.name] = keyword.elapsedtime

def stats_by_keywords(path):
    
    result = ExecutionResult(path)
    visitor = ExecutionKeywordStats()    
    result.visit(visitor)
    for kw in sorted(visitor.elapsed_by_kw, key=visitor.elapsed_by_kw.get, reverse=True):
      print kw, str(datetime.timedelta(milliseconds=visitor.elapsed_by_kw[kw]))[:-7]

if __name__ == '__main__':
    try:
        stats_by_keywords(*sys.argv[1:])
    except TypeError:
        print __doc__