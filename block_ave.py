def calc_block_ave_std(data, n_block):
    data = np.array(data)
    blocked_data = data.reshape(n_block, -1)
    blocked_aves = np.mean(blocked_data, axis=1)
    blocked_ave  = np.mean(blocked_aves)
    blocked_stds =  np.std(blocked_aves)
    return blocked_ave, blocked_stds
