import numpy as np

def shiftL(s):
    l = s.shape[0]
    state = np.zeros([l,l])
    state[:,0:l-1] = s[:,1:l]
    return state

def shiftR(s):
    l = s.shape[0]
    state = np.zeros([l,l])
    state[:,1:l] = s[:,0:l-1]
    return state

def shiftU(s):
    l = s.shape[0]
    state = np.zeros([l,l])
    state[0:l-1,:] = s[1:l,:]
    return state

def shiftD(s):
    l = s.shape[0]
    state = np.zeros([l,l])
    state[1:l,:] = s[0:l-1,:]
    return state

def shiftUL(state):
    return shiftU(shiftL(state))

def shiftUR(state):
    return shiftU(shiftR(state))

def shiftDL(state):
    return shiftD(shiftL(state))

def shiftDR(state):
    return shiftU(shiftR(state))

def shiftState(s):
    state = [shiftL(s),shiftR(s),shiftU(s),shiftD(s),shiftUL(s),shiftUR(s),shiftDL(s),shiftDR(s)]
    return state
