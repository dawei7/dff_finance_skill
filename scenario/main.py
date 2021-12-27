from typing import Dict, List, Tuple, Any
import re

from df_engine.core import Actor, Context
from df_engine.core.keywords import TRANSITIONS, RESPONSE, PROCESSING
import df_engine.conditions as cnd
import df_engine.labels as lbl

import scenario.condition as loc_cnd # Import all custom condition functions
import scenario.response as loc_rsp # Import all custom reponse functions

ctx = Context()
ctx.misc["language"] = "EN"

plot = {
    "global":{
        "start":{
        RESPONSE:"",
        TRANSITIONS: {
                lbl.forward():loc_rsp.param_setter # Always true, starting point
            },
        },
        "node1":{
        RESPONSE:loc_rsp.bot_introduction,
        TRANSITIONS: {
                ("global", "node1"): cnd.regexp(r"start", re.IGNORECASE),
                lbl.repeat():loc_rsp.check_language, # Always repeat response, when language change trigger words are used
                ("check_balance","node_1"): loc_rsp.transition_check_balance_flow,
                lbl.forward():cnd.true() # If nothing matches go into next node and loop, until something matches or back to start

            },
        },
        "node1_loop":{
        RESPONSE:loc_rsp.bot_introduction_loop,
        TRANSITIONS: {
                ("global", "node1"): cnd.regexp(r"start", re.IGNORECASE),
                lbl.repeat():loc_rsp.check_language, # Always repeat response, when language change trigger words are used
                ("check_balance","node_1"): loc_rsp.transition_check_balance_flow,
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
            RESPONSE:loc_rsp.check_balance_node1_response,
            TRANSITIONS:{
                ("global", "node1"): cnd.regexp(r"start", re.IGNORECASE),
                lbl.repeat():loc_rsp.check_language, # Always repeat response, when language change trigger words are used

                lbl.forward():cnd.true() # If nothing matches go into next node and loop, until something matches or back to start
            }
        },
        "node1_loop":{
        RESPONSE:loc_rsp.bot_introduction_loop,
        TRANSITIONS: {
                ("global", "node1"): cnd.regexp(r"start", re.IGNORECASE),
                lbl.repeat():loc_rsp.check_language, # Always repeat response, when language change trigger words are used
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
