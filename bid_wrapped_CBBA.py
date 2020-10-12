# HIPC Paper: https://apps.dtic.mil/dtic/tr/fulltext/u2/a627417.pdf
# Implementing BW_CBBA for the TAA part of HIPC. 

class BW_CBBA_Agent:
    def __init__(self, agent_index, all_tasks, bundle, A,num_agents, num_tasks):
        self.agent_index = agent_index
        self.tasks = all_tasks # set of all task 
        self.max_bundle_length = 100 # max times bundle bilding is iterated. (maximum length bundle for agent i can have)
        self.D = 5 # network diameter
        k = 0
        Q = []
        Z = [[0 for i in range(num_agents)] for j in range(num_tasks)]
        while (k < 2*self.D):
            if(len(Q) == 0):
                k = k + 1
            else:
                k = 0
        new_bundle, A = self.BW_bundle_building(A)
        A, Q, Z = BW_Task_Consensus(bundle, new_bundle, A, Q, Z)
        bundle = new_bundle
        return A
    
    def BW_bundle_building(self, A):
        temp_A = []
        task_dict = {}
        for bid in A:
            if(bid[0] != self.agent_index):
                temp_A.append(bid)
                task_dict[bid[1]] = bid[0]
        A = temp_A
        bundle = []
        while (len(bundle) < self.max_bundle_length):
            avail_tasks = []
            c = [0 for i in range(avail_tasks)]
            c_bw = [0 for i in range(avail_tasks)]
            for task in self.tasks:
                if(task not in task_dict):
                    avail_tasks.append(task)
            c = [0 for i in range(avail_tasks)]
            c_bw = [0 for i in range(avail_tasks)]
            h = [0 for i in range(avail_tasks)]
            most_recent_bw_index = 0
            for i,task in enumerate(avail_tasks):
                c[task] = int_score_func(bundle, task)
                c_bw[task] = min(c[task], c[bundle[-1][1]])
                h[task] = indicator_func(A,c, c_bw, task)
            new_max = -9999999
            new_task = 0
            for i in range(len(c)):
                if (c[i] * h[i] > new_max):
                    new_task = i
                    new_max = c[i] * h[i]
            new_bid = (self.agent_index, new_task, c_bw[new_task])
            if(c_bw[new_task] * h[new_task] > 0):
                bundle.append(new_bid)
                for i, bid in enumerate(A):
                    if(bid[1] == new_task):
                        task_dict[new_task] = self.agent_index
                        A[i] = new_bid
            else:
                break
        return (bundle, A)
    
    def BW_Task_Consensus(old_bundle, new_bundle, A, Q, Z):
        Q, Z = BW_Task_Consensus_Update(Q,Z,old_bundle, new_bundle)
        # broadcasting code goes here.
        messages = # receive messages code goes here
        A, Q, Z = BW_Task_Process_Messages(messages, A, Q, Z)
        return (A, Q, Z)
    
    def BW_Task_Consensus_Update(Q, Z, old_bundle, new_bundle):
        # Todo
    
    def BW_Task_Process_Messages(messages, A, Q, Z):
        # Todo


                
