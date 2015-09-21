
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow.interactive_replayer import InteractiveReplayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose  forwarding.consistency --consistent=False --deny=False  --update_wait=10 --update_once=True --consistent_sleep=5 --barriers=False  openflow.of_01 --address=__address__ --port=__port__ ', label='c1', address='127.0.0.1', cwd='pox/')],
                 topology_class=ConsistencyTopology,
                 topology_params="",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 ignore_interposition=False,
                 kill_controllers_on_exit=True)

control_flow = InteractiveReplayer(simulation_config, "traces/trace_pox_ConsistencyTopology-False-False-steps200/events.trace")
# wait_on_deterministic_values=False
# delay_flow_mods=False
# Invariant check: 'InvariantChecker.check_liveness'
# Bug signature: ""
