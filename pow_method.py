import numpy as np
def pow_method(M, thre=0.01):
    """
    M: Symmetric Matrix
    """
    n, _ = M.shape
    v = np.ones(n)/np.sqrt(n)
    eig = v.dot(M.dot(v))
    
    while True:
        Mv = M.dot(v)
        v_ = Mv/np.linalg.norm(Mv)
        eig_ = v_.dot(M.dot(v_))
        
        if np.abs(eig-eig_)<thre: return eig_, v_
        
        v = v_
        eig = eig_