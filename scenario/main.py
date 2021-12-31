from typing import Dict, List, Tuple, Any
import re

from df_engine.core import Actor, Context
from df_engine.core.keywords import TRANSITIONS, RESPONSE, PROCESSING, MISC
import df_engine.conditions as cnd
import df_engine.labels as lbl

import scenario.condition as loc_cnd # Import all custom condition functions
import scenario.response as loc_rsp # Import all custom reponse functions

ctx = Context()
ctx.misc["language"] = "EN"

plot = {
    "global":{
        "start":{
        RESPONSE:loc_rsp.bot_introduction,
        TRANSITIONS: {
                lbl.forward():cnd.true() # Automatic forward to first step
            },
        },
        "bot_introduction":{
        RESPONSE:loc_rsp.bot_introduction,
        TRANSITIONS: {
                ("check_accounts","check_banks"): loc_cnd.check_banks,
                lbl.repeat():cnd.true() # If nothing matches go loop until something matches, additionally a special loop message will be displayed
            },
        },
        "fallback": {  # We get to this node if an error occurred while the agent was running
            RESPONSE: "Ooops - something went wrong, either you type 'start' to go back to start node or \n\
            you press 'pevious' to go back to the previous point.' Anyway, I am very sorry.",
            TRANSITIONS: {
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                lbl.previous(): cnd.regexp(r"previous", re.IGNORECASE),
                lbl.repeat(): cnd.true(), # If no match, repeast
            },
        }     
    },
    "check_accounts":{
        "check_banks":{
            RESPONSE:loc_rsp.check_banks,
            TRANSITIONS:{
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                ("check_accounts","check_balance"): loc_cnd.check_balance,


                lbl.repeat():cnd.true() # If nothing matches go loop until something matches, additionally a special loop message will be displayed
            }
        },
        "check_balance":{
        RESPONSE:loc_rsp.check_banks,
        TRANSITIONS: {
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),

                lbl.repeat():cnd.true() # If nothing matches loop, until something matches
            }
        },
        "transfer_money":{
        RESPONSE:loc_rsp.check_banks,
        TRANSITIONS: {
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),

                lbl.repeat():cnd.true() # If nothing matches loop, until something matches
            }
        },
        "deposit_money":{
        RESPONSE:loc_rsp.check_banks,
        TRANSITIONS: {
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),

                lbl.repeat():cnd.true() # If nothing matches loop, until something matches
            }
        },
        "withdraw_money":{
        RESPONSE:loc_rsp.check_banks,
        TRANSITIONS: {
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),

                lbl.repeat():cnd.true() # If nothing matches loop, until something matches
            }
        },
    },
    "get_shares":{



    },
    "chat_financial_topics":{


    },

    "chat_creator_flow":{


    }

}

actor = Actor(plot, start_label=("global", "start"), fallback_label=("global", "fallback"))
