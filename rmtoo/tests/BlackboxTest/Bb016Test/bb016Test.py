'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Blackbox rmtoo test
   
 (c) 2011-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os

from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, compare_results, \
    cleanup_std_log, delete_result_is_dir, extract_container_files, \
    check_file_results

mdir = "tests/BlackboxTest/Bb016Test"

class TestBB16:

    def test_pos_001(self):
        "Blackbox test for simple constraint handling"

        def myexit(n):
            pass

        os.environ["basedir"] = mdir
        mout, merr = prepare_result_is_dir()
        main(["-j", "file://" + mdir + "/input/Config.json"], mout, merr,
             exitfun=myexit)
        cleanup_std_log(mout, merr)
#        extract_container_files(["reqspricing.ods",])
        check_file_results(mdir)
        delete_result_is_dir()

if __name__ == "__main__":
    t = TestBB16()
    t.test_pos_001()
