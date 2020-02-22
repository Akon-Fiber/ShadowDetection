# ===========================================================================
#   test.py -----------------------------------------------------------------
# ===========================================================================

#   import ------------------------------------------------------------------
# ---------------------------------------------------------------------------
import shdw.__init__
import shdw.config.settings
import shdw.utils.format

import shdw.tools.shadows

#   function ----------------------------------------------------------------
# ---------------------------------------------------------------------------
def task_default():
    task_print_user_settings()

#   function ----------------------------------------------------------------
# ---------------------------------------------------------------------------
get_value = lambda obj, key, default: obj[key] if key in obj.keys() else default

#   function ----------------------------------------------------------------
# ---------------------------------------------------------------------------
def task_new_shadow_img_freitas():
    shdw.tools.shadwos.get_shadow_freitas(
        shdw.config.settings._DATA,
        shdw.config.settings._SETTINGS["output"],
        scale=get_value(shdw.config.settings._SETTINGS,"scale", 100)
    )

#   function ----------------------------------------------------------------
# ---------------------------------------------------------------------------
def task_new_shadow_img_silva():
    shdw.tools.shadows.get_shadow_silva(
        shdw.config.settings._DATA,
        shdw.config.settings._SETTINGS["output"],
        scale=get_value(shdw.config.settings._SETTINGS,"scale", 100)
    )

#   function ----------------------------------------------------------------
# ---------------------------------------------------------------------------
def task_test_research():
    import shdw.utils.general
    research = shdw.utils.general.ReSearch(*shdw.config.settings._SETTINGS["output"]["regex"])
    print(research("G:\\Blubb\\ABC_345_RGB.tif"))

#   function ----------------------------------------------------------------
# ---------------------------------------------------------------------------
def task_print_user_settings():
    """Print the user settings"""
    
    # print user's defined settings
    shdw.__init__._logger.info("Print user's defined settings")
    shdw.utils.format.print_data(shdw.config.settings._SETTINGS)

#   function ----------------------------------------------------------------
# ---------------------------------------------------------------------------
def task_print_user_data():
    """Print the user data"""
    
    # print user's defined data
    shdw.__init__._logger.info("Print user's defined data")
    shdw.utils.format.print_data(shdw.config.settings._DATA)