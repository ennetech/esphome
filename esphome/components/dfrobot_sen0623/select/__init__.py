import esphome.codegen as cg
from esphome.components import select
import esphome.config_validation as cv
from esphome.const import ENTITY_CATEGORY_CONFIG

from .. import CONF_DFROBOT_SEN0623_ID, DfrobotSen0623Component, dfrobot_sen0623_ns

DEPENDENCIES = ["dfrobot_sen0623"]

Sen0623ModeSelect = dfrobot_sen0623_ns.class_(
    "Sen0623ModeSelect",
    select.Select,
    cg.Parented.template(DfrobotSen0623Component),
)

CONF_MODE = "mode"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_DFROBOT_SEN0623_ID): cv.use_id(DfrobotSen0623Component),
        cv.Required(CONF_MODE): select.select_schema(
            Sen0623ModeSelect,
            entity_category=ENTITY_CATEGORY_CONFIG,
        ),
    }
)


async def to_code(config):
    parent = await cg.get_variable(config[CONF_DFROBOT_SEN0623_ID])
    if mode := config.get(CONF_MODE):
        sel = await select.new_select(
            mode,
            options=["fall", "sleep"],
        )
        await cg.register_parented(sel, parent)
        cg.add(parent.set_mode_select(sel))
