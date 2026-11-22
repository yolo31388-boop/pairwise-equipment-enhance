import pytest
import gameplay.equipment_enhance as mod

CASES = [
    ("server_probability", (1, 2)),
    ("pity_on_fail", (1, 2)),
    ("concurrency_lock", (1, 2)),
    ("requirement_recalc", (1, 2)),
    ("downgrade_floor", (0, 1)),
    ("level_inherit", (1, 2)),
    ("cross_server_map", (10, 2)),
    ("precise_value", (10.5, 2)),
    ("flow_log", (1, 2)),
    ("binding_check", (1, 2)),
    ("rate_table", (0.3, 7)),
    ("material_consume", (1, 2)),
    ("attempt_count", (1, 2)),
    ("result_apply", (1, 2)),
    ("max_level", (10, 20)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
