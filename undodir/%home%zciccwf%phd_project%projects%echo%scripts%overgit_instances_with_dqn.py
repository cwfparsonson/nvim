Vim�UnDo� �Hf���e�(�S�϶[][�m7�F���   h   1                        checkpoint_frequency=200,   `   -      9       9   9   9    a7+w    _�                             ����                                                                                                                                                                                                                                                                                                                                                             a7**     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        a7*-     �                  5�_�                       2    ����                                                                                                                                                                                                                                                                                                                                                  V        a7*K     �         W      A    instances_path = 'instances_to_overfit/nrows_500_ncols_1000/'5�_�                       =    ����                                                                                                                                                                                                                                                                                                                                                  V        a7*N     �         W      A    instances_path = 'instances_to_overfit/nrows_100_ncols_1000/'5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                  V        a7*Q    �         W      ,    instances.readProblem(instance_paths[9])5�_�                    ,   )    ����                                                                                                                                                                                                                                                                                                                                                  V        a7*a     �   ,   C   W    �   ,   -   W    5�_�                    %       ����                                                                                                                                                                                                                                                                                                                            ,          %          V       a7*d     �   $   %          /    policy_network = BipartiteGCN(RLGNN_DEVICE,   ,                               emb_size=128,   ,                               num_rounds=2,   -                               cons_nfeats=5,   -                               edge_nfeats=1,   5                               var_nfeats=19, # 19 20   0                               aggregator='add')   �    policy_network.load_state_dict(torch.load('/scratch/datasets/echo/supervised_learner/gnn/gnn_266/checkpoint_235/trained_params.pkl'))5�_�      	              %       ����                                                                                                                                                                                                                                                                                                                            %          %          V       a7*f     �   $   &   e          # init value network5�_�      
           	   %       ����                                                                                                                                                                                                                                                                                                                            %          %          V       a7*f     �   $   &   e          #  value network5�_�   	              
   $        ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*g    �   #   $              # policy network5�_�   
                 $       ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*i    �   #   %   d          # value network5�_�                    *   )    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*p     �   )   +   d      .                                emb_size=1024,5�_�                    *   )    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*q     �   )   +   d      *                                emb_size=,5�_�                    +   ,    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*u     �   *   ,   d      -                                num_rounds=8,5�_�                    (   )    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�    �   '   )          y    # init_value_network_path = '/scratch/datasets/echo/supervised_learner/gnn/gnn_296/checkpoint_102/network_params.pkl'5�_�                    *   )    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�     �   )   +   d      -                                emb_size=128,5�_�                    *   )    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�     �   )   +   d      *                                emb_size=,5�_�                    *   )    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�     �   )   +   d      ,                                emb_size=64,5�_�                    *   )    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�     �   )   +   d      *                                emb_size=,5�_�                    +   ,    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�     �   *   ,   d      -                                num_rounds=4,5�_�                    2   +    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�     �   1   3   d      -                                num_rounds=8,5�_�                    2   +    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�     �   1   3   d      ,                                num_rounds=,5�_�                    1   )    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�     �   0   2   d      .                                emb_size=1024,5�_�                    1   )    ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�    �   0   2   d      *                                emb_size=,5�_�                    "       ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�     �   !   #   d          RLGNN_DEVICE = 'cuda:5'5�_�                    "       ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�     �   !   #   d          RLGNN_DEVIC2iE = 'cuda:5'5�_�                    "       ����                                                                                                                                                                                                                                                                                                                            $          $          V       a7*�    �   !   #   d           = 'cuda:5'5�_�                    "        ����                                                                                                                                                                                                                                                                                                                            "   	       "   	       V   	    a7*�     �   !   "              device = 'cuda:5'5�_�                            ����                                                                                                                                                                                                                                                                                                                            "   	       "   	       V   	    a7*�     �         c    �         c    5�_�                           ����                                                                                                                                                                                                                                                                                                                            #   	       #   	       V   	    a7*�    �         e          �         d    5�_�                     "        ����                                                                                                                                                                                                                                                                                                                            "          "          V       a7*�     �   !   "          "    print('Initialised instance.')5�_�      !               "        ����                                                                                                                                                                                                                                                                                                                            "           "           V        a7*�    �   !   "           5�_�       "           !           ����                                                                                                                                                                                                                                                                                                                                                  V        a7*�     �                *    # for instance_path in instance_paths:5�_�   !   #           "           ����                                                                                                                                                                                                                                                                                                                                                  V        a7*�   	 �                 5�_�   "   $           #   6       ����                                                                                                                                                                                                                                                                                                                                                  V        a7*�     �   6   8   a    5�_�   #   %           $   7       ����                                                                                                                                                                                                                                                                                                                                                  V        a7*�     �   6   9   b              5�_�   $   &           %   8       ����                                                                                                                                                                                                                                                                                                                                                  V        a7*�     �   7   :   c          # exploration network5�_�   %   '           &   @       ����                                                                                                                                                                                                                                                                                                                                                  V        a7*�     �   @   H   d    �   @   A   d    5�_�   &   (           '   <       ����                                                                                                                                                                                                                                                                                                                            @          <          V       a7*�   
 �   ;   <          @    rlgnn_agent = REINFORCEAgent(policy_network=policy_network,    6                                 device=RLGNN_DEVICE,    1                                 temperature=1.0,   /                                 name='rl_gnn')   ,    rlgnn_agent.train() # turn on train mode5�_�   '   )           (      *    ����                                                                                                                                                                                                                                                                                                                            <          <          V       a7*�     �          f      *from echo.learners import REINFORCELearner5�_�   (   *           )      +    ����                                                                                                                                                                                                                                                                                                                            <          <          V       a7+     �          f      6from echo.learners import REINFORCELearner, DQNLearner5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                            <          <          V       a7+	     �         f      <from echo.agents import REINFORCEAgent, StrongBranchingAgent5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                            <          <          V       a7+	    �         f      .from echo.agents import , StrongBranchingAgent5�_�   +   -           ,   a       ����                                                                                                                                                                                                                                                                                                                            <          <          V       a7+$     �   a      f    �   a   b   f    5�_�   ,   .           -   K       ����                                                                                                                                                                                                                                                                                                                            a          K          V       a7+*     �   J   K          1    learner = REINFORCELearner(agent=rlgnn_agent,   '                               env=env,   3                               instances=instances,   &                               seed=0,   A                               max_steps=int(1e12), # 5000 10 5 3   4                               max_steps_agent=None,   >                               batch_size=512, # 512 32 16 8 1   Q                               baseline='mean', # None 'sb' 'mean' 'pc' 'gr' 'sr'   �                               agent_reward='num_nodes', # 'num_nodes' 'primal_dual_integral' 'dual_integral' 'dual_bound' 'primal_dual_gap' 'primal_dual_gap_frac' 'dual_bound_frac'   '                               lr=1e-3,   *                               gamma=0.99,   9                               turn_off_heuristics=False,   Q                               threshold_difficulty=None, # None 250 100 50 75 30   4                               threshold_agent=None,   2                               threshold_env=None,   V                               action_filter_agent=None, # None StrongBranchingAgent()   @                               action_filter_percentile=10, # 90   9                               validation_frequency=None,   7                               episode_log_frequency=1,   G                               # path_to_save='/scratch/datasets/echo',   ;                               path_to_save=instances_path,   8                               checkpoint_frequency=100,                                   )5�_�   -   /           .   g        ����                                                                                                                                                                                                                                                                                                                            g          i           V       a7+=    �   f   g              learner.train(int(5e5))   s    print('Initialised learner with params {}. Will save to {}'.format(learner.episodes_log, learner.path_to_save))    5�_�   .   0           /   d        ����                                                                                                                                                                                                                                                                                                                            d           d           V       a7+A    �   c   d           5�_�   /   1           0   N   "    ����                                                                                                                                                                                                                                                                                                                            d           d           V       a7+N     �   M   O   h      J                        max_steps=100, # dont infinite loop while training5�_�   0   2           1   N   "    ����                                                                                                                                                                                                                                                                                                                            d           d           V       a7+N     �   M   O   h      G                        max_steps=, # dont infinite loop while training5�_�   1   3           2   R   *    ����                                                                                                                                                                                                                                                                                                                            d           d           V       a7+]     �   Q   S   h      0                        steps_per_update=5, # 255�_�   2   4           3   S   .    ����                                                                                                                                                                                                                                                                                                                            d           d           V       a7+`    �   R   T   h      9                        prob_add_to_buffer=0.5, # 1.0 0.15�_�   3   5           4   ]   (    ����                                                                                                                                                                                                                                                                                                                            ]   +       ]   +       V   +    a7+l     �   \   ^   h      8                        threshold_agent=threshold_agent,5�_�   4   6           5   ]   (    ����                                                                                                                                                                                                                                                                                                                            ]   +       ]   +       V   +    a7+l     �   \   ^   h      )                        threshold_agent=,5�_�   5   7           6   ^   &    ����                                                                                                                                                                                                                                                                                                                            ]   +       ]   +       V   +    a7+n     �   ]   _   h      4                        threshold_env=threshold_env,5�_�   6   8           7   ^   &    ����                                                                                                                                                                                                                                                                                                                            ]   +       ]   +       V   +    a7+o    �   ]   _   h      '                        threshold_env=,5�_�   7   9           8   `   -    ����                                                                                                                                                                                                                                                                                                                            ]   +       ]   +       V   +    a7+v     �   _   a   h      1                        checkpoint_frequency=200,5�_�   8               9   `   -    ����                                                                                                                                                                                                                                                                                                                            ]   +       ]   +       V   +    a7+v    �   _   a   h      .                        checkpoint_frequency=,5��