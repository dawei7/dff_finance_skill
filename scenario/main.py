from typing import Dict, List, Tuple, Any
import re

from df_engine.core import Actor, Context
from df_engine.core.keywords import TRANSITIONS, RESPONSE, PROCESSING, MISC
import df_engine.conditions as cnd
import df_engine.labels as lbl

import scenario.condition as loc_cnd # Import all custom condition functions
import scenario.response as loc_rsp # Import all custom reponse functions


plot = {
    "global":{
        "start":{
        RESPONSE:loc_rsp.bot_introduction,
        TRANSITIONS: {
                ("check_accounts","check_banks"): loc_cnd.check_banks,
                ("get_ticker","overview_ticker"): cnd.regexp(r"share", re.IGNORECASE),
                ("ask_the_bot_creator","QA_start_ask_the_bot_creator"): cnd.regexp(r"bot", re.IGNORECASE),
                lbl.forward():cnd.true() # Automatic forward to first step
            },
        },
        "bot_introduction":{
        RESPONSE:loc_rsp.bot_introduction,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("check_accounts","check_banks"): loc_cnd.check_banks,
                ("get_ticker","overview_ticker"): cnd.regexp(r"share", re.IGNORECASE),
                ("ask_the_bot_creator","QA_start_ask_the_bot_creator"): cnd.regexp(r"bot", re.IGNORECASE),
                lbl.repeat():cnd.true() # If nothing matches go loop until something matches, additionally a special loop message will be displayed
            },
        },
        "fallback": {  # We get to this node if an error occurred while the agent was running
            RESPONSE: "Ooops - something went wrong, either you type 'start' to go back to start node or \n\
            you press 'pevious' to go back to the previous point.' Anyway, I am very sorry.",
            TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
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
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                ("check_accounts","check_balances"): loc_cnd.check_balances,
                ("check_accounts","transfer_money"): loc_cnd.tranfer_money,
                ("check_accounts","deposit_money"): loc_cnd.deposit_money,
                ("check_accounts","withdraw_money"): loc_cnd.withdraw_money,
                ("check_accounts","check_banks"): loc_cnd.check_banks,
                lbl.repeat():cnd.true() # If nothing matches go loop until something matches, additionally a special loop message will be displayed
            }
        },
        "check_balances":{
        RESPONSE:loc_rsp.check_balances,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                ("check_accounts", "check_banks"): cnd.regexp(r"back", re.IGNORECASE),
                ("check_accounts","check_balances"): loc_cnd.check_balances,
                ("check_accounts","transfer_money"): loc_cnd.tranfer_money,
                ("check_accounts","deposit_money"): loc_cnd.deposit_money,
                ("check_accounts","withdraw_money"): loc_cnd.withdraw_money,
                ("check_accounts","check_banks"): loc_cnd.check_banks,
                lbl.repeat():cnd.true() # If nothing matches go loop until something matches, additionally a special loop message will be displayed
            }
        },
        "transfer_money":{
        RESPONSE:loc_rsp.transfer_money,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                ("check_accounts", "check_banks"): cnd.regexp(r"back", re.IGNORECASE),
                ("check_accounts","transfer_money_confirm"): cnd.true(), # In any case forward to get confirmation or rejection message
            }
        },
        "transfer_money_confirm":{
        RESPONSE:loc_rsp.transfer_money_confirm,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                ("check_accounts", "check_banks"): cnd.true() # In any case go back to start of check accounts
            }
        },
        "deposit_money":{
        RESPONSE:loc_rsp.deposit_money,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                ("check_accounts", "check_banks"): cnd.regexp(r"back", re.IGNORECASE),
                ("check_accounts", "deposit_money_confirm"): cnd.true(), # In any case forward to get confirmation or rejection message
            }
        },
        "deposit_money_confirm":{
        RESPONSE:loc_rsp.deposit_money_confirm,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                ("check_accounts", "check_banks"): cnd.true() # In any case go back to start of check accounts
            }
        },
        "withdraw_money":{
        RESPONSE:loc_rsp.withdraw_money,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                ("check_accounts", "check_banks"): cnd.regexp(r"back", re.IGNORECASE),
                ("check_accounts", "withdraw_money_confirm"): cnd.true() # In any case forward to get confirmation or rejection message
            }
        },
        "withdraw_money_confirm":{
        RESPONSE:loc_rsp.withdraw_money_confirm,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                ("check_accounts", "check_banks"): cnd.true() # In any case forward to get confirmation or rejection message
            }
        },
    },
    "get_ticker":{
        "overview_ticker":{
        RESPONSE:loc_rsp.overview_ticker,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                lbl.forward(): cnd.true() # If no match, repeast
            }
        },
        "plot_ticker":{
        RESPONSE:loc_rsp.plot_ticker,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                ("get_ticker", "overview_ticker"): cnd.regexp(r"back", re.IGNORECASE),          
                lbl.forward(): cnd.true() # FFrom Plot Ticker, you have the possibility to ask follow questions to the bot
            }
        },
        "QA_ticker":{
        RESPONSE:loc_rsp.QA_ticker,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                ("get_ticker", "overview_ticker"): cnd.regexp(r"back", re.IGNORECASE),
                lbl.repeat(): cnd.true() # If no match, repeat
            }
        }
    },
    "ask_the_bot_creator":{
        "QA_start_ask_the_bot_creator":{
        RESPONSE:loc_rsp.QA_start_ask_the_bot_creator,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE),
                lbl.forward(): cnd.true() # Forward with first Question; transitional step
            }
        },
        "QA_ask_the_bot_creator":{
        RESPONSE:loc_rsp.QA_ask_the_bot_creator,
        TRANSITIONS: {
                lbl.repeat(): loc_cnd.check_language,
                ("global", "bot_introduction"): cnd.regexp(r"start", re.IGNORECASE), 
                ("ask_the_bot_creator", "QA_start_ask_the_bot_creator"): cnd.regexp(r"back", re.IGNORECASE),   
                lbl.repeat(): cnd.true() # If no match go back to overview
            }
        }
    }
}

actor = Actor(plot, start_label=("global", "start"), fallback_label=("global", "fallback"))
