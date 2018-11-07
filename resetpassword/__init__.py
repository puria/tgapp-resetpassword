# -*- coding: utf-8 -*-
"""The tgapp-resetpassword package"""

import tg
from tg.configuration import milestones


def plugme(app_config, options):
    try:
        app_config['_pluggable_resetpassword_config'] = options
    except TypeError:
        app_config.update_blueprint({
            '_pluggable_resetpassword_config': options
        })
    return dict(appid='resetpassword', global_helpers=False)
