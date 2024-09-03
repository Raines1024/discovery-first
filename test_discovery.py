import pm4py
import sys


if __name__ == "__main__":

    # 加载 .xes 文件
    BPIC13_i = pm4py.read_xes('BPIC13_i.xes')
    BPIC13_cp = pm4py.read_xes('BPIC13_cp.xes')
    BPIC15_1f = pm4py.read_xes("BPIC15_1f.xes")
    BPIC15_2f = pm4py.read_xes("BPIC15_2f.xes")
    BPIC15_4f = pm4py.read_xes("BPIC15_4f.xes")
    BPIC15_5f = pm4py.read_xes("BPIC15_5f.xes")


    if len(sys.argv) > 1:
        # 获取第一个命令行参数
        param = sys.argv[1]
        print(f"第一个命令行参数是: {param}")
        if param == "minimum_self_distance":
            # 该算法计算事件日志中观察到的每个活动的最小自身距离
            msd = pm4py.derive_minimum_self_distance(BPIC13_i, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            msd = pm4py.derive_minimum_self_distance(BPIC13_cp, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            msd = pm4py.derive_minimum_self_distance(BPIC15_1f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            msd = pm4py.derive_minimum_self_distance(BPIC15_2f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            msd = pm4py.derive_minimum_self_distance(BPIC15_4f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            msd = pm4py.derive_minimum_self_distance(BPIC15_5f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

        elif param == "bpmn_inductive":
            # 使用 Induction Miner 算法发现 BPMN
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC13_i, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC13_cp, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC15_1f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC15_2f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC15_4f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC15_5f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
        elif param == "dfg":
            # 从日志中发现直接跟随图（DFG）
            dfg, start_activities, end_activities = pm4py.discover_dfg(BPIC13_i, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
            dfg, start_activities, end_activities = pm4py.discover_dfg(BPIC13_cp, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
            dfg, start_activities, end_activities = pm4py.discover_dfg(BPIC15_1f, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
            dfg, start_activities, end_activities = pm4py.discover_dfg(BPIC15_2f, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
            dfg, start_activities, end_activities = pm4py.discover_dfg(BPIC15_4f, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
            dfg, start_activities, end_activities = pm4py.discover_dfg(BPIC15_5f, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
        elif param == "heuristics_net":
            # 发现启发式网络
            heu_net = pm4py.discover_heuristics_net(BPIC13_i, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            heu_net = pm4py.discover_heuristics_net(BPIC13_cp, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            heu_net = pm4py.discover_heuristics_net(BPIC15_1f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            heu_net = pm4py.discover_heuristics_net(BPIC15_2f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            heu_net = pm4py.discover_heuristics_net(BPIC15_4f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            heu_net = pm4py.discover_heuristics_net(BPIC15_5f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
        elif param == "log_skeleton":
            # 从事件日志中发现日志骨架
            log_skeleton = pm4py.discover_log_skeleton(BPIC13_i, noise_threshold=0.1, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC13_cp, noise_threshold=0.1, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_1f, noise_threshold=0.1, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_2f, noise_threshold=0.1, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_4f, noise_threshold=0.1, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_5f, noise_threshold=0.1, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

    else:
        print("没有提供任何命令行参数")


