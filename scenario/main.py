from typing import Dict, List, Tuple, Any
import re

global LANG
LANG = "EN" # Default is EN - English, but it can be overwritten to DE - German

from df_engine.core import Actor, Context
from df_engine.core.keywords import TRANSITIONS, RESPONSE, PROCESSING
import df_engine.conditions as cnd
import df_engine.labels as lbl
from .response import * # Import all custom reponse functions


plot = {
    "global":{
        "start":{
        RESPONSE:"",
        TRANSITIONS: {
                "node1":cnd.true() # Always true, starting point
            },
        },
        "node1":{
        RESPONSE:bot_introduction,
        TRANSITIONS: {
                ("global", "node1"): cnd.regexp(r"start", re.IGNORECASE),
                lbl.repeat():check_language, # Always repeat response, when language change trigger words are used
                ("check_balance","node_1"): transition_check_balance_flow,
                lbl.forward():cnd.true() # If nothing matches go into next node and loop, until something matches or back to start

            },
        },
        "node1_loop":{
        RESPONSE:bot_introduction_loop,
        TRANSITIONS: {
                ("global", "node1"): cnd.regexp(r"start", re.IGNORECASE),
                lbl.repeat():check_language, # Always repeat response, when language change trigger words are used
                ("check_balance","node_1"): transition_check_balance_flow,
                lbl.repeat():cnd.true() # If nothing matches loop, until something matches
            },
        },




        "fallback": {  # We get to this node if an error occurred while the agent was running
            RESPONSE: "Ooops",
            TRANSITIONS: {
                ("global", "start"): cnd.regexp(r"hi|hello", re.IGNORECASE),
                lbl.previous(): cnd.regexp(r"previous", re.IGNORECASE),
                lbl.repeat(): cnd.true(), # If no match, repeast
            },
        }     
    },

    "shares_flow":{



    },
    "leasing_flow":{



    },
    "check_balance":{
        "node_1":{
            RESPONSE:check_balance_node1_response,
            TRANSITIONS:{
                ("global", "node1"): cnd.regexp(r"start", re.IGNORECASE),
                lbl.repeat():check_language, # Always repeat response, when language change trigger words are used

                lbl.forward():cnd.true() # If nothing matches go into next node and loop, until something matches or back to start
            }
        },
        "node1_loop":{
        RESPONSE:bot_introduction_loop,
        TRANSITIONS: {
                ("global", "node1"): cnd.regexp(r"start", re.IGNORECASE),
                lbl.repeat():check_language, # Always repeat response, when language change trigger words are used
                lbl.repeat():cnd.true() # If nothing matches loop, until something matches
            }
        }
    },
    "deposit_money_flow":{


    },
    "transfer_money_flow":{


    },
    "chitchat_creator_flow":{


    }


}

actor = Actor(plot, start_label=("global", "start"), fallback_label=("global", "fallback"))
