Vim�UnDo� pHʉ?t���:'�H�?$����^|�   r   9                                          show_fig=False,   J   &                       _)��    _�                             ����                                                                                                                                                                                                                                                                                                                                                             _)��    �   I              &#                                     �   J            �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                       ,           V        _)��     �   +   -          B                                                 print_data=False)�   *   ,          _                                                 interarrival_time_dist=interarrival_time_dist,�   )   +          O                                                 flow_size_dist=flow_size_dist,�   (   *          E                                                 node_dist=node_dist,�   '   )          L                                                 eps=config.ENDPOINT_LABELS,�   &   (          Pflow_centric_demand_data = tp.create_demand_data(num_demands=config.NUM_DEMANDS,�   %   '          >                                               xlim=[1e1,1e6])�   $   &          =                                               logscale=True,�   #   %          @                                               print_data=False,�   "   $          >                                               show_fig=False,�   !   #          P                                               params={'_mu': 7.4, '_sigma': 2},�       "          @interarrival_time_dist = tp.gen_named_val_dist(dist='lognormal',�      !          7                                       xlim=[1e2,1e12])�                 :                                       round_to_nearest=1,�                5                                       logscale=True,�                8                                       print_data=False,�                6                                       show_fig=False,�                O                                       params={'_alpha': 1.4, '_lambda': 7000},�                6flow_size_dist = tp.gen_named_val_dist(dist='weibull',�                ^node_dist = tp.gen_uniform_node_dist(config.ENDPOINT_LABELS, show_fig=False, print_data=False)5�_�                    -        ����                                                                                                                                                                                                                                                                                                                            -           U           V        _)��     �   T   V          B#                                                 print_data=True)�   S   U          L#                                                 use_multiprocessing=False,�   R   T          =#                                                 c=config.C,�   Q   S          L#                                                 num_ops_dist=num_ops_dist,�   P   R          `#                                                 interarrival_time_dist=interarrival_time_dist,�   O   Q          P#                                                 flow_size_dist=flow_size_dist,�   N   P          F#                                                 node_dist=node_dist,�   M   O          M#                                                 eps=config.ENDPOINT_LABELS,�   L   N          Q# job_centric_demand_data = tp.create_demand_data(num_demands=config.NUM_DEMANDS,�   K   M          =#                                           print_data=False)�   J   L          ;#                                           show_fig=False,�   I   K          ?#                                           round_to_nearest=1,�   H   J          ;#                                           bg_factor=0.05,�   G   I          E#                                           num_skew_samples=[10000],�   F   H          8#                                           scales=[50],�   E   G          9#                                           skews=[0.05],�   D   F          <#                                           locations=[100],�   C   E          ?#                                           config.MAX_NUM_OPS,�   B   D          ?# num_ops_dist = tp.gen_multimodal_val_dist(config.MIN_NUM_OPS,�   A   C          G#                                                     print_data=False)�   @   B          E#                                                     show_fig=False,�   ?   A          I#                                                     round_to_nearest=1,�   >   @          F#                                                     bg_factor=0.025,�   =   ?          k#                                                     num_skew_samples=[800, 1000, 2000, 4000, 4000, 3000],�   <   >          f#                                                     scales=[0.1, 62, 2000, 7500, 3500000, 20000000],�   ;   =          U#                                                     skews=[0, 100, -10, 10, 50, 6],�   :   <          c#                                                     locations=[1, 1, 3000, 1, 1800000, 10000000],�   9   ;          N#                                                     config.MAX_INTERARRIVAL,�   8   :          N# interarrival_time_dist = tp.gen_multimodal_val_dist(config.MIN_INTERARRIVAL,�   7   9          ?#                                             print_data=False)�   6   8          :#                                             num_bins=34,�   5   7          =#                                             show_fig=False,�   4   6          A#                                             round_to_nearest=1,�   3   5          :#                                             bg_factor=0,�   2   4          G#                                             num_skew_samples=[10000],�   1   3          :#                                             scales=[10],�   0   2          8#                                             skews=[0],�   /   1          =#                                             locations=[50],�   .   0          C#                                             config.MAX_FLOW_SIZE,�   -   /          C# flow_size_dist = tp.gen_multimodal_val_dist(config.MIN_FLOW_SIZE,�   ,   .          `# node_dist = tp.gen_uniform_node_dist(config.ENDPOINT_LABELS, show_fig=False, print_data=False)5�_�                    X        ����                                                                                                                                                                                                                                                                                                                            -           U           V        _)��     �   W   Y          5demand = Demand(demand_data=flow_centric_demand_data)5�_�                    Y        ����                                                                                                                                                                                                                                                                                                                            -           U           V        _)��    �   X   Z          6# demand = Demand(demand_data=job_centric_demand_data)5�_�                    l        ����                                                                                                                                                                                                                                                                                                                            l          l          V       _)�t     �   k   m          +        print('Action:\n{}'.format(action))5�_�                    j        ����                                                                                                                                                                                                                                                                                                                            l          l          V       _)�x     �   i   k          /        print('Time: {}'.format(env.curr_time))5�_�      	              h        ����                                                                                                                                                                                                                                                                                                                            l          l          V       _)�{     �   g   i          7    print('env slots dict:\n{}'.format(env.slots_dict))5�_�      
           	   f        ����                                                                                                                                                                                                                                                                                                                            l          l          V       _)�}    �   e   g          C    print('\nEpisode {}/{}'.format(episode+1, config.NUM_EPISODES))5�_�   	              
   f        ����                                                                                                                                                                                                                                                                                                                            l          l          V       _)��    �   e   g          E    # print('\nEpisode {}/{}'.format(episode+1, config.NUM_EPISODES))5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                       ,           V        _)��    �   +   -          D                                                 # print_data=False)�   *   ,          a                                                 # interarrival_time_dist=interarrival_time_dist,�   )   +          Q                                                 # flow_size_dist=flow_size_dist,�   (   *          G                                                 # node_dist=node_dist,�   '   )          N                                                 # eps=config.ENDPOINT_LABELS,�   &   (          R# flow_centric_demand_data = tp.create_demand_data(num_demands=config.NUM_DEMANDS,�   %   '          @                                               # xlim=[1e1,1e6])�   $   &          ?                                               # logscale=True,�   #   %          B                                               # print_data=False,�   "   $          @                                               # show_fig=False,�   !   #          R                                               # params={'_mu': 7.4, '_sigma': 2},�       "          B# interarrival_time_dist = tp.gen_named_val_dist(dist='lognormal',�      !          9                                       # xlim=[1e2,1e12])�                 <                                       # round_to_nearest=1,�                7                                       # logscale=True,�                :                                       # print_data=False,�                8                                       # show_fig=False,�                Q                                       # params={'_alpha': 1.4, '_lambda': 7000},�                8# flow_size_dist = tp.gen_named_val_dist(dist='weibull',�                `# node_dist = tp.gen_uniform_node_dist(config.ENDPOINT_LABELS, show_fig=False, print_data=False)5�_�                    Y        ����                                                                                                                                                                                                                                                                                                                                       ,           V        _)��     �   X   Z          4demand = Demand(demand_data=job_centric_demand_data)5�_�                    X        ����                                                                                                                                                                                                                                                                                                                                       ,           V        _)��    �   W   Y          7# demand = Demand(demand_data=flow_centric_demand_data)5�_�                    Y        ����                                                                                                                                                                                                                                                                                                                                       ,           V        _)�	     �   X   Z          6# demand = Demand(demand_data=job_centric_demand_data)5�_�                    X        ����                                                                                                                                                                                                                                                                                                                                       ,           V        _)�    �   W   Y          5demand = Demand(demand_data=flow_centric_demand_data)5�_�                    l        ����                                                                                                                                                                                                                                                                                                                                       ,           V        _)�    �   k   m          -        # print('Action:\n{}'.format(action))5�_�                    j        ����                                                                                                                                                                                                                                                                                                                                       ,           V        _)�   	 �   i   k          1        # print('Time: {}'.format(env.curr_time))5�_�                    Y        ����                                                                                                                                                                                                                                                                                                                                       ,           V        _)�j     �   X   Z          4demand = Demand(demand_data=job_centric_demand_data)5�_�                    X        ����                                                                                                                                                                                                                                                                                                                                       ,           V        _)�l   
 �   W   Y          7# demand = Demand(demand_data=flow_centric_demand_data)5�_�                   -        ����                                                                                                                                                                                                                                                                                                                            -           U           V        _)��    �   T   V          @                                                print_data=True)�   S   U          J                                                use_multiprocessing=False,�   R   T          ;                                                c=config.C,�   Q   S          J                                                num_ops_dist=num_ops_dist,�   P   R          ^                                                interarrival_time_dist=interarrival_time_dist,�   O   Q          N                                                flow_size_dist=flow_size_dist,�   N   P          D                                                node_dist=node_dist,�   M   O          K                                                eps=config.ENDPOINT_LABELS,�   L   N          Ojob_centric_demand_data = tp.create_demand_data(num_demands=config.NUM_DEMANDS,�   K   M          ;                                          print_data=False)�   J   L          9                                          show_fig=False,�   I   K          =                                          round_to_nearest=1,�   H   J          9                                          bg_factor=0.05,�   G   I          C                                          num_skew_samples=[10000],�   F   H          6                                          scales=[50],�   E   G          7                                          skews=[0.05],�   D   F          :                                          locations=[100],�   C   E          =                                          config.MAX_NUM_OPS,�   B   D          =num_ops_dist = tp.gen_multimodal_val_dist(config.MIN_NUM_OPS,�   A   C          E                                                    print_data=False)�   @   B          C                                                    show_fig=False,�   ?   A          G                                                    round_to_nearest=1,�   >   @          D                                                    bg_factor=0.025,�   =   ?          i                                                    num_skew_samples=[800, 1000, 2000, 4000, 4000, 3000],�   <   >          d                                                    scales=[0.1, 62, 2000, 7500, 3500000, 20000000],�   ;   =          S                                                    skews=[0, 100, -10, 10, 50, 6],�   :   <          a                                                    locations=[1, 1, 3000, 1, 1800000, 10000000],�   9   ;          L                                                    config.MAX_INTERARRIVAL,�   8   :          Linterarrival_time_dist = tp.gen_multimodal_val_dist(config.MIN_INTERARRIVAL,�   7   9          =                                            print_data=False)�   6   8          8                                            num_bins=34,�   5   7          ;                                            show_fig=False,�   4   6          ?                                            round_to_nearest=1,�   3   5          8                                            bg_factor=0,�   2   4          E                                            num_skew_samples=[10000],�   1   3          8                                            scales=[10],�   0   2          6                                            skews=[0],�   /   1          ;                                            locations=[50],�   .   0          A                                            config.MAX_FLOW_SIZE,�   -   /          Aflow_size_dist = tp.gen_multimodal_val_dist(config.MIN_FLOW_SIZE,�   ,   .          ^node_dist = tp.gen_uniform_node_dist(config.ENDPOINT_LABELS, show_fig=False, print_data=False)5�_�                    -        ����                                                                                                                                                                                                                                                                                                                            -           U           V        _)��     �   T   V          B                                                # print_data=True)�   S   U          L                                                # use_multiprocessing=False,�   R   T          =                                                # c=config.C,�   Q   S          L                                                # num_ops_dist=num_ops_dist,�   P   R          `                                                # interarrival_time_dist=interarrival_time_dist,�   O   Q          P                                                # flow_size_dist=flow_size_dist,�   N   P          F                                                # node_dist=node_dist,�   M   O          M                                                # eps=config.ENDPOINT_LABELS,�   L   N          Q# job_centric_demand_data = tp.create_demand_data(num_demands=config.NUM_DEMANDS,�   K   M          =                                          # print_data=False)�   J   L          ;                                          # show_fig=False,�   I   K          ?                                          # round_to_nearest=1,�   H   J          ;                                          # bg_factor=0.05,�   G   I          E                                          # num_skew_samples=[10000],�   F   H          8                                          # scales=[50],�   E   G          9                                          # skews=[0.05],�   D   F          <                                          # locations=[100],�   C   E          ?                                          # config.MAX_NUM_OPS,�   B   D          ?# num_ops_dist = tp.gen_multimodal_val_dist(config.MIN_NUM_OPS,�   A   C          G                                                    # print_data=False)�   @   B          E                                                    # show_fig=False,�   ?   A          I                                                    # round_to_nearest=1,�   >   @          F                                                    # bg_factor=0.025,�   =   ?          k                                                    # num_skew_samples=[800, 1000, 2000, 4000, 4000, 3000],�   <   >          f                                                    # scales=[0.1, 62, 2000, 7500, 3500000, 20000000],�   ;   =          U                                                    # skews=[0, 100, -10, 10, 50, 6],�   :   <          c                                                    # locations=[1, 1, 3000, 1, 1800000, 10000000],�   9   ;          N                                                    # config.MAX_INTERARRIVAL,�   8   :          N# interarrival_time_dist = tp.gen_multimodal_val_dist(config.MIN_INTERARRIVAL,�   7   9          ?                                            # print_data=False)�   6   8          :                                            # num_bins=34,�   5   7          =                                            # show_fig=False,�   4   6          A                                            # round_to_nearest=1,�   3   5          :                                            # bg_factor=0,�   2   4          G                                            # num_skew_samples=[10000],�   1   3          :                                            # scales=[10],�   0   2          8                                            # skews=[0],�   /   1          =                                            # locations=[50],�   .   0          C                                            # config.MAX_FLOW_SIZE,�   -   /          C# flow_size_dist = tp.gen_multimodal_val_dist(config.MIN_FLOW_SIZE,�   ,   .          `# node_dist = tp.gen_uniform_node_dist(config.ENDPOINT_LABELS, show_fig=False, print_data=False)5�_�                    Y        ����                                                                                                                                                                                                                                                                                                                            -           U           V        _)��     �   X   Z          6# demand = Demand(demand_data=job_centric_demand_data)5�_�                    X        ����                                                                                                                                                                                                                                                                                                                            -           U           V        _)��     �   W   Y          5demand = Demand(demand_data=flow_centric_demand_data)5�_�                     X        ����                                                                                                                                                                                                                                                                                                                            -           U           V        _)��    �   W   Y          5demand = Demand(demand_data=flow_centric_demand_data)5�_�                   -        ����                                                                                                                                                                                                                                                                                                                            -           -           V        _)�u     �   ,   /   r      �node_dist = tp.gen_uniform_node_dist(config.ENDPOINT_LABELS, show_fig=False, print_data=False) flow_size_dist = tp.gen_multimodal_val_dist(config.MIN_FLOW_SIZE,5�_�                    -   ^    ����                                                                                                                                                                                                                                                                                                                            -           -           V        _)�w     �   I   K   q      &#                                     5�_�                    J   %    ����                                                                                                                                                                                                                                                                                                                            -           -           V        _)�x     �   I   L   q      7#                                     print_data=False)5�_�                     J   &    ����                                                                                                                                                                                                                                                                                                                            -           -           V        _)�x     �   I   L   p      �#                                     print_data=False) job_centric_demand_data = tp.create_demand_data(num_demands=config.NUM_DEMANDS,5��