Vim�UnDo� u��{���B���������Ŝ0jJ��%[��   +                                  `��/    _�                            ����                                                                                                                                                                                                                                                                                                                                                             `��     �         +    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `��     �         ,          5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       `��$     �             
   num_repeats = 100 # 100    num_tasks_per_repeat = 100 # 100   4pbar = tqdm(total=num_repeats*num_tasks_per_repeat,                miniters=1,                # mininterval=1,               maxinterval=1,               desc='Testing',                leave=False,                smoothing=0)   start = time.time()5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       `��&     �         #    �         #    5�_�                            ����                                                                                                                                                                                                                                                                                                                                       -           V        `��)    �                 num_repeats = 100 # 100    num_tasks_per_repeat = 100 # 100   4pbar = tqdm(total=num_repeats*num_tasks_per_repeat,                miniters=1,                # mininterval=1,               maxinterval=1,               desc='Testing',                leave=False,                smoothing=0)   start = time.time()       !for repeat in range(num_repeats):   7    pool = multiprocessing.Pool(10, maxtasksperchild=1)   �    results = [pool.apply_async(do_work, args=(repeat,), callback=lambda _: pbar.update(1)) for _ in range(num_tasks_per_repeat)]   �    # results = [pool.apply_async(do_work, args=(repeat,), callback=functools.partial(pbar.update, 1)) for _ in range(num_tasks_per_repeat)]   �    # results = [pool.apply_async(do_work, args=(repeat,), callback=functools.partial(update_pbar, pbar)) for _ in range(num_tasks_per_repeat)]       pool.close()       pool.join()   '    output = [p.get() for p in results]       del pool       jobs = output       end = time.time()   pbar.close()   2print('Completed test in {} s.'.format(end-start))5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        `��-     �                    # time.sleep(0.1)5�_�                             ����                                                                                                                                                                                                                                                                                                                                                  V        `��.    �                    # time.sleep(0.01)5��